# Name: Ashlee Tan
# Admin No: 211362G
# Tutorial Group: IT2101

from Models import Booking
from Services.AdvancedService import AdvancedService
from Services.BookingService import BookingService

_svc = BookingService.get_instance()


# These variables set the min and max pax count inclusive
MIN_PAX_COUNT = 1
MAX_PAX_COUNT = 9

# Main view
# TAL: Can add additional fields, or reuse same fields for advanced features.
#      Additional features must not be covered in the module;
#      NOT Merge Sort etc. No bonus marks for that.
# DONE: Search returns duplicate vals and allows selecting intended record
#      Additional featuers are algorithm-centered; things like pretty display
#      and DB does not count.
#     Interview is a verbal interview; 'Challenge: Can you change your code?'
#     'OK no problem! Fang ma guo lai! Do do do' => more marks
#     'I very scared to change my code' => less marks
#     You can just don't do, but you may not fare that well.
#     Demonstrate advanced algorithsm actual running time
def main():
    running = True

    print("Welcome to Staycation Package Deals Inventory")
    while running:
        display_menu()
        user_input = input("Enter choice: ")
        if user_input == "0":
            running = False
        elif user_input == "1":
            Routines.display_all_records()
        elif user_input == "2":
            Routines.sort_customer_name()
            Routines.previous_sort_order = Routines.sort_customer_name
        elif user_input == "3":
            Routines.sort_package_name()
            Routines.previous_sort_order = Routines.sort_package_name
        elif user_input == "4":
            Routines.sort_package_cost()
            Routines.previous_sort_order = Routines.sort_package_cost
        elif user_input == "5":
            # Routines.linear_search_cust_and_update()
            Routines.linear_search_multi_cust_and_update()
        elif user_input == "6":
            # Routines.binary_search_package_and_update()
            Routines.binary_search_multi_package_and_update()
        elif user_input == "7":
            Routines.search_price_range()
        elif user_input == "8":
            # TODO
            # print("Coming soon")
            AdvancedRoutines.main_view()
        else:
            print("Invalid input. Please try again?")

    print("Exiting...")


def display_menu():
    print('*' * 70)
    print("1. Display all records")
    print("2. Sort record by Customer Name using Bubble sort")
    print("3. Sort record by Package Name using Selection sort")
    print("4. Sort record by Package Cost using Insertion sort")
    print("5. Search record by Customer Name using Linear Search "
          "and update record")
    print("6. Search record by Package Name using Binary Search "
          "and update record")
    print("7. List records range from $X to $Y. e.g $100-200")
    print("8. Open bonus features menu")
    print("0. Exit Application")


class Routines:
    previous_sort_order = None  # for reverting upon binary search

    @staticmethod
    def display_all_records():
        print('=' * 70)
        print("Format: package_name, customer_name, no_of_pax, cost_per_pax")
        for i in range(len(_svc.data)):
            obj = _svc.data[i]
            print("%d. %s" % (i + 1, obj))

    @staticmethod
    def display_selected_records(records: list):
        print('=' * 70)
        print("Format: package_name, customer_name, no_of_pax, cost_per_pax")
        for i in range(len(records)):
            obj = records[i]
            print("%d. %s" % (i + 1, obj))

    @staticmethod
    def sort_customer_name():
        _svc.sort_customer_name()
        print("Done sorting by Customer Name using Bubble Sort")

    @staticmethod
    def sort_package_name():
        _svc.sort_package_name()
        print("Done sorting by Package Name using Selection Sort")

    @staticmethod
    def sort_package_cost():
        _svc.sort_package_cost()
        print("Done sorting by Package Cost using Insertion Sort")

    # @staticmethod
    # def linear_search_cust_and_update():
    #     search = input("Enter exact customer name (case-insensitive): ")
    #     obj = _svc.search_customer_name(search)
    #
    #     if obj is None:
    #         print("No matching booking found.")
    #         return
    #
    #     print("Found booking: %s" % obj)
    #     Routines.update_booking(obj)

    @staticmethod
    def linear_search_multi_cust_and_update():
        search = input("Enter exact customer name (case-insensitive): ")
        res = _svc.search_multi_customer_name(search)

        if len(res) == 0:
            print("No matching booking found.")
            return

        Routines.multi_select(res)

    # To be called internally - select an option to update from search results
    # then update it.
    # Assumption: results list has at least 1 item.
    # If there is 1 item, we don't offer a selection.
    @staticmethod
    def multi_select(res: list):
        if len(res) == 1:
            print("Found booking: %s" % res[0])
            Routines.update_booking(res[0])
            return

        print("Found bookings:")
        for i in range(len(res)):
            print("%d. %s" % (i + 1, res[i]))

        while 1:
            try:
                id = int(input("Select booking to update (-1 to cancel): "))
                if id == -1:
                    return
                elif not id >= 1:
                    print("You have not entered a valid ID. Try again?")
                    continue
                obj = res[id-1]
                if obj is None:
                    print("Booking does not exist. Try again?")
                    continue
                break
            except:
                print("You have not entered a valid ID. Try again?")

        Routines.update_booking(obj)


    # @classmethod
    # def binary_search_package_and_update(cls):
    #     search = input("Enter exact package name (case-insensitive): ")
    #
    #     print("Sorting by package name and binary searching for %s..." % search)
    #     obj = _svc.search_package_name(search)
    #
    #     if cls.previous_sort_order is not None:
    #         print("Reverting to previously saved sorting order...")
    #         cls.previous_sort_order()
    #
    #     if obj is None:
    #         print("No matching booking record found.")
    #         return
    #
    #     print("Found booking: %s" % obj)
    #     Routines.update_booking(obj)

    @classmethod
    def binary_search_multi_package_and_update(cls):
        search = input("Enter exact package name (case-insensitive): ")

        print("Sorting by package name and binary searching for %s..." % search)
        res = _svc.search_multi_package_name(search)

        if cls.previous_sort_order is not None:
            print("Reverting to previously saved sorting order...")
            cls.previous_sort_order()

        if len(res) == 0:
            print("No matching booking found.")
            return

        Routines.multi_select(res)

    # TODO: Check if package name already exists - update method in service?
    @staticmethod
    def update_booking(booking: Booking):
        booking.package_name = input("Enter new package name: ")
        while 1:
            name = input("Enter new customer name: ")
            if name.isalpha():
                booking.customer_name = name
                break
            print("Customer name must be alphabetical and not contain numbers!")

        while 1:
            try:
                n = input("Enter no. of pax (%d-%d): " % (MIN_PAX_COUNT, MAX_PAX_COUNT))
                n = int(n)
                if n < MIN_PAX_COUNT:
                    print("No. of pax must be at least %d!" % MIN_PAX_COUNT)
                    continue
                if n > MAX_PAX_COUNT:
                    print("Maximum of %d pax allowed!" % MAX_PAX_COUNT)
                    continue
                booking.no_of_pax = n
                break
            except Exception as e:
                print("Please enter a valid integer.")

        while 1:
            try:
                price = input("Enter package cost per pax: $")
                price = float(price)
                if price <= 0:
                    print("Please enter a valid positive price!")
                    continue
                booking.cost_per_pax = price
                break
            except Exception as e:
                print("Please enter a valid price.")

        print("Successfully updated package")

    @classmethod
    def search_price_range(cls):
        lower = None
        upper = None

        while 1:
            try:
                lower = input("Enter $X: ")
                lower = float(lower)
                break
            except Exception as e:
                print("Enter a valid price!")

        while 1:
            try:
                upper = input("Enter $Y: ")
                upper = float(upper)
                break
            except Exception as e:
                print("Enter a valid price!")

        print("Sorting by package cost to search price range...")
        res = _svc.search_price_range(lower, upper)

        if cls.previous_sort_order is not None:
            print("Reverting to previously saved sorting order...")
            cls.previous_sort_order()

        print("Found records (sorted by price):")
        cls.display_selected_records(res)


