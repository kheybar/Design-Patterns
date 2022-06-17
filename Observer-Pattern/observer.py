from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self):
        pass


class Subject:
    __observers = []
    def attach(self, observer):
        self.__observers.append(observer)

    def detach(self, observer):
        self.__observers.remove(observer)

    def notify(self, value):
        for observer in self.__observers:
            observer.update(value)
