"""

    Creational:
        Prototype

"""


from copy import deepcopy



class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color



class Prototype:
    def __init__(self):
        self._object = {}

    def register(self, name, obj):
        """
            name of object and object
        """
        self._object[name] = obj

    
    def unregister(self, name):
        """
            for delete object
        """
        del self._object[name]

    
    def clone(self, name, **kwargs):
        # clone_obj for get copy
        clone_obj = deepcopy(self._object.get(name))

        # edit property in object
        clone_obj.__dict__.update(kwargs)

        return clone_obj





benz = Car('Cls', 'red')


pro1 = Prototype()
pro1.register('benz-cls', benz)
pro1_copy = pro1.clone('benz-cls', color='yellow')


print(pro1_copy.__dict__)


print(benz.name is pro1_copy.name) # True