import logging
import json
from http import HTTPStatus as Status
from django.http import JsonResponse
from django.forms.models import model_to_dict
#from django_app.models import Project
from django.views.generic import View

logger = logging.getLogger('django')


class ProjectView(View):
    def get(self, request, *args, **kwargs):
        try:
            return JsonResponse({'message': '', 'data': {}}, status=Status.OK)
        except Exception as e:
            logger.error(e, exc_info=True)
            return JsonResponse({'message': '', 'data': {}}, status=Status.INTERNAL_SERVER_ERROR)

    # def post(self, request, *args, **kwargs):
    #     try:
    #         if kwargs['pk'] != '':
    #             raise Exception('pk should be empty')

    #         data = json.loads(request.body.decode('utf-8'))
    #         project = Project(**data)
    #         project.save()
    #         logger.info(f'{data["name"]} is created with param {data}')
    #         return JsonResponse({'code': 201, 'message': f'{data["name"]} is created'}, status=201)
    #     except Exception as e:
    #         logger.error(e, exc_info=True)
    #         return JsonResponse({'code': 500, 'message': str(e)}, status=500)

    # def put(self, request, *args, **kwargs):
    #     try:
    #         if kwargs['pk'] == '':
    #             raise Exception('pk shouldn\'t be empty')

    #         data = json.loads(request.body.decode('utf-8'))
    #         Project.objects.filter(pk=kwargs['pk']).update(**data)
    #         logger.info(f'{data["name"]} is updated with param {data}')
    #         return JsonResponse({'code': 200, 'message': f'{data["name"]} is updated'}, status=200)

    #     except Exception as e:
    #         logger.error(e, exc_info=True)
    #         return JsonResponse({'code': 500, 'message': str(e)}, status=500)

    # def delete(self, request, *args, **kwargs):
    #     try:
    #         if kwargs['pk'] == '':
    #             raise Exception('pk shouldn\'t be empty')
    #         Project.objects.filter(pk=kwargs['pk']).delete()
    #         logger.info(f'{kwargs["pk"]} is deleted')
    #         return JsonResponse({'code': 200, 'message': f'{kwargs["pk"]} is deleted'}, status=200)
    #     except Exception as e:
    #         logger.error(e, exc_info=True)
    #         return JsonResponse({'code': 500, 'message': str(e)}, status=500)
