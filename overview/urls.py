from django.conf.urls import url, include
from .views import overview

urlpatterns = [
    url(r'^$', overview, name='overview'),
]