from urllib2 import URLError
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from mailchimp.chimpy.chimpy import ChimpyException
from forms import ChumpSubscribeForm

DONE_URL = getattr(settings, 'CHUMP_DONE_URL', '/chump/done/')
ERROR_URL = getattr(settings, 'CHUMP_ERROR_URL', '/chump/error/')

def subscribe_process(request):
    form = ChumpSubscribeForm(settings.CHUMP_LIST_ID, 
                              data=request.POST or None)
    err_msg = 'Invalid entry'
    if form.is_valid():
        try:
            form.subscribe()
            if request.is_ajax():
                # For ajax, return target URL as plain text
                return HttpResponse(DONE_URL, content_type='text/plain')
            return HttpResponseRedirect(DONE_URL)
        except URLError:
            err_msg = 'Subscription temporarily unavailable'
        except ChimpyException, e:
            # Chimpy library appends too much shit after first colon
            err_msg = unicode(e).split(':')[0]
    if request.is_ajax():
        # For ajax, return error message as plain text
        return HttpResponse(err_msg, status=400, content_type='text/plain')
    return HttpResponseRedirect(ERROR_URL)
