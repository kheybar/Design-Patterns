"""

    Behavioral:
        Chain of Responsibility

"""
from abc import ABC, abstractmethod



class AbstractHandler(ABC):
    def __init__(self, successor):
        self.successor = successor

    def handle(self, request):
        handle = self.process_request(request)
        if not handle:
            self.successor.handle(request)

    @abstractmethod
    def process_request(self, request):
        pass



class HandlerOne(AbstractHandler):
    def process_request(self, request):
        if 0 < request <= 10:
            print(f'hendler One is Processing this request ... {request}')
            return True



class HandlerTwo(AbstractHandler):
    def process_request(self, request):
        if 10 < request <= 20:
            print(f'hendler Two is Processing this request ... {request}')
            return True



class HandlerDefault(AbstractHandler):
    def process_request(self, request):
        print(f'hendler Default is Processing this request ... {request}')
        return True



class Client:
    def __init__(self):
        self.handler = HandlerOne(HandlerTwo(HandlerDefault(None)))

    def delegate(self, requests):
        for request in requests:
            self.handler.handle(request)

numbers = Client()
numbers.delegate([2, 12, 58, 4])