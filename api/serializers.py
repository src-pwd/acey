from rest_framework import serializers
from django.db import transaction
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from .models import *
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .tokens import account_activation_token
from django.core.mail import send_mail
from django.db.utils import *
from django.conf import settings
import sys
from crontab import CronTab
import os
import pwd
from datetime import datetime
from dateutil.tz import tzutc
sys.path.append('..')
from utils.iden import Iden
import hashlib

LOCAL_DIR = os.path.dirname(os.path.abspath(__file__))
DOMAIN = 'localhost:8000'
BACKGROUND = '#EEEEEE'

class UserSerializer(serializers.ModelSerializer):

	class Meta:

		model = User
		fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name', 'date_joined', 'last_login', 'is_active')
		extra_kwargs = {#'password': {'write_only': True}, 
						'username': {'validators': []}}
		read_only_fields = ('date_joined', 'last_login', 'id')

	def validate(self, data):

		user_qs = User.objects.filter(email=data.get('email'))
		if user_qs.exists():
			raise serializers.ValidationError("This email is already registered.")

		user_qs = User.objects.filter(username__iexact=data.get('username'))
		if user_qs.exists():
			raise serializers.ValidationError("This username already exists.")

		return data

class ProfileSerializer(serializers.ModelSerializer):
	user = UserSerializer()

	class Meta:
		model = Profile
		fields = ('user', 'profile_picture', 'rate', 'info', 'sum', 'bets', 'events', 'activity_rate', 'win_rate',)
		read_only_fields = ('user', 'bets', 'events', 'rate', 'sum', 'activity_rate', 'win_rate', 'profile_picture')

	def create(self, validated_data):
		user_data = validated_data.pop('user')
		with transaction.atomic():
			user = User(
				username=user_data['username'],
				email=user_data.get('email', ''),
				password=make_password(user_data['password']),
				first_name = user_data.get('first_name', ''),
				last_name = user_data.get('last_name', ''),
				is_active = False,
				# is_active = True,
			)
			try:
				user.save()
			except IntegrityError:
				raise serializers.ValidationError("User with username '{}' already exists.".format(user.username))
			profile = Profile.objects.create(user=user, profile_picture = "{0}.svg".format(user.username), sum = 1000, **validated_data)
		mail_subject = 'Activate your ACEY account.'
		message = render_to_string('acc_active_email.html', {
				'user': user,
				'domain': DOMAIN,
				'uid':urlsafe_base64_encode(force_bytes(user.pk)),
				'token':account_activation_token.make_token(user),
			})
		send_mail(mail_subject, message, settings.EMAIL_HOST_USER, [user.email])
		md5_hash = hashlib.md5()
		md5_hash.update(user.username.encode('UTF-8'))
		iden_avatar = Iden(md5_hash.hexdigest(), 'pixel')
		iden_avatar.setBackgroundColor(BACKGROUND)
		iden_avatar.save("user_pictures/"+user.username+'.svg')
		return profile

	def update(self, instance, validated_data):
		
		if validated_data.get('rate') or validated_data.get('sum') or validated_data.get('bets') or validated_data.get('events') or validated_data.get('activity_rate') or validated_data.get('win_rate'):
			raise serializers.ValidationError("Fields except info, picture, password, first and last name can't be updated.")

		instance.profile_picture = validated_data.get('profile_picture', instance.profile_picture)
		instance.info = validated_data.get('info', instance.info)
		instance.save()
		user_data = validated_data.get('user')

		if user_data:
			user = instance.user
			new_password = user_data.get('password')
			user.password = make_password(new_password) if new_password else user.password
			user.last_name = user_data.get('last_name', user.last_name)
			user.first_name = user_data.get('first_name', user.first_name)
			user.save()

		return instance


class OptionSerializer(serializers.ModelSerializer):

	event = serializers.PrimaryKeyRelatedField(queryset = Event.objects.filter(type = "Prediction"), required = False)

	class Meta:
		model = Option
		fields=('id',
				'event',
				'total_users',
				'total_sum',
				'sum_from',
				'sum_to',
				)
		read_only_fields = ('id', 'event', 'total_users', 'total_sum', )


