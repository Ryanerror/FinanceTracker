
import sqlite3
import tkinter
from tkinter import messagebox
import math

class Manager:
    __slots__ = ["__My_Money_Percent", "__Food_Percent", "__Investments_Percent", "__Car_Parts_Percent", "__Coffee_Percent", "__Fun_Percent", "__Disney_Percent"]
    
    def __init__(self, my_money, food, investments, car_parts, coffee, fun, disney):
        self.__My_Money_Percent = my_money
        self.__Food_Percent = food
        self.__Investments_Percent = investments
        self.__Car_Parts_Percent = car_parts
        self.__Coffee_Percent = coffee
        self.__Fun_Percent = fun 
        self.__Disney_Percent = disney
      
        # add seter methods for these
    
    
    def connect_to_database(self):
        connection = sqlite3.connect("Wallet.db")
        cursor = connection.cursor()
        
        return connection, cursor
    
    def make_data_table(self):
        # alraedy ran this method dont neeed to run it ever again
        connection, cursor = self.connect_to_database()
        cursor.execute(""" CREATE TABLE wallet (
                        Food REAL,
                        Investments REAL,
                        My_Money REAL,
                        Car_Parts REAL,
                        Coffee REAL,
                        Fun REAL,
                        Disney REAL
                    )""")
        
        connection.commit()
        connection.close()
      
    def add_row(self):
        connection, cursor = self.connect_to_database()
        cursor.execute("INSERT INTO wallet VALUES (0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00)")
        connection.commit()
        connection.close()
    
    def update_Food(self, number):
        connection, cursor = self.connect_to_database()
        cursor.execute("UPDATE wallet SET Food = " + str(number))
        connection.commit()
        connection.close()
    
    def get_Food(self):
        connection, cursor = self.connect_to_database()
        cursor.execute("SELECT Food FROM wallet")
        Food = str(cursor.fetchall()) 
        Food = Food.replace(")", "")
        Food = Food.replace("(", "")
        Food = Food.replace(",", "")
        Food = Food.replace("[", "")
        Food = Food.replace("]", "")
        
        connection.commit()
        connection.close()
        
        return float(Food)
        
    
    def update_Investments(self, number):
        connection, cursor = self.connect_to_database()
        cursor.execute("UPDATE wallet SET Investments = " + str(number))
        connection.commit()
        connection.close()
    
    def get_Investments(self):
        connection, cursor = self.connect_to_database()
        cursor.execute("SELECT Investments FROM wallet")
        Investments = str(cursor.fetchall())
        Investments = Investments.replace(")", "")
        Investments = Investments.replace("(", "")
        Investments = Investments.replace(",", "")
        Investments = Investments.replace("[", "")
        Investments = Investments.replace("]", "")
            
        connection.commit()
        connection.close()
        
        return float(Investments)
        
    
    def update_My_Money(self, number):
        connection, cursor = self.connect_to_database()
        cursor.execute("UPDATE wallet SET My_Money = " + str(number))
        connection.commit()
        connection.close()
    
    def get_My_Money(self):
        connection, cursor = self.connect_to_database()
        cursor.execute("SELECT My_Money FROM wallet")
        My_Money = str(cursor.fetchall())
        My_Money = My_Money.replace(")", "")
        My_Money = My_Money.replace("(", "")
        My_Money = My_Money.replace(",", "")
        My_Money = My_Money.replace("[", "")
        My_Money = My_Money.replace("]", "")
        
        connection.commit()
        connection.close()
        
        return float(My_Money)
        
    def update_Car_Parts(self, number):
        connection, cursor = self.connect_to_database()
        cursor.execute("UPDATE wallet SET Car_Parts = " + str(number))
        connection.commit()
        connection.close()
        
    def get_Car_Parts(self):
        connection, cursor = self.connect_to_database()
        cursor.execute("SELECT Car_Parts FROM wallet")
        Car_Parts = str(cursor.fetchall())
        Car_Parts = Car_Parts.replace(")", "")
        Car_Parts = Car_Parts.replace("(", "")
        Car_Parts = Car_Parts.replace(",", "")
        Car_Parts = Car_Parts.replace("[", "")
        Car_Parts = Car_Parts.replace("]", "")
        
        connection.commit()
        connection.close()
        
        return float(Car_Parts)
        
    
    def update_Coffee(self, number):
        connection, cursor = self.connect_to_database()
        cursor.execute("UPDATE wallet SET Coffee = " + str(number))
        connection.commit()
        connection.close()
        
    def get_Coffee(self):
        connection, cursor = self.connect_to_database()
        cursor.execute("SELECT Coffee FROM wallet")
        Coffee = str(cursor.fetchall())
        
        Coffee = Coffee.replace(")", "")
        Coffee = Coffee.replace("(", "")
        Coffee = Coffee.replace(",", "")
        Coffee = Coffee.replace("[", "")
        Coffee = Coffee.replace("]", "")
        
        connection.commit()
        connection.close()
        
        return float(Coffee)
        
    
    def update_Fun(self, number):
        connection, cursor = self.connect_to_database()
        cursor.execute("UPDATE wallet SET Fun = " + str(number))
        connection.commit()
        connection.close()
    
    def get_Fun(self):
        connection, cursor = self.connect_to_database()
        cursor.execute("SELECT Fun FROM wallet")
        Fun = str(cursor.fetchall())
        
        Fun = Fun.replace(")", "")
        Fun = Fun.replace("(", "")
        Fun = Fun.replace(",", "")
        Fun = Fun.replace("[", "")
        Fun = Fun.replace("]", "")
        
        connection.commit()
        connection.close()
        
        return float(Fun)
        
    
    def update_Disney(self, number):
        connection, cursor = self.connect_to_database()
        cursor.execute("UPDATE wallet SET Disney = " + str(number))
        connection.commit()
        connection.close()

    def get_Disney(self):
        connection, cursor = self.connect_to_database()
        cursor.execute("SELECT Disney FROM wallet")
        Disney = str(cursor.fetchall())
        
        Disney = Disney.replace(")", "")
        Disney = Disney.replace("(", "")
        Disney = Disney.replace(",", "")
        Disney = Disney.replace("[", "")
        Disney = Disney.replace("]", "")
        
        connection.commit()
        connection.close()
        
        return float(Disney)
        
    
    def print_table(self):
        return "Food : " + str(self.get_Food())  + "\n" \
            + "Investments : " + str(self.get_Investments()) + "\n" \
                +  "My_Money : "  + str(self.get_My_Money()) + "\n" \
                    + "Car_Parts : " + str(self.get_Car_Parts()) + "\n" \
                        +  "Coffee : " + str(self.get_Coffee()) + "\n" \
                            +  "Fun : " + str(self.get_Fun()) + "\n" \
                                +  "Disney : " + str(self.get_Disney())      
        
    
     
    
    def filter(self):
        
        Aprroved_Transactions = set() 
        Coffee_key_words = set(["CAFE", "STARBUCKS", "COFFEE"]) 
        with open("csv/SavingAccData.csv") as file:
            next(file)
            next(file)
            next(file)
            next(file)
            next(file)
            # ryan fix this later this is dumb 
            next(file)
            next(file)
            next(file)
            for line in file:
                line = line.split(",")
                
                price = line[2]
                price = price.replace('"', "")
                
                if "-" in price:
                    if price == '-25.00':
                        self.update_Fun(self.get_Fun() - 25.00)
                    else:
                        if messagebox.askyesno("There was a charge for " + price + " Was this for car stuff "):
                            
                            self.update_Car_Parts(self.get_Car_Parts() - abs(float(price)))
                        else:
                            self.update_My_Money(self.get_My_Money() - abs(float(price)))
                else:
                    continue
                
        with open("csv/CheckingAccData.csv") as file:
            next(file)
            next(file)
            next(file)
            next(file)
            # ryan fix this later this is dumb
            next(file)
            next(file)
            next(file)
            next(file)
            for line in file:
                line = line.split(",")
                price = line[2]
                price = price.replace('"', "")
                
                if "-" in price:
                    if price in Aprroved_Transactions:
                        continue
                    elif price == "-25.00" :
                        continue
                    elif "SMOKE" in line[1]:
                        self.update_Fun(self.get_Fun() - (abs(float(price)) * self.__Fun_Percent)) 
                    else:
                        coffee = False
                        
                        for keyword in Coffee_key_words:
                            if keyword in line[1]:
                                coffee = True
                                break
                        
                        if coffee:
                            self.update_Coffee(self.get_Coffee() - abs(float(price)))
                        else:
                            self.update_Food(self.get_Food() - abs(float(price))) 
                        
                else:
                    if "Online Banking transfer from CHK 6015" in line[1]:
                        Aprroved_Transactions.add(price)
                        
                    elif "FARQUHARSON" in line[1] or "VICTOR" in line[1] or "VICTORIA" in line[1]:
                        self.update_My_Money(self.get_My_Money() + abs(float(price)))
                        
                    else: 
                        income = abs(float(price))
                        self.update_My_Money(self.get_My_Money() + (income * self.__My_Money_Percent))
                        self.update_Food(self.get_Food() + (income * self.__Food_Percent))
                        self.update_Fun(self.get_Fun() + (income * self.__Fun_Percent)) 
                        self.update_Car_Parts(self.get_Car_Parts() + (income * self.__Car_Parts_Percent))
                        self.update_Coffee(self.get_Coffee() + (income * self.__Coffee_Percent))
                        self.update_Investments(self.get_Investments() + (income * self.__Investments_Percent))
                        
                        if self.get_Disney() >= 11.00:
                            self.update_My_Money(self.get_My_Money() + (income * self.__Disney_Percent))
                        else: 
                            self.update_Disney(self.get_Disney() + (income * self.__Disney_Percent))  
                                
                            
                
            
           
def main():
    manager = Manager(0.14, 0.35, 0.20, 0.14, 0.07, 0.09, 0.01)
    manager.update_Car_Parts(0.00)
    manager.update_Coffee(0.00)
    manager.update_My_Money(0.00)
    manager.update_Fun(0.00)
    manager.update_Food(0.00)
    manager.update_Investments(0.00)
    manager.update_Disney(0.00)
    manager.filter()
    
    print(manager.print_table())
    
    
    
if __name__ == "__main__":
    main()