import logging
from http import HTTPStatus as Status
from django.http import JsonResponse
from django.views.generic import View

logger = logging.getLogger('django')


class LoginView(View):
    def post(self, *args, **kwargs):
        try:
            return JsonResponse({'message': '', 'data': 'hello world'}, status=Status.OK)
        except Exception as e:
            logger.error(e, exc_info=True)
            return JsonResponse({'message': '', 'data': []}, status=Status.INTERNAL_SERVER_ERROR)
