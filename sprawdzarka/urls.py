from django.conf.urls.defaults import *
from SQLArena.sprawdzarka.views import news

urlpatterns = patterns('',
	url(r'^$',news),
)