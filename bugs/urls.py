from django.conf.urls import url, include
from .views import bugs

urlpatterns = [
    url(r'^all/$', bugs, name='bugs'),
]