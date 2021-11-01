"""

    Abstract Factory
        Car => Benz, Bmw => Suv, Coupe
			benz suv => gla
			bmw suv => x1
			benz coupe => cls
			bmw coupe => m2

"""



from abc import ABC, abstractmethod


# ---------- Creator
# Car
class Car(ABC):
    @abstractmethod
    def call_suv(self):
        pass

    @abstractmethod
    def call_coupe(self):
        pass



# Benz, Bmw
class Benz(Car):
    def call_suv(self):
        return Gla()

    def call_coupe(self):
        return Cls()



class Bmw(Car):
    def call_suv(self):
        return X1()
    
    def call_coupe(self):
        return M2()
# ---------- 



# ---------- Product
# Benz
class Gla(Benz):
    def creating_suv(self):
        print('this is benz suv: GLA')


class Cls(Benz):
    def creating_coupe(self):
        print('this is benz coupe: CLS')



# Bmw
class X1(Bmw):
    def creating_suv(self):
        print('this is bmw suv: X1')


class M2(Bmw):
    def creating_coupe(self):
        print('this is bmw coupe: M2')
# ----------



# ---------- Client
def client_suv(order):
    suv = order.call_suv()
    suv.creating_suv()


def client_coupe(order):
    coupe = order.call_coupe()
    coupe.creating_coupe()
# ----------