import logging
from http import HTTPStatus as Status
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.views.generic import View
from tblog_app.models import Post
from collections import Counter

logger = logging.getLogger('django')


class TagView(View):
    def get(self, *args, **kwargs):
        try:
            tags = [model_to_dict(obj)['tag'] for obj in Post.tags.through.objects.all()]
            c = Counter(tags)
            data = [tag for tag, _ in c.most_common()]
            return JsonResponse({'message': '', 'data': data}, status=Status.OK)
        except Exception as e:
            logger.error(e, exc_info=True)
            return JsonResponse({'message': '', 'data': []}, status=Status.INTERNAL_SERVER_ERROR)


'''
    def post(self, request: HttpRequest, *args, **kwargs):
        try:
            if kwargs['pk'] != '':
                raise Exception('pk should be empty')

            data = json.loads(request.body.decode('utf-8'))
            project = Post(**data)
            project.save()
            logger.info(f'post {project.id} is created with param {data}')
            return JsonResponse({'message': f'{data["title"]} is created', 'data': []}, status=Status.CREATED)
        except Exception as e:
            logger.error(e, exc_info=True)
            return JsonResponse({'message': str(e), 'data': []}, status=Status.INTERNAL_SERVER_ERROR)

    def put(self, request: HttpRequest, *args, **kwargs):
        try:
            if kwargs['pk'] == '':
                raise Exception('pk shouldn\'t be empty')

            data = json.loads(request.body.decode('utf-8'))
            Post.objects.filter(pk=kwargs['pk']).update(**data)
            logger.info(f'post {kwargs["pk"]} is replaced with param {data}')
            return JsonResponse({'message': f'{data["title"]} is replaced'}, status=Status.OK)
        except Exception as e:
            logger.error(e, exc_info=True)
            return JsonResponse({'message': str(e), 'data': []}, status=Status.INTERNAL_SERVER_ERROR)

    def delete(self, *args, **kwargs):
        try:
            if kwargs['pk'] == '':
                raise Exception('pk shouldn\'t be empty')
            Post.objects.filter(pk=kwargs['pk']).delete()
            logger.info(f'post {kwargs["pk"]} is deleted')
            return JsonResponse({'message': f'{kwargs["pk"]} is deleted'}, status=Status.OK)
        except Exception as e:
            logger.error(e, exc_info=True)
            return JsonResponse({'message': str(e), 'data': []}, status=Status.INTERNAL_SERVER_ERROR)'''
