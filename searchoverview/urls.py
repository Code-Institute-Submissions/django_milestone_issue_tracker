from django.conf.urls import url
from .views import do_search_overview

urlpatterns = [
    url(r'^$', do_search_overview, name='search_overview')
]
