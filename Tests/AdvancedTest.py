import unittest

from Services.AdvancedService import AdvancedService

_svc = AdvancedService


class CombSortTestCase(unittest.TestCase):
    def test_comb_sort(self):
        # Given
        data = [5, 4, 3, 2, 1, 0, -1]
        expected = [-1, 0, 1, 2, 3, 4, 5]

        # When
        _svc.comb_sort(data, lambda x: x)

        # Then
        self.assertEqual(expected, data)  # add assertion here


class HeapSortTestCase(unittest.TestCase):
    def test_heap_sort(self):
        # Given
        data = [5, 4, 3, 2, 1, 0, -1]
        expected = [-1, 0, 1, 2, 3, 4, 5]

        # When
        _svc.heap_sort(data, lambda x: x)

        # Then
        self.assertEqual(expected, data)  # add assertion here


class JumpSearchObjectList(unittest.TestCase):
    def test_basic(self):
        # Example object used for the following test cases
        class Example:
            def __init__(self, a, b):
                self.a = a
                self.b = b

        # Given
        list_of_obj = list()
        obj1 = Example("A", 1)
        obj2 = Example("B", 2)
        obj3 = Example("C", 2)
        obj4 = Example("D", 1)
        obj5 = Example("E", 1)
        obj6 = 6
        obj7 = 6
        obj8 = 11
        obj9 = 12

        list_of_obj.append(obj6)
        list_of_obj.append(obj7)
        list_of_obj.append(obj8)
        list_of_obj.append(obj9)

        search = 11
        expected = [11]

        # When
        actual = _svc.jump_multi_search(list_of_obj, lambda x: x, search)

        # Then
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
