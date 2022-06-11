"""
    
    __call__

"""


class A:
    def __call__(self, name, *args, **kwargs):
        print('Call Method ...', name)


a1 = A()
a1('Mahdi')