import logging
from .models import RequestLog, RequestCounter

logger = logging.getLogger(__name__)


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
        elif path in ['/requests', '/requests/']:
            try:
                RequestCounter.objects.get(id=1).reset()
            except:
                logger.info("Problem with RequestCounter")
        else:
            try:
                RequestCounter.objects.get(id=1).increment()
            except:
                logger.info("Problem with RequestCounter")

        self.arg['FULL_PATH'] = path
        for field in self.META_FIELDS:
            if field in request.META:
                self.arg[field] = request.META[field]
        logger.info(str(self.arg))
        RequestLog().save(self.arg)


def requestsLogger(request):
    """
    logger for viewvs
    """

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

    logger = logging.getLogger(__name__)
    path = request.get_full_path()

    arg['FULL_PATH'] = path

    for field in META_FIELDS:
        if field in request.META:
            arg[field] = request.META[field]
    logger.info(str(arg))
