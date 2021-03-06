

# Итератор для удаления дубликатов
from gen_random import gen_random


class Unique:
    """Итератор, оставляющий только уникальные значения."""

    def __init__(self, data, **kwargs):
        self.used_elements = set()
        self.data = iter(data)
        self.ignore_case = False
        if 'ignore_case' in kwargs.keys():
            self.ignore_case = kwargs['ignore_case']

    def __iter__(self):
        return self

    def __next__(self):
        #если нет аргументов, чтобы не выдавал ошибку
        while True:
            #try:
            current = next(self.data)
            #except StopIteration:
                #raise StopIteration
            #чтобы не выводило одинаковые значения
            if self.ignore_case:
                if current.upper() not in self.used_elements:
                    # Добавление в множество производится
                    # с помощью метода add
                    self.used_elements.add(current.upper())
                    return current
            else:
                if current not in self.used_elements:
                    # Добавление в множество производится
                    # с помощью метода add
                    self.used_elements.add(current)
                    return current




def uniqueSort(arr):
    tmp = []
    for i in Unique(arr, ignore_case=True):
        tmp.append(i)
    return sorted(tmp)

if __name__ == '__main__':
    for i in Unique(["abc", "dsada", "dSada", "abc"]):
        print(i, end=" ")
    print()
    for i in Unique(["abc", "dsada", "dSada", "abc"], ignore_case=True):
        print(i, end=" ")
    print()
    for i in Unique(gen_random(7, 1, 3)):
        print(i, end=" ")
    print()
    for i in Unique([1, 6, 4, 3, 6, 4, 3, 2, 76, 3, 23, 4]):
        print(i, end=" ")
    print()