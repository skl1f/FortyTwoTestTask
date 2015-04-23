from .models import RequestLog, RequestCounter


def return_on_failure(value):
    def decorate(f):
        def applicator(*args, **kwargs):
            try:
                f(*args, **kwargs)
            except:
                print('Error')

        return applicator


class RequestLoggingMiddleware(object):
    META_FIELDS = [
        'REQUEST_METHOD',
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

        for field in self.META_FIELDS:
            if field in request.META:
                self.arg[field] = request.META[field]
        RequestLog().save(self.arg)
        RequestCounter.objects.get(id=1).increment()