class EventSerializer(serializers.ModelSerializer):

	creator = serializers.SlugRelatedField(slug_field = 'username', queryset = User.objects.all())

	class Meta:
		model = Event
		fields=('id',
				'creator', 
				'name', 
				'status', 
				'type', 
				'created', 
				'expired', 
				'description', 
				'currency_pair', 
				'exchange', 
				'total_users', 
				'total_sum',
				)
		read_only_fields = ('id', 'total_users', 'total_sum', 'created', 'status',)


	@transaction.atomic
	def create(self, validated_data):

		# if validated_data.get('exchange') not in Exchange.objects.only("name"):
		# 	raise serializers.ValidationError("Wrong or unsupported exchange.")

		# currency_from = validated_data.get('currency_pair')[:3]
		# currency_to = validated_data.get('currency_pair')[4:] 
		# currencies = Currencies.objects.only("name")
		# if not currency_from or not currency_to or currency_from not in currencies or currency_to not in currencies or currency_from==currency_to:
		# 	raise serializers.ValidationError("Wrong or unsupported currency pair.")

		timedelta = validated_data['expired'].replace(tzinfo=tzutc())-datetime.now().replace(tzinfo=tzutc())

		if timedelta.seconds < 3600 or timedelta.days < 0:
			raise serializers.ValidationError("Events should expire at least in 1 hour after creating.")

		event = Event.objects.create(
			creator = validated_data['creator'],
			name = validated_data['name'],
			type = validated_data['type'],
			expired = validated_data['expired'],
			description = validated_data['description'],
			currency_pair = validated_data['currency_pair'],
			exchange = validated_data['exchange'],
			status = "New",
		)

		_profile = Profile.objects.select_for_update().get(user = validated_data['creator'])
		_profile.events+=1
		_profile.save()

		cron = CronTab(user = pwd.getpwuid(os.getuid())[0])
		job = cron.new(command = "cd {0}/utils && {1} {0}/utils/close_event.py {2} {3} {4} {5}".format(
			settings.BASE_DIR,
			sys.executable,
			event.exchange,
			event.currency_pair,
			event.id,
			event.type
			)
		)
		
		job.setall("{} {} {} {} *".format(event.expired.minute, event.expired.hour, event.expired.day, event.expired.month))
		cron.write()

		return event


class PredictionSerializer(serializers.ModelSerializer):

	creator = serializers.SlugRelatedField(slug_field = 'username', queryset = User.objects.all())
	options = OptionSerializer(many = True)

	class Meta:
		model = Event
		fields=('id',
				'creator', 
				'name', 
				'status', 
				'type', 
				'created', 
				'expired', 
				'description', 
				'currency_pair', 
				'exchange', 
				'total_users', 
				'total_sum',
				'options',
				)
		read_only_fields = ('status', 'type', 'created', 'total_users', 'total_sum',)

	@transaction.atomic
	def create(self, validated_data):

		options = validated_data.pop('options')

		if validated_data.get('exchange') not in Exchange.objects.only("name"):
			raise serializers.ValidationError("Wrong or unsupported exchange.")

		currency_from = validated_data.get('currency_pair')[:3]
		currency_to = validated_data.get('currency_pair')[4:] 
		currencies = Currencies.objects.only("name")
		if not currency_from or not currency_to or currency_from not in currencies or currency_to not in currencies or currency_from==currency_to:
			raise serializers.ValidationError("Wrong or unsupported currency pair.")

		timedelta = validated_data['expired'].replace(tzinfo=tzutc())-datetime.now().replace(tzinfo=tzutc())

		if timedelta.seconds < 3600 or timedelta.days < 0:
			raise serializers.ValidationError("Events should expire at least in 1 hour after creating.")

		event = Event.objects.create(
			creator = validated_data['creator'],
			name = validated_data['name'],
			type = "Prediction",
			expired = validated_data['expired'],
			description = validated_data['description'],
			currency_pair = validated_data['currency_pair'],
			exchange = validated_data['exchange'],			
		)

		_profile = Profile.objects.select_for_update().get(user = validated_data['creator'])
		_profile.events+=1
		_profile.save()

		if options:
			for option in options:
				Option.objects.create(**option, event = event)

		cron = CronTab(user = pwd.getpwuid(os.getuid())[0])
		job = cron.new(command = "cd {0}/utils && {1} {0}/utils/close_event.py {2} {3} {4} {5}".format(
			settings.BASE_DIR,
			sys.executable,
			event.exchange,
			event.currency_pair,
			event.id,
			"Prediction"
			)
		)
		
		job.setall("{} {} {} {} *".format(event.expired.minute, event.expired.hour, event.expired.day, event.expired.month))
		cron.write()

		return event


