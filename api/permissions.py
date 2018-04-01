from rest_framework.permissions import IsAuthenticated, BasePermission

class IsCreator(BasePermission):
	def has_object_permission(self, request, view, obj):
		return obj.creator == request.user
		
class IsBettor(BasePermission):
	def has_object_permission(self, request, view, obj):
		return obj.bettor == request.user