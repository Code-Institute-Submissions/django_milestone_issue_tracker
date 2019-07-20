
from django.conf.urls import url
from .views import do_search_bugs

urlpatterns = [
    url(r'^$', do_search_bugs, name='search_bugs')
]