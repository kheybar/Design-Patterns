from observer import (
    Subject,
    Observer,
)


class Sheet(Observer):
    def __init__(self, q):
        self.q = q

    def update(self, value):
        print(f'Sheet Updated. {value}')


class Chart(Observer):
    def update(self, value):
        print(f'Chart Updated. {value}')


class DataSource(Subject):
    __value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value
        self.notify(value)
        return self.__value


ds = DataSource()

sheet = Sheet('q')
chart = Chart()

ds.attach(sheet)
ds.attach(chart)

ds.value = 2
