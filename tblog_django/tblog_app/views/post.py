import logging
import json
from http import HTTPStatus as Status
from django.http import HttpRequest, JsonResponse
from django.forms.models import model_to_dict
from tblog_app.models import Post
from django.views.generic import View

logger = logging.getLogger('django')


class ProjectView(View):
    def get(self, **kwargs):
        try:
            if kwargs['pk'] == '':
                data = [model_to_dict(obj) for obj in Post.objects.all().order_by('created_date')]
            else:
                data = [model_to_dict(Post.objects.get(pk=kwargs['pk']))]

            return JsonResponse({'message': '', 'data': data}, status=Status.OK)
        except Exception as e:
            logger.error(e, exc_info=True)
            return JsonResponse({'message': '', 'data': []}, status=Status.INTERNAL_SERVER_ERROR)

    def post(self, request: HttpRequest, **kwargs):
        try:
            if kwargs['pk'] != '':
                raise Exception('pk should be empty')

            data = json.loads(request.body.decode('utf-8'))
            project = Post(**data)
            project.save()
            logger.info(f'post {data["title"]} is created with param {data}')
            return JsonResponse({'message': f'{data["title"]} is created', 'data': []}, status=Status.CREATED)
        except Exception as e:
            logger.error(e, exc_info=True)
            return JsonResponse({'message': str(e), 'data': []}, status=Status.INTERNAL_SERVER_ERROR)

    def put(self, request: HttpRequest, **kwargs):
        try:
            if kwargs['pk'] == '':
                raise Exception('pk shouldn\'t be empty')

            data = json.loads(request.body.decode('utf-8'))
            Post.objects.filter(pk=kwargs['pk']).update(**data)
            logger.info(f'{data["title"]} is replaced with param {data}')
            return JsonResponse({'message': f'{data["title"]} is replaced'}, status=Status.OK)
        except Exception as e:
            logger.error(e, exc_info=True)
            return JsonResponse({'message': str(e), 'data': []}, status=Status.INTERNAL_SERVER_ERROR)

    def delete(self, **kwargs):
        try:
            if kwargs['pk'] == '':
                raise Exception('pk shouldn\'t be empty')
            Post.objects.filter(pk=kwargs['pk']).delete()
            logger.info(f'{kwargs["pk"]} is deleted')
            return JsonResponse({'message': f'{kwargs["pk"]} is deleted'}, status=Status.OK)
        except Exception as e:
            logger.error(e, exc_info=True)
            return JsonResponse({'message': str(e), 'data': []}, status=Status.INTERNAL_SERVER_ERROR)
