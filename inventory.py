#Author: Jonathan Chen
#Due Date: N/A
#Assignment: This program contains class for storing inventory information


class inventory:
    def __init__(self, new_id, new_name, new_stock, new_price):
        self.__id = new_id
        self.__name = new_name
        self.__stock = new_stock
        self.__price = new_price

    #create the get and set methods for ID
    def get_id(self):
        return self.__id

    #create the get and set methods for name
    def get_name(self):
        return self.__name

    #create the get and set methods for stock
    def get_stock(self):
        return self.__stock

    #create the get and set methods for price
    def get_price(self):
        return self.__price

    #this "restock" method manipulate the attribute of the inventory class
    def restock(self, new_stock):
        if new_stock > 0:
            self.__stock += new_stock
            return True
        else:
            return False

    #this "purchase" method manipulate the attribute of the inventory classs
    def purchase(self, purch_qty):
        if self.__stock >= purch_qty:
            self.__stock -= purch_qty
            return True
        else:
            return False

    #this method print the attributes of the class
    def __str__(self):
        return f"{self.__id:<8}{self.__name:<30}${self.__price:.2f}\t{self.__stock:>15}"





    
    
    

    
        

    
