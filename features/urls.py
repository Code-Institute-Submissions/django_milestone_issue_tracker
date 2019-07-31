from django.conf.urls import url
from .views import features, create_feature, feature_detail, upvote_feature

urlpatterns = [
    url(r'^all/$', features, name='features'),
    url(r'^feature-request/$', create_feature, name='create_feature'),
    url(r'^(?P<pk>\d+)/$', feature_detail, name='feature_detail'),
    url(r'^(?P<pk>\d+)/upvote/$', upvote_feature, name='upvote_feature'),
]
