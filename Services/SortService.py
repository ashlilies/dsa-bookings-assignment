class SortService:
    __instance = None

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = SortService()
        return cls.__instance

    def __init__(self):
        if self.__class__.__instance is not None:
            Exception("Can't create a singleton - use get_instance()")

    # Swap two indices in a list in-place, nothing too interesting
    # (Can't use simple swapping as not necessarily mutable references)
    def swap_indices(self, objs: list, first_idx: int, second_idx: int):
        tmp = objs[first_idx]
        objs[first_idx] = objs[second_idx]
        objs[second_idx] = tmp

    # # Move an object in a list from a position to another, like a card stack
    # def move_to_idx(self, objs: list, from_idx: int, to_idx: int):
    #     tmp = objs[from_idx]
    #     objs.pop(from_idx)
    #     objs.insert(to_idx, tmp)

    # Sorts an object list in-place, using key lambda function
    # to determine sort order.
    def bubble_sort(self, obj_list, key: callable) -> None:
        for i in range(len(obj_list) - 1, 0, -1):  # max no of passes: n-1
            is_sorted = True
            for j in range(i):  # one pass
                if key(obj_list[j]) > key(obj_list[j + 1]):  # swap
                    is_sorted = False
                    self.swap_indices(obj_list, j, j + 1)

            if is_sorted:
                return

    # Sorts an object list in-place, using key lambda function
    # to determine sort order.
    def selection_sort(self, obj_list, key: callable) -> None:
        for i in range(len(obj_list) - 1):  # first idx of unsorted subarr
            min_idx = i
            for j in range(i + 1, len(obj_list)):
                if key(obj_list[j]) < key(obj_list[min_idx]):
                    min_idx = j

            self.swap_indices(obj_list, i, min_idx)

    # Sorts an object list in-place, using key lambda function
    # to determine sort order.
    # def insertion_sort(self, obj_list, key: callable) -> None:
    #     for i in range(1, len(obj_list), 1):
    #         move_to_zero = True
    #         for j in range(i - 1, 0 - 1, -1):  # compare backwards until 0 or
    #             if key(obj_list[i]) > key(obj_list[j]):  # key > predecessor
    #                 self.move_to_idx(obj_list, i, j + 1)
    #                 move_to_zero = False
    #                 break
    #         if move_to_zero:
    #             self.move_to_idx(obj_list, i, 0)

    # Re-implementation of insertion sort
    # Sorts an object list in-place, using key lambda function
    # to determine sort order.
    def insertion_sort(self, obj_list: list, key: callable) -> None:
        n = len(obj_list)
        for i in range(1, n, 1):
            tmp = obj_list[i]
            j = i - 1
            while j >= 0 and key(obj_list[j]) > key(tmp):
                obj_list[j+1] = obj_list[j]
                j -= 1
            obj_list[j+1] = tmp
