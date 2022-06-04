# Name: Ashlee Tan
# Admin No: 211362G
# Tutorial Group: IT2101

class Booking:
    def __init__(self, package_name: str, customer_name: str, no_of_pax: int,
                 cost_per_pax: float):
        self.package_name = package_name
        self.customer_name = customer_name
        self.no_of_pax = no_of_pax
        self.cost_per_pax = cost_per_pax

    def __str__(self):
        return ("%s, %s, %d pax, $%.2f"
                % (self.package_name, self.customer_name, self.no_of_pax,
                   self.cost_per_pax))
