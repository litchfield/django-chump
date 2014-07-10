from django.conf import settings
from django.conf.urls import *
from django.views.generic import TemplateView
from chump import get_template_names

urlpatterns = []

urlpatterns += patterns('',
    url(r'^$', 'chump.views.subscribe_process', name='chump_process'),
    url(r'^list/(.+)/$', 'chump.views.subscribe_process', name='chump_process'),
    url(r'^done/', TemplateView.as_view(template_name=get_template_names('chump_done.html')), name='chump_done'),
    url(r'^error/', TemplateView.as_view(template_name=get_template_names('chump_error.html')), name='chump_error'),
)
