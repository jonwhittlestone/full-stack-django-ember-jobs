from django.conf.urls import url
from django.contrib import admin

from .views import (
    JobListAPIView,
    )


urlpatterns = [
    url(r'^$', JobListAPIView.as_view(), name='list'),
    # Todo. GET /jobs/{id}      PostDetailAPIView
]