class BetSerializer(serializers.ModelSerializer):

	option = serializers.PrimaryKeyRelatedField(queryset = Option.objects.all())
	bettor = serializers.SlugRelatedField(slug_field = 'username', queryset = User.objects.all())

	class Meta:
		model = Bet
		fields=('id',
				'option',
				'bettor',
				'sum',
				)
		read_only_fields = ('id',)

	def create(self, validated_data):

		option_list = Option.objects.filter(event = validated_data.get('option').event)

		for i in option_list:
			if Bet.objects.filter(bettor = validated_data.get('bettor'), option = i).exists():
				raise serializers.ValidationError("This user has already made bet on this event.")

		if validated_data.get('bettor') == validated_data.get('option').event.creator:
			raise serializers.ValidationError("Creator of event can't bet on his event.")
		sum = validated_data.get('sum')

		with transaction.atomic():

			_profile = Profile.objects.select_for_update().get(user = validated_data.get('bettor'))
			if _profile.sum - sum >= 0:
				_profile.bets+=1
				_profile.sum-=sum
				_profile.save()
			else:
				raise serializers.ValidationError("Not enough funds on bettor wallet.")

			_option = validated_data.get('option')
			_option.total_users+=1
			_option.total_sum+=sum
			_event = _option.event
			_event.total_users+=1
			_event.total_sum+=sum
			_option.save()
			_event.save()

		return Bet.objects.create(option = validated_data.get('option'), bettor = validated_data.get('bettor'), sum = sum)


class AccurateBetSerializer(serializers.ModelSerializer):

	event = serializers.PrimaryKeyRelatedField(queryset = Event.objects.filter(type = "AccuratePrediction"))
	bettor = serializers.SlugRelatedField(slug_field = 'username', queryset = User.objects.all())

	class Meta:
		model = AccurateBet
		fields=('id',
				'event',
				'bettor',
				'sum',
				'stake',
				)
		read_only_fields = ('id',)

	def create(self, validated_data):

		if validated_data.get('bettor') == validated_data.get('event').creator:
			raise serializers.ValidationError("Can't bet on your own event.")	

		if AccurateBet.objects.filter(bettor = validated_data.get('bettor'), event = validated_data.get('event')).exists():
			raise serializers.ValidationError("This user has already made bet on this event.")	

		if validated_data.get('stake')<=0:
			raise serializers.ValidationError("Incorrect token price stake. Token can't cost 0 or less.")

		_sum = validated_data.get('sum')
		accurate_bet = None

		with transaction.atomic():

			_profile = Profile.objects.select_for_update().get(user = validated_data.get('bettor'))
			if _profile.sum - _sum >= 0:
				_profile.bets+=1
				_profile.sum-=_sum
				_profile.save()
			else:
				raise serializers.ValidationError("Not enough funds on bettor wallet.")

			_event = validated_data.get('event')
			_event.total_users+=1
			_event.total_sum+=validated_data.get('sum')
			_event.save()
			accurate_bet = AccurateBet.objects.create(
				event = validated_data.get('event'), 
				bettor = validated_data.get('bettor'), 
				sum = validated_data.get('sum'), 
				stake = validated_data.get('stake')
				)

		return accurate_bet


