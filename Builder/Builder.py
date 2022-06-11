"""

    Creational:
        Builder

"""
from abc import ABC, abstractmethod



# ---------
class Director:
    __biulder = None

    def set_biulder(self, biulder):
        self.__biulder = biulder

    def get_car(self):
        car = Car()
        
        wheel = self.__biulder.get_wheel()
        car.set_wheel(wheel)

        body = self.__biulder.get_body()
        car.set_body(body)

        engine = self.__biulder.get_engine()
        car.set_engine(engine)

        return car
# ---------



# ---------
class Car:
    def __init__(self):
        self.__wheel = None
        self.__body = None
        self.__engine = None

    def set_wheel(self, wheel):
        self.__wheel = wheel
    
    def set_body(self, body):
        self.__body = body
    
    def set_engine(self, engine):
        self.__engine = engine
    
    def detail(self):
        print(f'engine: {self.__engine.hp}')
        print(f'body: {self.__body.shape}')
        print(f'wheel: {self.__wheel.size}')
# ---------



# ---------
class Builder(ABC):
    @abstractmethod
    def get_wheel(self):
        pass
    @abstractmethod
    def get_body(self):
        pass
    @abstractmethod
    def get_engine(self):
        pass


class Benz(Builder):
    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 22
        return wheel

    def get_body(self):
        body = Body()
        body.shape = 'sedan'
        return body

    def get_engine(self):
        engine = Engine()
        engine.hp = 420
        return engine
# ---------



# ---------
class Wheel: size = None
class Body: shape = None
class Engine: hp = None
# ---------



car1 = Benz()
director = Director()
director.set_biulder(car1)
b1 = director.get_car()
b1.detail()