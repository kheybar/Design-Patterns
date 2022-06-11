"""

    Guido van Rossum:
        First-Class Everything.
            One of my goals for Python was to make it so that all objects were "first class."        
            By this, I meant that I wanted all objects that could be named in the language (
            e.g., integers, strings, functions, classes, modules, methods, etc.) to have equal status.
            That is, they can be assigned to variables, placed in lists, stored in dictionaries, passed as arguments, and so forth.

"""

# -------
# Everything is Class
# import datetime

# def test():
#     pass

# print(type('string')) # <class 'str'>
# print(type(14)) # <class 'int'>
# print(type(['hello', 'world'])) # <class 'list'>
# print(type(True)) # <class 'bool'>
# print(type(datetime)) # <class 'module'>
# print(type(test)) # <class 'function'>
# print(type(type)) # <class 'type'>
# print(type(print)) # <class 'builtin_function_or_method'>
# -------






# ------------------- Function is Object

"""

    1. function are object
    2. function can be stored in data structure
    3. function can be passed to other functions (higher-order functions)
    4. function can be nested (inner and outer functions)
    5. function can capture local state (lexical closure)
    6. object can behave like functions

"""


# ------- 1
# def show(name):
#     return f'hello {name}'

# variable = show
# del show # variable is a pointer to show
# print(variable('Mahdi')) # worked!
# print(show('Boss')) # NameError: name 'show' is not defined

# -------



# ------- 2
# def show(name):
    # return f'hello {name.upper()}'

# name = [show, str.capitalize, str.lower]

# print(name[2]('MAHDI')) # mahdi

# for i in name:
#     print(i)
#     print(i('Mahdi ZaRePour'))
    # <function show at 0x7f42414a05e0>  # hello MAHDI ZAREPOUR

    # <method 'capitalize' of 'str' objects> # Mahdi zarepour

    # <method 'lower' of 'str' objects> # mahdi zarepour

# -------



# ------- 3
# def show(name):
#     return f'hello {name.capitalize()}'

# def sender(func, name):
#     return func(name)

# print(sender(show, 'mahdi'))

# for i in map(show, ['Hamid', 'rose']): # map is builtin higher order function
#     print(i)

# -------



# ------- 4
# def show(name):
#     def say_hello(first_name):
#         return f'Hello {first_name.capitalize()}'
    
#     return say_hello(name)

# print(show('mahdi'))


# --- B
# def person(age):

#     def adult(name): return f'{name} is adult.'

#     def kid(name): return f'{name} is kid.'
    
#     if age > 18: return adult
#     else: return kid

# rose = person(17)
# print(rose) # <function person.<locals>.kid at 0x7f819b71a700>
# print(rose('Rose'))

# -------



# ------- 5
# def person(age, name):

#     def adult(): return f'{name} is adult.'

#     def kid(): return f'{name} is kid.'
    
#     if age > 18: return adult
#     else: return kid


# print(person(24, 'Hamid')) # <function person.<locals>.adult at 0x7f8aa3e7e670>
# print(person(24, 'Hamid')()) # Hamid is adult. we callable adult function with use ()

# -------



# ------- 6
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def __call__(self, *args, **kwargs):
#         print(f'{self.name} is {self.age} years old.')


# mahdi = Person('Mahdi', 17)

# mahdi() 
# without __call__ => TypeError: 'Person' object is not callable
# with __call__ => Mahdi is 17 years old.

# -------