"""

    Proxy

"""


class DataBase:
    def work(self):
        print('you are admin so you can work with database ...')



class Proxy:
    __password = 'secret'
    def check_admin(self, password):
        if password == self.__password:
            admin = DataBase()
            admin.work()
        else:
            print('you are not admin so you can not work with database ...')



mahdi = Proxy()
mahdi.check_admin('secret')