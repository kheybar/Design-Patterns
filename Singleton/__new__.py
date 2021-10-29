"""

    __new__

"""

class A:
    def __init__(self, name):
        self.name = name
    
    def __new__(cls, name, *args, **kwargs):
        if name == "Roham":
            return None
        else:
            return super().__new__(cls, *args, **kwargs)



a1 = A('Roham')
print(a1) # output => None