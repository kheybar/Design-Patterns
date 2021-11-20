"""

    Facade

"""


class Raw:
    def raw(self):
        print('Buying raw foods from market ...')


class Transfer:
    def transfer(self):
        print('Transfring raw to kithchen ...')


class Cook:
    def cook(self):
        print('Cooking raw food by chief ...')


class Serve:
    def serve(self):
        print('Serving food to client.')


    
class ItalianRestaurant:
    def get(self):
        raw = Raw()
        raw.raw()

        transfer = Transfer()
        transfer.transfer()

        cook = Cook()
        cook.cook()

        serve = Serve()
        serve.serve()


client = ItalianRestaurant()
client.get()