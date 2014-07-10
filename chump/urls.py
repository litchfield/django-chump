from django.conf import settings
from django.conf.urls import *
from django.views.generic import TemplateView

urlpatterns = []

urlpatterns += patterns('',
    url(r'^$', 'chump.views.subscribe_process', name='chump_process'),
    url(r'^(.+)/$', 'chump.views.subscribe_process', name='chump_process'),
)
