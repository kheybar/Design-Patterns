"""

    Iterator:
        1-Iterable
        2-Iteration

"""
class Iteration:
    def __init__(self, value):
        self.value = value

    def __next__(self):
        if self.value == 0:
            raise StopIteration('End of Sequence ...')
        for i in range(0, self.value):
            value = self.value
            self.value -= 1

            return value



class Iterator:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return Iteration(self.value)



sequence_1 = Iterator(3)
sequence_1_iter = iter(sequence_1)

print(next(sequence_1_iter))
print(next(sequence_1_iter))
print(next(sequence_1_iter))
print(next(sequence_1_iter))