from django.conf.urls import url, include
from .views import bugs, create_bug

urlpatterns = [
    url(r'^all/$', bugs, name='bugs'),
    url(r'^bug-report/$', create_bug, name='create_bug'),
]