class Error(Exception):
    def __init__(self, message):
        self.message = message

class ParameterError(Error):
    pass

class MessageError(Error):
    pass