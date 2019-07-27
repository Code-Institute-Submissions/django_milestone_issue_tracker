from django.conf.urls import url, include
from .views import stats, bug_status_stats, feature_status_stats, bugs_vs_features_stats, top_bugs_stats, top_feature_stats

urlpatterns = [
    url(r'^$', stats, name='stats'),
    url(r'^get_bug_stats/$', bug_status_stats, name='bug_status_stats'),
    url(r'^get_feature_stats/$', feature_status_stats, name='feature_status_stats'),
    url(r'^bugs_vs_features_stats/$', bugs_vs_features_stats, name='bugs_vs_features_stats'),
    url(r'^top_bugs_stats/$', top_bugs_stats, name='top_bugs_stats'),
    url(r'^top_feature_stats/$', top_feature_stats, name='top_feature_stats'),
]