# Name: Ashlee Tan
# Admin No: 211362G
# Tutorial Group: IT2101

# Provides a variety of static methods allowing for advanced search and sort
# Included algorithms: comb sort, heap sort, counting sort, jump search
import math


class AdvancedService:
    # Swap two indices in a list
    @staticmethod
    def _swap_indices(objs: list, first_idx: int, second_idx: int):
        tmp = objs[first_idx]
        objs[first_idx] = objs[second_idx]
        objs[second_idx] = tmp

    # Comb sort
    @staticmethod
    def _comb_sort_get_next_gap(gap):
        gap = (gap * 10) // 13  # shrink by shrink factor
        if gap < 1:
            return 1
        return gap

    @classmethod
    def comb_sort(cls, obj_list: list, key: callable):
        n = len(obj_list)
        gap = n
        swapped = True  # first run
        while gap > 1 or swapped:
            gap = cls._comb_sort_get_next_gap(gap)
            swapped = False  # checking
            for i in range(0, n - gap):
                if key(obj_list[i]) > key(obj_list[i + gap]):
                    cls._swap_indices(obj_list, i, i + gap)
                    swapped = True

    # Heapify a sub-tree rooted at index i
    # n is the size of the heap
    @staticmethod
    def _heapify(objs: list, key: callable, n, i):
        largest = i  # initializing largest idx as root
        l = 2 * i + 1
        r = 2 * i + 2

        # L child of root exists, greater than root?
        if l < n and key(objs[largest]) < key(objs[l]):
            largest = l

        # R child of root exists & greater than root?
        if r < n and key(objs[largest]) < key(objs[r]):
            largest = r

        # Changing root if necessary
        if largest != i:
            AdvancedService._swap_indices(objs, i, largest)
            # Recursively heapify the new root
            AdvancedService._heapify(objs, key, n, largest)

    @staticmethod
    def heap_sort(obj_list: list, key: callable):
        n = len(obj_list)

        # Build maxheap by rearranging the list in-place
        for i in range(n // 2 - 1, -1, -1):
            AdvancedService._heapify(obj_list, key, n, i)

        # Extract elements
        for i in range(n - 1, 0, -1):
            AdvancedService._swap_indices(obj_list, 0, i)
            AdvancedService._heapify(obj_list, key, i, 0)

    # Counting sort
    # An integer sorting algorithm that is not in-place
    @staticmethod
    def count_sort(obj_list: list, min_int, max_int, key: callable):
        def _ckey(n):
            return n - min_int

        k = max_int - min_int  # number of distinct keys

        count = [0 for x in range(k+1)]
        output = [None for x in range(len(obj_list))]

        for i in range(0, len(obj_list)):
            j = _ckey(key(obj_list[i]))
            count[j] += 1

        for i in range(1, k+1):
            count[i] += count[i-1]

        for i in range(len(obj_list) - 1, 0-1, -1):
            j = _ckey(key(obj_list[i]))
            count[j] -= 1
            output[count[j]] = obj_list[i]

        return output

    # Search algorithms
    # Jump search - O(sqrt(n)) time
    # Prerequisite: sorted array like binary search
    @staticmethod
    def jump_multi_search(sorted_data_list: list, key: callable, value):
        res = []
        n = len(sorted_data_list)
        step = math.sqrt(n)  # block size to be jumped

        # find block where element is present, if it is
        prev = 0
        while key(sorted_data_list[int(min(step, n) - 1)]) < value:
            prev = step
            step += math.sqrt(n)
            if prev >= n:
                return res

        # linear search in block beginning with prev
        while key(sorted_data_list[int(prev)]) < value:
            prev += 1
            if prev == min(step, n):  # reached next block or end of array,
                return res  # meaning element is not present

        # if it is found
        if key(sorted_data_list[int(prev)]) == value:
            res.append(sorted_data_list[int(prev)])
            # check right and left
            i = int(prev) + 1
            while i < n:
                if key(sorted_data_list[i]) == value:
                    res.append(sorted_data_list[i])
                    i += 1
                else:
                    break

            i = int(prev) - 1
            while i >= 0:
                if key(sorted_data_list[i]) == value:
                    res.append(sorted_data_list[i])
                    i -= 1
                else:
                    break

        return res
