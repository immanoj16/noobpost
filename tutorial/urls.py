from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^(?P<tutorial_id>\d+)/$', views.tutorial)
]