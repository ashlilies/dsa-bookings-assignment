# Name: Ashlee Tan
# Admin No: 211362G
# Tutorial Group: IT2101

import unittest
from Services.SortService import SortService

_svc = SortService.get_instance()


class SwapTestCase(unittest.TestCase):
    def test_swap(self):
        # given
        data = [3, 5, 6]
        first_idx = 1
        second_idx = 2
        expected = [3, 6, 5]

        # when
        _svc.swap_indices(data, first_idx, second_idx)

        # then
        self.assertEqual(expected, data)


class MoveToIdxTestCase(unittest.TestCase):
    def test_move(self):
        # given
        data = [1, 2, 3, 4, 5, 6]
        from_idx = 5
        to_idx = 0
        expected = [6, 1, 2, 3, 4, 5]

        # when
        _svc.move_to_idx(data, to_idx, from_idx)


class BubbleSortTestCase(unittest.TestCase):
    def test_bubble_sort(self):
        # Given
        data = [5, 4, 3, 2, 1, 0, -1]
        expected = [-1, 0, 1, 2, 3, 4, 5]

        # When
        _svc.bubble_sort(data, lambda x: x)

        # Then
        self.assertEqual(expected, data)  # add assertion here


class SelectionSortTestCase(unittest.TestCase):
    def test_selection_sort(self):
        # Given
        data = [5, 4, 3, 2, 1, 0, -1]
        expected = [-1, 0, 1, 2, 3, 4, 5]

        # When
        _svc.selection_sort(data, lambda x: x)

        # Then
        self.assertEqual(expected, data)  # add assertion here


class InsertionSortTestCase(unittest.TestCase):
    def test_insertion_sort(self):
        # Given
        data = [5, 4, 3, 2, 1, 0, -1]
        expected = [-1, 0, 1, 2, 3, 4, 5]

        # When
        _svc.insertion_sort(data, lambda x: x)

        # Then
        self.assertEqual(expected, data)  # add assertion here

    def test_insertion_sort_2(self):
        # Given
        data = [4, 3, 2, 10, 12, 1, 5, 6]
        expected = [1, 2, 3, 4, 5, 6, 10, 12]

        # When
        _svc.insertion_sort(data, lambda x: x)

        # Then
        self.assertEqual(expected, data)  # add assertion here


if __name__ == '__main__':
    unittest.main()
