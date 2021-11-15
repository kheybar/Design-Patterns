"""

    *args, **kwargs

"""

def show_args(*args):
    print(args)


show_args('Mahdi', 'Rose')



def show_kwargs(**kwargs):
    print(kwargs)


show_kwargs(name='Mahdi', age=17)