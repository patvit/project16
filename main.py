
# Задание 1
#Доработать класс FlatIterator в коде ниже. Должен получиться итератор, который принимает список списков и возвращает их плоское представление, т. е. последовательность, состоящую из вложенных элементов. Функция test в коде ниже также должна отработать без ошибок.
#задание 3. Необязательное задание. Написать итератор, аналогичный итератору из задания 1, но обрабатывающий списки с любым уровнем вложенности. Шаблон и тест в коде ниже:




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

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()

def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()



#---------------------------------------------

#Задание 2
# Доработать функцию flat_generator. Должен получиться генератор, который принимает список списков и возвращает их плоское представление. Функция test в коде ниже также должна отработать без ошибок.
#4.* 4.* Необязательное задание. Написать генератор, аналогичный генератору из задания 2, но обрабатывающий списки с любым уровнем вложенности. Шаблон и тест в коде ниже:

import types

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

def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)

def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)



if __name__ == '__main__':
    test_2()
if __name__ == '__main__':
    test_4()


