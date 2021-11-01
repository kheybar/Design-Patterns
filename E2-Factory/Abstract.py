"""

    Abstract Class, Abstract Methods

"""

from abc import ABC, abstractmethod



class A(ABC):
    @abstractmethod
    def show(self):
        print('5his method from abstractmethod ...')


class B(A):
    def show(self):
        super().show()
        print('OverRide abstractmethod from B')

b1 = B()
b1.show()



# --------- with out abstract

class C:
    def show(self):
        raise NotImplementedError


class D(C):
    def show(self):
        print('OverRide abstractmethod from D')

d1 = D()
d1.show()