class ParleySerializer(serializers.ModelSerializer):

	event = serializers.PrimaryKeyRelatedField(queryset = Event.objects.filter(type = "Parley"), required = False)
	creator = serializers.SlugRelatedField(slug_field = 'username', queryset = User.objects.all(), required = False)
	bettor = serializers.SlugRelatedField(slug_field = 'username', queryset = User.objects.all(), required = False, allow_null = True)

	class Meta:
		model = Parley
		fields = ('id', 'event', 'creator', 'bettor', 'created', 'koefficient', 'min_sum', 'max_sum', 'status', 'bet_sum', )
		read_only_fields = ('id', 'created', 'status', 'bettor',)

	def validate(self, data):

		user_qs = Parley.objects.filter(event=data.get('event'), creator = data.get('creator'))
		if user_qs.exists():
			raise serializers.ValidationError("Don't cheat. One event - one parley - one user.")

		return data

	def create(self, validated_data):

		if validated_data.get('max_sum') * validated_data.get('koefficient') > Profile.objects.get(user = validated_data.get('creator')).sum:
			raise serializers.ValidationError("Creator won't be able to pay that sum. Please decrease maximum sum possible to bet.")

		parley = None

		with transaction.atomic():

			_profile = Profile.objects.select_for_update().get(user = validated_data.get('creator'))
			_profile.bets+=1
			_profile.sum-=validated_data.get('max_sum') * validated_data.get('koefficient')
			_profile.save()
			_event = validated_data.get('event')
			_event.total_users+=1
			_event.total_sum+=validated_data.get('max_sum') * validated_data.get('koefficient')

			parley = Parley.objects.create(
				event = _event,
				creator = validated_data.get('creator'),
				koefficient = validated_data.get('koefficient'),
				min_sum = validated_data.get('min_sum'),
				max_sum = validated_data.get('max_sum'),
				status = "Waiting",
				)

		return parley

	@transaction.atomic
	def update(self, instance, validated_data):

		if validated_data.get('bettor') == instance.creator:
			raise serializers.ValidationError("Creator can't bet.")

		if (validated_data.get('bet_sum')>instance.max_sum or validated_data.get('bet_sum')<instance.min_sum):
			raise serializers.ValidationError("Invalid sum to bet.")

		_profile = Profile.objects.select_for_update().get(user = validated_data.get('bettor'))
		if _profile.sum - validated_data.get('bet_sum')>=0:
			_profile.sum-=validated_data.get('bet_sum')
		else:
			raise serializers.ValidationError("Not enough funds on bettor wallet.")
		_profile.bets+=1
		_profile.save()

		_profile = Profile.objects.select_for_update().get(user = instance.creator)
		_profile.sum += (instance.max_sum * instance.koefficient - validated_data.get('bet_sum') * instance.koefficient)
		_profile.save()

		_event = instance.event
		_event.total_users+=1
		_event.total_sum+= validated_data.get('bet_sum')
		_event.save()

		instance.bettor = validated_data.get('bettor', instance.bettor)
		instance.bet_sum = validated_data.get('bet_sum', instance.bet_sum)
		instance.status = "Ready"
		instance.save()

		return instance

class ExchangeSerializer(serializers.ModelSerializer):

	class Meta:
		model = Exchange
		fields = "__all__"
		read_only_fields = ('name', 'url')

class CurrenciesSerializer(serializers.ModelSerializer):

	class Meta:
		model = Currencies
		fields = "__all__"
		read_only_fields = ('name',)

class ExchangeCurrenciesSerializer(serializers.ModelSerializer):

	exchange = serializers.SlugRelatedField(slug_field = 'name', queryset = Exchange.objects.filter(), required = False)
	currencies = CurrenciesSerializer(required = False)

	class Meta:
		model = ExchangeCurrencies
		fields = ('exchange', 'сurrencies')
		read_only_fields = ('exchange', 'сurrencies')











