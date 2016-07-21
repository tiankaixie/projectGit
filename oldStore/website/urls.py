from django.conf.urls import url, patterns
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
	url(r'^index/$', views.index, name='index'),
	url(r'^historyList/$', views.historyList, name = 'historyList'),
	url(r'^particularHistory/(?P<history_id>[0-9]+)$', views.particularHistory, name = 'particularHistory'),
	url(r'^particularPeriod/(?P<period_id>[0-9]+)$', views.particularPeriod, name = 'particularPeriod'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)