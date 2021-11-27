"""

    Strategy

"""
from abc import ABC, abstractmethod



class Context:
    def __init__(self, sentence, direction):
        self.sentence = sentence
        self._direction = direction

    @property
    def direction(self):
        self._direction = dir
    
    @direction.setter
    def direction(self, dir):
        self._direction = dir

    def sorting(self):
        return self._direction.direct(self.sentence)



class Direction(ABC):
    @abstractmethod
    def direct(self, data):
        pass


class Right(Direction):
    def direct(self, data):
        print(data[::-1])

class Left(Direction):
    def direct(self, data):
        print(data)



c1 = Context('Hello World ...', Right())
c1.sorting()