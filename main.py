class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.current_list = None
        self.current_index = 0

    def __iter__(self):
        self.current_list = self.list_of_list
        self.current_index = 0
        return self

    def __next__(self):
        while self.current_list:
            try:
                item = self.current_list[self.current_index]
                self.current_index += 1
                if isinstance(item, list):
                    self.current_list = item
                    self.current_index = 0
                    continue
                return item
            except IndexError:
                self.current_list = self.list_of_list[self.current_index]
                self.current_index += 1
                if self.current_list is None:
                    raise StopIteration

import types

def flat_generator(list_of_lists):
    for sublist in list_of_lists:
        if isinstance(sublist, list):
            yield from flat_generator(sublist)
        else:
            yield sublist

def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_generator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_generator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)

if __name__ == '__main__':
    test_2()

class FlatIterator:

    def __init__(self, list_of_list):
        self.stack = list(reversed(list_of_list))

    def __iter__(self):
        return self

    def __next__(self):
        while self.stack:
            current = self.stack.pop()
            if isinstance(current, list):
                self.stack.extend(reversed(current))
            else:
                return current
        raise StopIteration

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

import types

def flat_generator(list_of_list):
    for sublist in list_of_list:
        if isinstance(sublist, list):
            yield from flat_generator(sublist)
        else:
            yield sublist

def test_4():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_generator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_generator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)

if __name__ == '__main__':
    test_4()