from django.conf.urls import url, include
from .views import profile, update_profile

urlpatterns = [
    url(r'^$', profile, name='profile'),
    url(r'^update/$', update_profile, name='update_profile'),
]