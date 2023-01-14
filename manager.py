
import sqlite3
import tkinter
from tkinter import messagebox
import csv

class Manager:
    __slots__ = ["__My_Money_Percent", "__Food_Percent", "__Investments_Percent", "__Car_Parts_Percent", "__Coffee_Percent", "__Fun_Percent", "__Disney_Percent"]
    
    def __init__(self):
        self.__My_Money_Percent = 0.14    
        self.__Food_Percent = 0.35
        self.__Investments_Percent = 0.20
        self.__Car_Parts_Percent = 0.14
        self.__Coffee_Percent = 0.07
        self.__Fun_Percent = 0.09
        self.__Disney_Percent = 0.01
      
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
        return "Food : " + str(round(self.get_Food(), 2))  + "\n" \
            + "Investments : " + str(round(self.get_Investments(), 2)) + "\n" \
                +  "My_Money : "  + str(round(self.get_My_Money(), 2)) + "\n" \
                    + "Car_Parts : " + str(round(self.get_Car_Parts(), 2)) + "\n" \
                        +  "Coffee : " + str(round(self.get_Coffee(), 2)) + "\n" \
                            +  "Fun : " + str(round(self.get_Fun(), 2)) + "\n" \
                                +  "Disney : " + str(round(self.get_Disney(), 2))      
        
    
     
    
    def filter(self):
        
        Aprroved_Transactions = set() 
        Coffee_key_words = set(["CAFE", "STARBUCKS", "COFFEE", "coffee", "cafe", "starbucks"]) 
        
        try:
            with open("csv/SavingAccData.csv") as data1:
                file = csv.reader(data1)
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
                    price = line[2]

                    
                    if "-" in price:
                        if price == '-25.00':
                            self.update_Fun(self.get_Fun() - 25.00)
                        else:
                            Aprroved_Transactions.add(line[1])
                            if messagebox.askyesno("There was a charge for " + price + " Was this for car stuff "):
                                self.update_Car_Parts(self.get_Car_Parts() - abs(float(price)))
                            else:
                                self.update_My_Money(self.get_My_Money() - abs(float(price)))
                    else:
                        pass
        except:
            pass
                
        try:
            with open("csv/CheckingAccData.csv") as data2:
                file = csv.reader(data2)
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
                    price = line[2]
                    
                    if "-" in price:
                        if line[1] in Aprroved_Transactions:
                            continue
                        elif price == "-25.00" :
                            continue
                        elif "SMOKE" in line[1] or "smoke" in line[1]:
                            self.update_Fun(self.get_Fun() - abs(float(price))) 
                        elif "disney" in  line[1]:
                            self.update_Disney(self.get_Disney - abs(float(price)))
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
                            pass
                            
                        elif "STARBUCKS" in line[1]: 
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
                        else:
                            self.update_My_Money(self.get_My_Money() + abs(float(price)))
        except:
            pass                        
                            
                
            
           
def main():
    manager = Manager()
    manager.update_Car_Parts(0.00)
    manager.update_Coffee(0.00)
    manager.update_My_Money(96.73)
    manager.update_Fun(0.00)
    manager.update_Food(0.00)
    manager.update_Investments(0.00)
    manager.update_Disney(0.00)
    
    
    print(manager.print_table())
    
    
    
if __name__ == "__main__":
    main()