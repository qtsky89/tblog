import logging
import json
from http import HTTPStatus as Status
from django.http import HttpRequest, JsonResponse
from django.forms.models import model_to_dict
from tblog_app.models import Post, Tag
from django.views.generic import View
from django.db.models.query import QuerySet
from typing import List

logger = logging.getLogger('django')


class PostView(View):
    def _object_to_tag(self, tags: List[Tag]) -> List[str]:
        ret = [''] * len(tags)
        for i, tag in enumerate(tags):
            ret[i] = tag.name
        return ret

    def _get_query_spec(self, request: HttpRequest) -> QuerySet:
        qs = None
        if 'tag' in request.GET:
            qs = Post.objects.filter(tags=request.GET['tag'])
        else:
            qs = Post.objects.all()
        qs = qs.order_by('-created_date')
        return qs

    def get(self, request: HttpRequest, **kwargs):
        try:
            if kwargs['pk'] == '':
                # build qs
                qs = self._get_query_spec(request)
                data = [model_to_dict(obj) for obj in qs]
                for d in data:
                    del d['body']
            else:
                data = [model_to_dict(Post.objects.get(pk=kwargs['pk']))]

            # convert tag type (object -> type)
            for d in data:
                d['tags'] = self._object_to_tag(d['tags'])

            return JsonResponse({'message': '', 'data': data}, status=Status.OK)
        except Exception as e:
            logger.error(e, exc_info=True)
            return JsonResponse({'message': '', 'data': []}, status=Status.INTERNAL_SERVER_ERROR)

    def post(self, request: HttpRequest, **kwargs):
        try:
            if kwargs['pk'] != '':
                raise Exception('pk should be empty')

            data = json.loads(request.body.decode('utf-8'))
            post = Post(title=data['title'], body=data['body'], description=data['description'])
            post.save()

            # make Tag object and add to Post object
            for tag in data['tags']:
                t = Tag(tag)
                t.save()
                post.tags.add(t)

            logger.info(f'post {post.id} is created with param {data}')
            return JsonResponse({'message': f'post{post.id} is created', 'data': []}, status=Status.CREATED)
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
            return JsonResponse({'message': f'post{kwargs["pk"]} is deleted'}, status=Status.OK)
        except Exception as e:
            logger.error(e, exc_info=True)
            return JsonResponse({'message': str(e), 'data': []}, status=Status.INTERNAL_SERVER_ERROR)
