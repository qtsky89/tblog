from tblog_app import views
from django.urls import re_path

urlpatterns = [
    re_path(r'api/v1/post/?(?P<pk>[\w]*)/?', views.PostView.as_view(), name='api_project'),
    re_path(r'api/v1/tag/?', views.TagView.as_view(), name='api_tag')
]
