class Restaurant:
    def __init__(self):
        self.menu = dict
        self.customers = customers

    def get_customer_info(self, customerid):
        if customerid in self.customers:
            print(f"Customer Name: {self.customers[customerid][0]}")
            print(f"Phone: {self.customers[customerid][3]}")
        else:
            print("Customer not found!")

    def get_order_total(self, customerid):
        for key, value in self.menu.items():
            if value[3] == int(customerid):
                print(f"Ordered Item: {value[1]}   Price: ${value[2]}")
                self.order_total += value[2]
        print(f"Total Cost: ${self.order_total}")

        if self.customers[customerid][4] == "True":
            discount = self.order_total * 0.2
            print(f"Member Discount: ${discount}")
            print(f"Total Cost after discount: ${self.order_total-discount}")
