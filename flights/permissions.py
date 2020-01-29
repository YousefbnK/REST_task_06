from datetime import date 

from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
	message = "Bugger off or contact staff member"

	def has_object_permission(self, request, view, obj):
		if request.user.is_staff or (obj.user == request.user):
			return True

		return False

class IsModified(BasePermission):
	message = "You snooze you lose sucker !"

	def has_object_permission(self, request, view, obj):
		if (obj.date - date.today()).days > 3:
			return True 

		return False