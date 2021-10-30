"""

    Creational:
        Factory Method
            3 Components => 1-Creator 2-Product 3-Client
                1-Creator:
                    Identifier

"""



# --------- 1 Esay Example
# class A:
#     def __init__(self, name, format):
#         self.name = name
#         self.format = format



# class B:
#     def edit(self, file):
#         if file.format == 'json':
#             print(f'Editing Json File ... {file.name}')
#         elif file.format == 'xml':
#             print(f'Editing Xml File ... {file.name}')
#         else:
#             raise ValueError('Sorry ...')



# a1 = A(name='first', format='json')

# b1 = B()

# b1.edit(a1)
# ---------



# --------- 2
# class A:
#     def __init__(self, name, format):
#         self.name = name
#         self.format = format



# class B:
#     def edit(self, file): # Client
#         edit = self._get_edit(file)
#         return edit

#     def _get_edit(self, file): # Creator
#         if file.format == 'json': # format => Identifier
#             return self.json_edit(file)
#         elif file.format == 'xml': # format => Identifier
#             return self.xml_edit(file)
#         else:
#             raise ValueError('Sorry ...')


#     def json_edit(self, file): # Product
#         print(f'Editing Json File ... {file.name}')

#     def xml_edit(self, file): # Product
#         print(f'Editing Xml File ... {file.name}')



# a1 = A(name='first', format='json')

# b1 = B()

# b1.edit(a1)
# ---------






# --------- 1 Hard Example
from abc import ABC, abstractmethod



# --- Creator
class Creator(ABC):
    @abstractmethod
    def make(self):
        pass

    def _call_edit(self):
        # product = self.make()
        # result = product.edit()
        # return result
        return self.make().edit()

class JsonCreator(Creator):
    def make(self):
        return Json()

class XmlCreator(Creator):
    def make(self):
        return Xml()




# --- Product
class Product(ABC):
    @abstractmethod
    def edit(self):
        pass


class Json(Product):
    def edit(self):
        return 'Edititng Json File ...'


class Xml(Product):
    def edit(self):
        return 'Edititng Xml File ...'
# ---------


# --- Client
def client(format):
    return format._call_edit()


print(client(JsonCreator()))
