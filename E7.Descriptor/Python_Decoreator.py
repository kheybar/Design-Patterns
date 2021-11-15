"""

    Python Decorator:
        1. Creating Decorator
        2. Applying Multiple Decorators to a Single Function
        3. Acceptin Arguments in Decorator Function
        4. Defining General Purpose Decorators


"""


# ------- 1
# def upper(function):
#     def upper_case():
#         input_func = function()
#         text = input_func.upper()
#         return text
#     return upper_case



# @upper
# def show():
#     return 'hello world ...'


# print(show())
# -------



# ------- 2
# def upper_decorator(function):
#     def upper_case():
#         input_func = function()
#         text = input_func.upper()
#         return text
#     return upper_case



# def split_decorator(function):
#     def split_text():
#         input_func = function()
#         split = input_func.split(' ')
#         return split
#     return split_text



# @split_decorator
# @upper_decorator
# def show():
#     return 'hello world ...'


# print(show())
# -------



# ------- 3
# def upper_decorator(function):
#     def upper_case(first_name, last_name):
#         input_func = function(first_name, last_name)
#         text = input_func.upper()
#         return text
#     return upper_case



# @upper_decorator
# def show_full_name(first_name, last_name):
#     return f'hello{first_name} {last_name}'


# print(show_full_name('mahdi', 'zarepour'))
# -------



# ------- 4
# def upper_decorator(function):
#     def upper_case(first_name, last_name, *args, **kwargs):
#         input_func = function(first_name, last_name)
#         text = input_func.upper()
#         return text
#     return upper_case



# @upper_decorator
# def show_full_name(first_name, last_name):
#     return f'hello{first_name} {last_name}'


# print(show_full_name('mahdi', 'zarepour'))
# -------



# ------- 5 Master!
# def upper(name, age):
#     print(name, age)
#     def upper_decorator(function):
#         def upper_case(first_name, last_name):
#             input_func = function(first_name, last_name)
#             text = input_func.upper()
#             return text
#         return upper_case
#     return upper_decorator



# @upper('BOSS', 17)
# def show_full_name(first_name, last_name):
#     return f'hello {first_name} {last_name}'


# print(show_full_name('mahdi', 'zarepour'))
# -------



# ------- 6
import functools

def upper(name, age):
    print(name, age)
    def upper_decorator(function):

        @functools.wraps(function) # Use Evry Time
        def upper_case(first_name, last_name):
            'change to upper case'
            input_func = function(first_name, last_name)
            text = input_func.upper()
            return text
        return upper_case

    return upper_decorator



@upper('BOSS', 17)
def show_full_name(first_name, last_name):
    'show full name'
    return f'hello {first_name} {last_name}'


print(show_full_name.__name__)
print(show_full_name.__doc__)
# -------