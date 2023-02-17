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

Customer = fc.Customer

print(f"Customer Name: {customers[customerid][0]}")
print(f"Phone: {customers[customerid][3]}")


for key in dict:
    if dict[key][3] == int(customerid):
        print(f"Ordered Item: {dict[key][1]}   Price: ${dict[key][2]}")

for key, value in dict.items():
    if value[3] == int(customerid):
        order_total += value[2]

print(f"Total Cost: ${order_total}")

if customers[customerid][4] == "True":
    discount = order_total * 0.2
    print(f"Member Discount: ${discount}")
    print(f"Total Cost after discount: ${order_total-discount}")
