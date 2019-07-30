from django.conf.urls import url, include
from . import urls_reset
from .views import index, register, logout, login, profile, update_profile

urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^password-reset/', include(urls_reset)),
    url(r'^profile/$', profile, name='profile'),
    url(r'^profile/update/$', update_profile, name='update_profile'),
]
