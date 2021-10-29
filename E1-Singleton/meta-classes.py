"""

    meta classes

"""

# --- 1
class A:
    def __new__(cls, *args, **kwargs):
        print(cls)


a1 = A() # <class '__main__.A'>
# ---


# --- 2
class B:
    pass

b1 = B()
print(b1.__class__.__class__) # <class 'type'>
# ---


# --- 3

# print(help(type))
# output:
    # type(object_or_name, bases, dict)
    # type(object) -> the object's type
    # type(name, bases, dict) -> a new type

C = type('C', (), {})
print(C) # <class '__main__.C'>
# ---


# --- 4
class D(type):
    _instance = None
    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = super().__call__()
        return self._instance


class E(metaclass=D):
    pass

e1 = E()
e2 = E()

print(id(e1)) # 140337585923984
print(id(e2)) # 140337585923984