class AdvancedRoutines:
    options = None

    # Load all options to a dict
    # Format: key - menu entry, val[0] - label, val[1] - function pointer
    @classmethod
    def load_options(cls):
        cls.options = dict()
        cls.options["1"] = ("Display all records", cls.display_all_records)
        cls.options["2"] = ("Sort record by Package Cost using Comb Sort",
                            cls.sort_package_cost_comb_sort)
        cls.options["3"] = ("Sort record by Customer Name using Heap Sort",
                            cls.sort_customer_name_heap_sort)
        cls.options["4"] = ("Sort record by Package Pax using Counting Sort",
                            cls.sort_package_pax_count_sort)
        cls.options["5"] = ("Search record by Package Name using Jump Search "
                            "and update record",
                            cls.search_package_name_jump_search_multi)

    @classmethod
    def main_view(cls):
        if AdvancedRoutines.options is None:
            cls.load_options()
        while True:
            cls.print_menu()
            cmd = input("Enter option: ")
            if cmd == "0":
                return
            opt = cls.options.get(cmd)
            if opt:
                opt[1]()
            else:
                print("Invalid option! Try again?")

    @classmethod
    def print_menu(cls):
        print('*' * 70)
        print("ADVANCED FEATURE MENU")
        print('=' * 70)
        for key in cls.options:
            print("%s. %s" % (key, (cls.options[key])[0]))
        print("0. Exit Advanced Menu")

    @staticmethod
    def display_all_records():  # pass through
        Routines.display_all_records()

    @staticmethod
    def sort_package_cost_comb_sort():
        _svc.adv_sort_package_cost_comb_sort()
        Routines.previous_sort_order = AdvancedRoutines.sort_package_cost_comb_sort
        print("Done sorting by Package Cost using Comb Sort")

    @staticmethod
    def sort_customer_name_heap_sort():
        _svc.adv_sort_customer_name_heap_sort()
        Routines.previous_sort_order = AdvancedRoutines.sort_customer_name_heap_sort
        print("Done sorting by Customer Name using Heap Sort")

    @staticmethod
    def sort_package_pax_count_sort():
        _svc.adv_sort_package_pax_count_sort(MIN_PAX_COUNT, MAX_PAX_COUNT)
        Routines.previous_sort_order = AdvancedRoutines.sort_package_pax_count_sort
        print("Done sorting by Package Pax using Counting Sort")

    @staticmethod
    def search_package_name_jump_search_multi():
        search = input("Enter exact package name (case-insensitive): ")

        print("Sorting by package name and jump searching for %s..." % search)
        res = _svc.search_multi_package_name(search)

        if Routines.previous_sort_order is not None:
            print("Reverting to previously saved sorting order...")
            Routines.previous_sort_order()

        if len(res) == 0:
            print("No matching booking found.")
            return

        Routines.multi_select(res)


if __name__ == "__main__":
    main()
