from .models import RequestLog, RequestCounter


class RequestLoggingMiddleware(object):

    def process_request(self, request):
        """
        Saving some of fields from HttpRequest.
        """
        count = RequestCounter.objects.get(id=1)
        log = RequestLog()
        log.full_path = request.get_full_path()
        log.request_method = request.META['REQUEST_METHOD']
        log.remote_addr = request.META['REMOTE_ADDR']
        log.http_user_agent = request.META['HTTP_USER_AGENT']
        try:
            log.http_referer = request.META['HTTP_REFERER']
        except:
            pass
        log.http_accept_language = request.META['HTTP_ACCEPT_LANGUAGE']
        log.save()
        count.increment()
