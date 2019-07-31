from django.conf.urls import url
from .views import bugs, create_bug, bug_detail, upvote_bug

urlpatterns = [
    url(r'^all/$', bugs, name='bugs'),
    url(r'^bug-report/$', create_bug, name='create_bug'),
    url(r'^(?P<pk>\d+)/$', bug_detail, name='bug_detail'),
    url(r'^(?P<pk>\d+)/upvote/$', upvote_bug, name='upvote_bug'),
]
