from rest_framework import serializers
from rest_auth.serializers import UserDetailsSerializer
from django.contrib.auth.models import User

class ProfileSerializer(UserDetailsSerializer):

	profile_picture = serializers.ImageField(source = "profile.profile_picture")
	rate = serializers.IntegerField(source = "profile.rate")
	info = serializers.CharField(source = "profile.info")
	sum = serializers.IntegerField(source = "profile.sum")
	bets = serializers.IntegerField(source = "profile.bets")
	events = serializers.IntegerField(source = "profile.events")
	activity_rate = serializers.IntegerField(source = "profile.activity_rate")
	win_rate = serializers.IntegerField(source = "profile.win_rate")

	class Meta:
		model = User
		fields = UserDetailsSerializer.Meta.fields + ('profile_picture', 'rate', 'info', 'events','sum', 'bets', 'activity_rate','win_rate', )

	def update(self, instance, validated_data_):
		profile_data = validated_data.pop('profile', {})
		profile_picture = profile_data.get('profile_picture')
		rate = profile_data.get('rate')
		info = profile_data.get('info')
		events = profile_data.get('events')
		sum = profile_data.get('sum')
		bets = profile_data.get('bets')
		activity_rate = profile_data.get('activity_rate')
		win_rate = profile_data.get('win_rate')

		instance = super(ProfileSerializer, self).update(instance, validated_data)

		profile = instance.profile
		if profile_data:
			if profile_picture:
				profile.profile_picture = profile_picture
			if rate:
				profile.rate = rate
			if info:
				profile.info = info
			if events:
				profile.events = events
			if sum:
				profile.sum = sum
			if bets:
				profile.bets = bets
			if activity_rate:
				profile.activity_rate = activity_rate
			if win_rate:
				profile.win_rate = win_rate
			profile.save()
		return instance



