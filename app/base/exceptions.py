

class ServerError(Exception):
    pass

class ServerMisConfigured(ServerError):
    pass

class InternalServerError(ServerError):
    pass


class ClientError(Exception):
    pass


class ClientMethodNotAllowed(ClientError):
    pass