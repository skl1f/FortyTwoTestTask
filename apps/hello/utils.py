import logging
from .models import RequestLog, RequestCounter
from django.conf import settings


logger = logging.getLogger(__name__)


def write_logline(request, content):
    META_FIELDS = ['REQUEST_METHOD',
                   'REMOTE_ADDR',
                   'HTTP_USER_AGENT',
                   'HTTP_REFERER',
                   'HTTP_ACCEPT_LANGUAGE']
    message = []
    message.append("Full path: {0}".format(request.build_absolute_uri()))

    for field in META_FIELDS:
        if field in request.META:
            message.append("{0}: {1}; ".format(field, request.META[field]))
    logger.info(''.join(message))

    if settings.DEBUG is True:
        message.append("DATA: ")
        for data in content:
            message.append(str(content[data]))
        logger.debug(''.join(message))


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
        path = request.get_full_path()

        if path in ['/api/requests', '/api/requests/']:
            return None
        elif path in ['/request', '/requests/']:
            RequestCounter.objects.get(id=1).reset()
        else:
            RequestCounter.objects.get(id=1).increment()

        self.arg['FULL_PATH'] = path
        for field in self.META_FIELDS:
            if field in request.META:
                self.arg[field] = request.META[field]
        RequestLog().save(self.arg)
