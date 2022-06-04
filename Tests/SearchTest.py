# Name: Ashlee Tan
# Admin No: 211362G
# Tutorial Group: IT2101

import unittest
from Services.SearchService import SearchService

_svc = SearchService.get_instance()


# Example object used for the following test cases
class Example:
    def __init__(self, a, b):
        self.a = a
        self.b = b


class LinearSearchObjectList(unittest.TestCase):
    def test_basic(self):
        # Given
        list_of_obj = list()
        obj = Example("Fox", 20)

        list_of_obj.append(Example("The", 5))
        list_of_obj.append(Example("Quick", 10))
        list_of_obj.append(Example("Brown", "sss"))
        list_of_obj.append(obj)

        search = "Fox"
        expected = obj

        # When
        actual = _svc.linear_search(list_of_obj, lambda x: x.a.lower(),
                                    search.lower())

        # Then
        self.assertEqual(expected, actual)


class BinarySearchNumberList(unittest.TestCase):
    def test_number(self):
        # Given
        nums = [1, 2, 3, 5, 7, 11]
        search = 3
        expected = search

        # When
        actual = _svc.binary_search(nums, lambda x : x, search)

        # Then
        self.assertEqual(expected, actual)


class BinarySearchObjectList(unittest.TestCase):
    def test_basic(self):
        # Given
        list_of_obj = list()
        obj = Example("E", 1)

        list_of_obj.append(Example("A", 1))
        list_of_obj.append(Example("B", 1))
        list_of_obj.append(Example("C", 1))
        list_of_obj.append(Example("D", 1))
        list_of_obj.append(obj)

        search = "e"
        expected = obj

        # When
        actual = _svc.binary_search(list_of_obj, lambda x : x.a.lower(),
                                    search.lower())

        # Then
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
