#Author: Jonathan Chen
#Due Date: N/A
#Assignment: This program contains class for storing information aobut each item purchased or returned.

class TransactionItem:
    def __init__(self):
        self.__id = 0
        self.__name = ""
        self.__qty = 0
        self.__price = 0

    #create the get and set methods for ID
    def get_id(self):
        return self.__id
    def set_id(self, value):
        self.__id = value

    #create the get and set methods for name
    def get_name(self):
        return self.__name
    def set_name(self, new_name):
        self.__name = new_name

    #create the get and set methods for quantity
    def get_qty(self):
        return self.__qty
    def set_qty(self, new_qty):
        self.__qty = new_qty

    #create the get and set methods for price
    def get_price(self):
        return self.__price
    def set_price(self, new_price):
        self.__price = new_price

    #calculates the cost
    def calc_cost(self):
        return self.__qty * self.__price

    def __str__(self):
        return f"{self.__id:<8}{self.__name:<30}{self.__qty:<9}${self.__price:<15}${self.calc_cost():,.2f}"

