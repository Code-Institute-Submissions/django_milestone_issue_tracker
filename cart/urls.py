from django.conf.urls import url, include
from .views import cart

urlpatterns = [
    url(r'^$', cart, name='cart'),
]