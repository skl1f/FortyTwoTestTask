from .models import RequestLog, RequestCounter


class RequestLoggingMiddleware(object):
    META_FIELDS = ['REQUEST_METHOD',
                   'REMOTE_ADDR',
                   'HTTP_USER_AGENT',
                   'HTTP_REFERER',
                   'HTTP_ACCEPT_LANGUAGE']

    arg = {'FULL_PATH': '',
           'REQUEST_METHOD': '',
           'REMOTE_ADDR': '',
           'HTTP_USER_AGENT': '',
           'HTTP_REFERER': '',
           'HTTP_ACCEPT_LANGUAGE': ''}

    def process_request(self, request):
        """
        Saving some of fields from HttpRequest.
        """
        self.arg['FULL_PATH'] = request.get_full_path()
        path = request.get_full_path()

        if '/api/requests/' in path:
            return None
        elif path in ['/request', '/requests/']:
            RequestCounter.objects.get(id=1).reset()
        else:
            RequestCounter.objects.get(id=1).increment()

        for field in self.META_FIELDS:
            if field in request.META:
                self.arg[field] = request.META[field]
        RequestLog().save(self.arg)
