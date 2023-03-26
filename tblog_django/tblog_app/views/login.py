import json
import logging
import jwt
from http import HTTPStatus as Status
from django.views.generic import View
from django.http import HttpRequest, JsonResponse
from django.conf import settings

logger = logging.getLogger('django')


class LoginView(View):
    def post(self, request: HttpRequest, *args, **kwargs):
        try:
            data = json.loads(request.body.decode('utf-8'))
            is_su = True if data['email'] == settings.SU_EMAIL else False
            encoded_jwt = jwt.encode({'email': data['email'], 'isSu': is_su}, settings.SECRET_KEY, algorithm='HS256')
            return JsonResponse({'message': '', 'data': [{'isSu': is_su, 'encodedJwt': encoded_jwt}]}, status=Status.OK)
        except Exception as e:
            logger.error(e, exc_info=True)
            return JsonResponse({'message': '', 'data': []}, status=Status.INTERNAL_SERVER_ERROR)
