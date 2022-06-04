# Name: Ashlee Tan
# Admin No: 211362G
# Tutorial Group: IT2101

# One node of a linked list. Save the starting node yourself.
class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    # Construct a linked list from a regular Python list
    @classmethod
    def construct_linked_list(cls, objs: list):
        if len(objs) == 0:  # blank list, return None
            return None

        first_node = None
        prev_node = None
        for obj in objs:
            ll = LinkedListNode(obj)
            if first_node is None:
                first_node = ll
            if prev_node is not None:
                prev_node.next = ll
            prev_node = ll

        return first_node
