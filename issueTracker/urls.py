"""issuetracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from home import urls as urls_home
from accounts import urls as urls_accounts
from bugs import urls as urls_bugs
from features import urls as urls_features
from overview import urls as urls_overview
from cart import urls as urls_cart
from checkout import urls as urls_checkout
from searchbugs import urls as urls_search_bugs
from searchfeatures import urls as urls_search_features
from searchoverview import urls as urls_search_overview
from stats import urls as urls_stats

urlpatterns = [
    url(r'^$', include(urls_home)),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^bugs/', include(urls_bugs)),
    url(r'^features/', include(urls_features)),
    url(r'^overview/', include(urls_overview)),
    url(r'^cart/', include(urls_cart)),
    url(r'^checkout/', include(urls_checkout)),
    url(r'^search/bugs/', include(urls_search_bugs)),
    url(r'^search/features/', include(urls_search_features)),
    url(r'^search/overview/', include(urls_search_overview)),
    url(r'^stats/', include(urls_stats)),
]
