class WebDavException(Exception):
    pass


class NotValid(WebDavException):
    pass


class OptionNotValid(NotValid):
    def __init__(self, name, value, ns=''):
        self.name = name
        self.value = value
        self.ns = ns

    def __str__(self):
        return 'Option ({}{}={}) have invalid name or value'.format(self.ns,self.name,self.value)


class CertificateNotValid(NotValid):
    pass


class NotFound(WebDavException):
    pass


class LocalResourceNotFound(NotFound):
    def __init__(self, path):
        self.path = path

    def __str__(self):
        return 'Local file: {} not found'.format(self.path)


class RemoteResourceNotFound(NotFound):
    def __init__(self, path):
        self.path = path

    def __str__(self):
        return 'Remote resource: {} not found'.format(self.path)


class RemoteParentNotFound(NotFound):
    def __init__(self, path):
        self.path = path

    def __str__(self):
        return 'Remote parent for: {} not found'.format(self.path)


class ResourceTooBig(WebDavException):
    def __init__(self, path, size, max_size):
        self.path = path
        self.size = size
        self.max_size = max_size

    def __str__(self):
        return 'Resource {} is too big, it should be less then {} but actually: {}'.format(self.path, self.max_size, self.size)


class MethodNotSupported(WebDavException):
    def __init__(self, name, server):
        self.name = name
        self.server = server

    def __str__(self):
        return 'Method {} not supported for {}'.format(self.name, self.server)


class ConnectionException(WebDavException):
    def __init__(self, exception):
        self.exception = exception

    def __str__(self):
        return self.exception.__str__()


class NoConnection(WebDavException):
    def __init__(self, hostname):
        self.hostname = hostname

    def __str__(self):
        return 'No connection with {}'.format(self.hostname)


# This exception left only for supporting original library interface.
class NotConnection(WebDavException):
    def __init__(self, hostname):
        self.hostname = hostname

    def __str__(self):
        return 'No connection with {}'.format(self.hostname)


class ResponseErrorCode(WebDavException):
    def __init__(self, url, code, message):
        self.url = url
        self.code = code
        self.message = message

    def __str__(self):
        return 'Request to {} failed with code {} and message: {}'.format(self.url, self.code, self.message)


class ServerException(WebDavException):
    def __init__(self, url, code, message):
        self.url = url
        self.code = code
        self.message = message

    def __str__(self):
        return 'WebDAV server failed to process request to {} failed with code {} and message: {}'.format(self.url, self.code, self.message)


class NotEnoughSpace(WebDavException):
    def __init__(self):
        pass

    def __str__(self):
        return 'Not enough space on the server'
