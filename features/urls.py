from django.conf.urls import url, include
from .views import features, create_feature

urlpatterns = [
    url(r'^all/$', features, name='features'),
    url(r'^feature-request/$', create_feature, name='create_feature'),
]