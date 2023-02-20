import FoodClass as fc

# this dictionary represents transactions. The key of the dictionary is the transaction identifier.
# The Value of the dictionary is a list. The elements in each list are -
# ['Date', 'Name of item', 'Cost', 'customerid' ]

dict = {
    "trans1": ["2/15/2023", "The Lone Patty", 17, 569],
    "trans2": ["2/15/2023", "The Octobreakfast", 18, 569],
    "trans3": ["2/15/2023", "The Octoveg", 16, 570],
    "trans4": ["2/15/2023", "The Octoburger", 20, 570],
}

order_total = 0

customers = {
    "570": [
        "Danni Sellyar",
        "97 Mitchell Way Hewitt Texas 76712",
        "dsellyarft@gmpg.org",
        "254-555-9362",
        "False",
    ],
    "569": [
        "Aubree Himsworth",
        "1172 Moulton Hill Waco Texas 76710",
        "ahimsworthfs@list-manage.com",
        "254-555-2273",
        "True",
    ],
}

customerid = input("Enter a customer ID: ")

restaurant = fc.Restaurant()

customerid = input("Enter a customer ID: ")
fc.restaurant.get_customer_info(customerid)
fc.restaurant.get_order_total(customerid)
