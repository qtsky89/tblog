from tblog_app import views
from django.urls import re_path

urlpatterns = [
    re_path(r'api/v1/post/?(?P<pk>[\w]*)/?', views.ProjectView.as_view(), name='api_project'),
]
