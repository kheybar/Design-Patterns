"""

    Creational:
        Singleton

"""

class Singleton(type):
    _instance = None

    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = super().__call__()

        return self._instance



class Db(metaclass=Singleton):
    pass


d1 = Db()
d2 = Db()



print(d1 is d2) # True
print(d2 == d1) # True

print(id(d1)) # 140236710059648
print(id(d2)) # 140236710059648
