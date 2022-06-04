# Name: Ashlee Tan
# Admin No: 211362G
# Tutorial Group: IT2101

# Singleton - do not call constructor directly.
class SearchService:
    __instance = None

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = SearchService()
        return cls.__instance

    # Pass a list of objects in, specify a key lambda function
    # that returns a parameter, returns the found object or None.
    def linear_search(self, data_list: list, key: callable, value):
        for i in range(len(data_list)):
            if key(data_list[i]) == value:
                return data_list[i]
        return None

    def linear_search_multi(self, data_list: list, key: callable, value):
        res = []
        for i in range(len(data_list)):
            if key(data_list[i]) == value:
                res.append(data_list[i])
        return res

    # List passed in must be sorted by given key,
    # and have no duplicates of such value.
    # Returns object if found, or None.
    def binary_search(self, sorted_data_list: list, key: callable, value):
        l = 0
        h = len(sorted_data_list) - 1

        while l <= h:
            mid = int((h - l) / 2) + l

            if key(sorted_data_list[mid]) == value:
                return sorted_data_list[mid]
            elif key(sorted_data_list[mid]) < value:
                l = mid + 1
            else:
                h = mid - 1

        return None

    # Multi-search variant of the above
    def binary_search_multi(self, sorted_data_list: list, key: callable, value):
        res = []
        l = 0
        h = len(sorted_data_list) - 1

        while l <= h:
            mid = int((h - l) / 2) + l

            if key(sorted_data_list[mid]) == value:
                res.append(sorted_data_list[mid])
                # Check left and right
                i = mid + 1
                while i < len(sorted_data_list):
                    if key(sorted_data_list[i]) == value:
                        res.append(sorted_data_list[i])
                        i += 1
                    else:
                        break

                i = mid - 1
                while i >= 0:
                    if key(sorted_data_list[i]) == value:
                        res.append(sorted_data_list[i])
                        i -= 1
                    else:
                        break
                return res

            elif key(sorted_data_list[mid]) < value:
                l = mid + 1
            else:
                h = mid - 1

        return res
