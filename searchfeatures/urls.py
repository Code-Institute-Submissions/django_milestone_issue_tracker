from django.conf.urls import url
from .views import do_search_features

urlpatterns = [
    url(r'^$', do_search_features, name='search_features')
]
