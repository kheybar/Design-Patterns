from abc import ABC, abstractmethod


class House(ABC):
    @abstractmethod
    def building_structure(self):
        pass

    @abstractmethod
    def wall(self):
        pass

    def balcony(self):
        pass

    @abstractmethod
    def window(self):
        pass



class WoodenHouse(House):
    def building_structure(self):
        return 'Wooden'

    def wall(self):
        return 'four walls for the wooden house'

    def window(self):
        return 'two windows for the wooden house'


class StoneHouse(House):
    def building_structure(self):
        return 'Stone'

    def wall(self):
        return 'eight walls for the stone house'

    def window(self):
        return 'three windows for the stone house' 


class BrickHouse(House):
    def building_structure(self):
        return 'Brick'

    def wall(self):
        return 'four walls for the brick house'
    
    def balcony(self):
        return 'one balcony for the brick house'

    def window(self):
        return 'one window for the brick house' 
