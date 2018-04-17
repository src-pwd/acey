from rest_framework.permissions import IsAuthenticated, BasePermission
from .models import *
from rest_framework import serializers

class IsCreator(BasePermission):
	def has_object_permission(self, request, view, obj):
		return obj.creator == request.user
		
class IsBettor(BasePermission):
	def has_object_permission(self, request, view, obj):
		return obj.bettor == request.user

class BetOnEvent(BasePermission):
	def has_object_permission(self, request, view, obj):
		option_list = Option.objects.filter(event = obj)
		for i in option_list:
			if Bet.objects.filter(bettor = request.user, option = i).exists():
				raise serializers.ValidationError("This user has already made bet on this event.")
		return True
