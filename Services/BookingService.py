# Name: Ashlee Tan
# Admin No: 211362G
# Tutorial Group: IT2101

from Models.Booking import Booking
from Models.LinkedListNode import LinkedListNode
from Services.AdvancedService import AdvancedService
from Services.SearchService import SearchService
from Services.SortService import SortService


# This singleton service offers a get_instance() method to get an instance.
# Data can be accessed with the instance.data property (read-only)
class BookingService:
    __instance = None

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = BookingService()
        return cls.__instance

    # Do not call; for internal use only
    def __init__(self):
        if self.__class__.__instance is not None:
            Exception("Can't create a singleton - use get_instance()")

        # TODO: 10 records - implement BST
        self.__data = list()
        self.__search_svc = SearchService.get_instance()
        self.__sort_svc = SortService.get_instance()
        self.initialize_data()

    # Create pre-initialized data
    def initialize_data(self):
        bookings = [Booking("Sentosa Family Package", "Simon Yee", 3, 500),
                    Booking("Marina Sands Package", "Lee Chit Boon", 2, 235),
                    Booking("Shangri-La Package", "Novita Kho", 5, 340),
                    Booking("NYP Overnight Staycay", "Leow Zhen Zhen", 1, 20),
                    Booking("Hotel 81", "Roy Ng", 3, 50),
                    Booking("Marriott Hotel", "Bobby Liu", 3, 550),
                    Booking("Grand Park Package", "Chan Yuen Loong", 8, 999),
                    Booking("Plaza Hotels", "Leung Sai Cheong", 4, 1239),
                    Booking("At-Home Package", "Gabriel Choo", 5, 10),
                    Booking("Underwater Package", "Tan Ai Lian", 3, 100)]
        self.__data += bookings

    @property
    def data(self):
        return self.__data

    # Sorting methods - all lowercase to prevent bugs with searching
    # Bubble sort
    def sort_customer_name(self):
        self.__sort_svc.bubble_sort(self.__data, lambda x: x.customer_name.lower())

    # Selection sort
    def sort_package_name(self):
        self.__sort_svc.selection_sort(self.__data, lambda x: x.package_name.lower())

    # Insertion sort
    def sort_package_cost(self):
        self.__sort_svc.insertion_sort(self.__data, lambda x: x.cost_per_pax.lower())

    # Searching methods - returns editable object reference or null
    # Ignore case sensitivity
    # Linear search - return object reference or null
    # def search_customer_name(self, name: str):
    #     return self.__search_svc.linear_search(self.__data,
    #                                            lambda
    #                                                x: x.customer_name.lower(),
    #                                            name.lower())

    # Multi-search variant of the above
    def search_multi_customer_name(self, name: str):
        return self.__search_svc.linear_search_multi(self.__data,
                                                     lambda
                                                         x: x.customer_name.lower(),
                                                     name.lower())

    # Binary search - return object reference or null
    # Sorts by package name first, to enable binary search.
    # def search_package_name(self, name: str):
    #     self.sort_package_name()
    #     return self.__search_svc.binary_search(self.__data,
    #                                            lambda x: x.package_name.lower(),
    #                                            name.lower())

    # Multi-search variant of the above
    def search_multi_package_name(self, name: str):
        self.sort_package_name()
        return self.__search_svc.binary_search_multi(self.__data,
                                                     lambda
                                                         x: x.package_name.lower(),
                                                     name.lower())

    # Get all records within a specified price range per pax, inclusive
    # Sorts by prices first, as it uses a linked list.
    # Can handle same start and end.
    # Returns result as a regular python list.
    def search_price_range(self, start: float, end: float) -> list:
        key = lambda x: x.cost_per_pax

        if start > end:
            tmp = start
            start = end
            end = tmp

        self.sort_package_cost()
        first_node = LinkedListNode.construct_linked_list(self.__data)
        start_node = first_node

        while start_node != None:
            if key(start_node.data) >= start:
                break
            start_node = start_node.next

        end_node = start_node
        while end_node.next != None:
            if key(end_node.data) <= end and key(end_node.next.data) > end:
                break
            end_node = end_node.next

        res = []
        if start_node == None:  # nothing found
            return res

        while 1:
            res.append(start_node.data)
            if start_node == end_node:
                break
            start_node = start_node.next

        return res

    # Methods starting with 'adv' are for advanced features
    def adv_sort_package_pax_comb_sort(self):
        AdvancedService.comb_sort(self.__data, key=lambda x: x.no_of_pax)

    def adv_sort_customer_name_heap_sort(self):
        AdvancedService.heap_sort(self.__data, key=lambda x: x.customer_name)

    def adv_search_package_name_jump_search_multi(self, package_name: str):
        self.sort_package_name()
        return AdvancedService.jump_multi_search(self.__data,
                                                 key=lambda x: x.package_name,
                                                 value=package_name)
