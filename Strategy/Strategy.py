from abc import ABC, abstractmethod


class Compressor(ABC):
    """Interface"""
    @abstractmethod
    def algorithm(self):
        pass


class Filter(ABC):
    """Interface"""
    @abstractmethod
    def type(self):
        pass


class RAWCompressor(Compressor):
    """Concrete Compressor"""
    def algorithm(self):
        return 'RAW compression'


class JPGCompressor(Compressor):
    """Concrete Compressor"""
    def algorithm(self):
        return 'JPG compression'


class WBFilter(Filter):
    """Concrete Filter"""
    def type(self):
        return 'W&B filter'


class HighContrastFilter(Filter):
    """Concrete Filter"""
    def type(self):
        return 'High Contrast filter'


class ImageStore:
    def __init__(self, filename, compressor:Compressor, filter:Filter):
        self.filename = filename
        self.compressor = compressor
        self.filter = filter

    def store(self):
        return f'{self.filename}-{self.compressor().algorithm()}-{self.filter().type()}'



a = ImageStore('test', JPGCompressor, HighContrastFilter)
result = a.store()
print(result)
