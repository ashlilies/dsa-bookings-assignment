import unittest
from Models.LinkedListNode import LinkedListNode


class ListToLinkedListTestCase(unittest.TestCase):
    def test_construct_linked_list(self):
        # given
        objs = [3, 6, 9, 12]
        expected = 3 + 6 + 9 + 12

        # when
        ll = LinkedListNode.construct_linked_list(objs)
        actual = 0
        while ll is not None:
            actual += ll.data
            ll = ll.next

        # then
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
