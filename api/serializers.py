from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from .models import *
import sys


class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ('username', 'email', 'password', 'first_name', 'last_name', 'date_joined', 'last_login',)
		extra_kwargs = {#'password': {'write_only': True}, 
						'username': {'validators': []}}
		read_only_fields = ('date_joined', 'last_login')


class ProfileSerializer(serializers.ModelSerializer):
	user = UserSerializer()

	class Meta:
		model = Profile
		fields = ('user', 'profile_picture', 'rate', 'info', 'sum', 'bets', 'events', 'activity_rate', 'win_rate',)
		read_only_fields = ('user', 'bets', 'events',)

	def create(self, validated_data):
		user_data = validated_data.pop('user')
		user = User.objects.create(
			username=user_data['username'],
			email=user_data['email'],
			password=make_password(user_data['password']),
			first_name = user_data['first_name'],
			last_name = user_data['last_name']
		)
		my_user = Profile.objects.create(user=user, **validated_data)
		return my_user

	def update(self, instance, validated_data):
		if validated_data.get('rate') or validated_data.get('sum') or validated_data.get('bets') or validated_data.get('events') or validated_data.get('activity_rate') or validated_data.get('win_rate'):
			raise serializers.ValidationError("Fields except info, picture and password can't be updated.")
		instance.profile_picture = validated_data.get('profile_picture', instance.profile_picture)
		instance.info = validated_data.get('info', instance.info)
		instance.save()
		user_data = validated_data.get('user')
		if user_data:
			user = instance.user
			new_password = user_data.get('password')
			user.password = make_password(new_password) if new_password else user.password
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

	def create(self, validated_data):
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
		p = Profile.objects.get(user = validated_data['creator'])
		p.events+=1
		p.save()
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

	def create(self, validated_data):
		options = validated_data.pop('options')
		event = Event.objects.create(
			creator = validated_data['creator'],
			name = validated_data['name'],
			type = "Prediction",
			expired = validated_data['expired'],
			description = validated_data['description'],
			currency_pair = validated_data['currency_pair'],
			exchange = validated_data['exchange'],			
		)
		if options:
			for option in options:
				Option.objects.create(**option, prediction = event)
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
		sum = validated_data.get('sum')
		p = Profile.objects.get(user = validated_data.get('bettor'))
		if p.sum - sum >= 0:
			p.bets+=1
			p.sum-=sum
			p.save()
		else:
			raise serializers.ValidationError("Not enough funds on bettor wallet.")
		o = validated_data.get('option')
		o.total_users+=1
		o.total_sum+=sum
		e = o.event
		e.total_users+=1
		e.total_sum+=sum
		o.save()
		e.save()
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
		sum = validated_data.get('sum')
		if validated_data.get('stake')<=0:
			raise serializers.ValidationError("Incorrect token price stake. Token can't cost 0 or less.")
		p = Profile.objects.get(user = validated_data.get('bettor'))
		if p.sum - sum >= 0:
			p.bets+=1
			p.sum-=sum
			p.save()
		else:
			raise serializers.ValidationError("Not enough funds on bettor wallet.")
		p.bets+=1
		p.sum-=validated_data.get('sum')
		p.save()
		e = validated_data.get('event')
		e.total_users+=1
		e.total_sum+=validated_data.get('sum')
		e.save()
		return AccurateBet.objects.create(
			event = validated_data.get('event'), 
			bettor = validated_data.get('bettor'), 
			sum = validated_data.get('sum'), 
			stake = validated_data.get('stake'))


class ParleySerializer(serializers.ModelSerializer):

	event = serializers.PrimaryKeyRelatedField(queryset = Event.objects.filter(type = "Parley"))
	creator = serializers.SlugRelatedField(slug_field = 'username', queryset = User.objects.all())
	bettor = serializers.SlugRelatedField(slug_field = 'username', queryset = User.objects.all(), required = False, allow_null = True)

	class Meta:
		model = Parley
		fields = ('id', 'event', 'creator', 'bettor', 'created', 'koefficient', 'min_sum', 'max_sum', 'status', 'bet_sum', )
		read_only_fields = ('id', 'created', 'status', 'bettor',)

	def create(self, validated_data):
		if validated_data.get('max_sum') * validated_data.get('koefficient') > Profile.objects.get(user = validated_data.get('creator')).sum:
			raise serializers.ValidationError("Creator won't be able to pay that sum. Please decrease maximum sum possible to bet.")
		p = Profile.objects.get(user = validated_data.get('creator'))
		p.bets+=1
		p.sum-=validated_data.get('bet_sum') * instance.koefficient
		p.save()
		e = validated_data.get('event')
		e.total_users+=1
		e.total_sum+=validated_data.get('bet_sum') * instance.koefficient
		return Parley.objects.create(
			event = e,
			creator = p,
			koefficient = validated_data.get('koefficient'),
			min_sum = validated_data.get('min_sum'),
			max_sum = validated_data.get('max_sum'),
			status = "Waiting",
			)
	
	def update(self, instance, validated_data):
		p = Profile.objects.get(user = validated_data.get('bettor'))
		if p.sum - validated_data.get('bet_sum')>=0:
			p.sum-=validated_data.get('bet_sum')
		else:
			raise serializers.ValidationError("Not enough funds on bettor wallet.")
		p.bets+=1
		p.save()
		e = instance.event
		e.total_users+=1
		e.total_sum+= validated_data.get('bet_sum')
		e.save()
		instance.bettor = validated_data.get('bettor', instance.bettor)
		instance.bet_sum = validated_data.get('bet_sum', instance.bet_sum)
		instance.status = "Ready"
		instance.save()
		return instance










