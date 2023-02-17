price_adjust = 1


class Customer:
    def __init__(self, customerid, Name, address, email, phone, member_status):
        self.customerid = customerid
        self.__Name = Name
        self.__address = address
        self.__email = email
        self.__phone = phone
        self.__member_status = member_status

    def get_customerid(self, customerid):
        self.__customerid = customerid

    def get_MemberStatus(self, member_status):
        self.__member_status = member_status

    def get_phone(slf, phone):
        self.__phone = phone

    def get_Name(self, Name):
        self.__Name = Name


# Transaction class


class Transaction:
    def __init__(self, date, time, item_name, cost, customerid):
        self.__date = date
        self.__time = time
        self.__item_name = item_name
        self.__cost = cost
        self.__customerid = customerid

    def get_item_name(self, item_name):
        self.__ItemName = item_name

    def get_cost(self, cost):
        self.__cost = cost
