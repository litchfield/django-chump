from django.conf import settings
from django.conf.urls import *

urlpatterns = []

urlpatterns += patterns('',
    url(r'^$', 'chump.views.subscribe_process', name='chump_process'),
    url(r'^list/(.+)/$', 'chump.views.subscribe_process', name='chump_process'),
    url(r'^done/', 'chump.views.subscribe_done', name='chump_done'),
    url(r'^error/', 'chump.views.subscribe_error', name='chump_error'),
)
