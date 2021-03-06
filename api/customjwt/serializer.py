import jwt
from rest_framework_jwt.serializers import RefreshJSONWebTokenSerializer
from calendar import timegm
from datetime import datetime, timedelta

from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import ugettext as _
from rest_framework import serializers
from .compat import Serializer

from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.compat import get_username_field, PasswordField

User = get_user_model()
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
jwt_get_username_from_payload = api_settings.JWT_PAYLOAD_GET_USERNAME_HANDLER


class RefreshJSONWebTokenIsActiveSerializer(RefreshJSONWebTokenSerializer):

	def validate(self, attrs):
		token = attrs['token']

		payload = self._check_payload(token=token)
		user = self._check_user(payload=payload)
		# Get and check 'orig_iat'
		if user.is_active == False:
			return {'error': 'User is not activated'}
		orig_iat = payload.get('orig_iat')

		if orig_iat:
			# Verify expiration
			refresh_limit = api_settings.JWT_REFRESH_EXPIRATION_DELTA

			if isinstance(refresh_limit, timedelta):
				refresh_limit = (refresh_limit.days * 24 * 3600 +
								 refresh_limit.seconds)

			expiration_timestamp = orig_iat + int(refresh_limit)
			now_timestamp = timegm(datetime.utcnow().utctimetuple())

			if now_timestamp > expiration_timestamp:
				msg = _('Refresh has expired.')
				raise serializers.ValidationError(msg)
		else:
			msg = _('orig_iat field is required.')
			raise serializers.ValidationError(msg)

		new_payload = jwt_payload_handler(user)
		new_payload['orig_iat'] = orig_iat

		return {
			'token': jwt_encode_handler(new_payload),
			'user': user
		}