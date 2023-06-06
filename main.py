
# Задание 1
# Написать итератор, который принимает список списков,
# и возвращает их плоское представление, т.е последовательность состоящую из вложенных элементов.
# Например
#задание 3. Написать итератор аналогичный итератору из задания 1, но обрабатывающий списки с любым уровнем вложенности



nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, [None, 0, 'bcd']],
]


class FlatIterator:
    def __init__(self, nested_list):  # конструктор принимает два аргумента low и high (помимо self)
        self.flat_list = []
        self.flatten(nested_list)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self, *args):
        if self.index < len(self.flat_list):
            item = self.flat_list[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration

    def flatten(self, nested_list):
        for item in nested_list:
            if isinstance(item, list):
                self.flatten(item)
            else:
                self.flat_list.append(item)


for item in FlatIterator(nested_list):
	print(item) #

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)

#---------------------------------------------

#Задание 2
# Написать генератор, который принимает список списков, и возвращает их плоское представление. Например
#4.* Написать генератор аналогичный генератор из задания 2, но обрабатывающий списки с любым уровнем вложенности

nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, [None, 1, 'abc']],
]

def flat_generator(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            yield from flat_generator(item)
        else:
            yield item

for item in flat_generator(nested_list):
    print(item)

