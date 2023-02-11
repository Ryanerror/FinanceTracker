
import sqlite3
import tkinter
from tkinter import messagebox
import csv
import Texter
from datetime import *
import datetime
import shutil
import pathlib
import os

class Manager:
    __slots__ = ["__My_Money_Percent", "__Food_Percent", "__Investments_Percent", "__Car_Parts_Percent", "__Coffee_Percent", "__Fun_Percent", "__Disney_Percent"]
    
    def __init__(self):
        self.__My_Money_Percent = 0.24    
        self.__Food_Percent = 0.35
        self.__Investments_Percent = 0.10
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
        cursor.execute("CREATE TABLE wallet (Newest_Date TEXT, Food REAL, Investments REAL, My_Money REAL, Car_Parts REAL, Coffee REAL, Fun REAL, Disney REAL)")
    
                
        connection.commit()
        connection.close()
      
    def add_row(self):
        connection, cursor = self.connect_to_database()

        cursor.execute("INSERT INTO wallet VAlUES ('2023/2/10', 0, 0, 0, 0, 0, 0, 0)")
        
        connection.commit()
        connection.close()
        
    def get_Newest_Date(self):
        connection, cursor = self.connect_to_database()
        cursor.execute("SELECT Newest_Date FROM wallet")
        Newest_Date = str(cursor.fetchall())
        Newest_Date = Newest_Date.replace(")", "")
        Newest_Date = Newest_Date.replace("(", "")
        Newest_Date = Newest_Date.replace(",", "")
        Newest_Date = Newest_Date.replace("[", "")
        Newest_Date = Newest_Date.replace("]", "")
        Newest_Date = Newest_Date.replace("'", "")
        connection.commit()
        connection.close()
        Newest_Date = Newest_Date.split("/")
        Newest_Date = datetime.datetime(int(Newest_Date[2]), int(Newest_Date[0]), int(Newest_Date[1]))
        
        return Newest_Date
    
    def update_Newest_Date(self, a_string):
        connection, cursor = self.connect_to_database()
        cursor.execute("UPDATE wallet SET Newest_Date = ?", (a_string,))
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
        return "Food : $" + str(round(self.get_Food(), 2))  + "\n" \
            + "Investments : $" + str(round(self.get_Investments(), 2)) + "\n" \
                +  "My_Money : $"  + str(round(self.get_My_Money(), 2)) + "\n" \
                    + "Car_Parts : $" + str(round(self.get_Car_Parts(), 2)) + "\n" \
                        +  "Coffee : $" + str(round(self.get_Coffee(), 2)) + "\n" \
                            +  "Fun : $" + str(round(self.get_Fun(), 2)) + "\n" \
                                +  "Disney : $" + str(round(self.get_Disney(), 2))      
        
    
     
    
    def filter(self):
        print("made it to filter")
        amount_of_money_to_move_to_savings = 0
        amount_of_money_to_invest = 0
        Aprroved_Transactions = set() 
        Coffee_key_words = set(["CAFE", "STARBUCKS", "COFFEE", "coffee", "cafe", "starbucks"])
        food_key_words = set(["MCDONALD'S", "CHIPOTLE", "TAICHI BUBBLE TEA", "DOMINO'S", "WENDYS", "NOODLE", "FOOD"])
        end_date = ""
        
        newest_date = self.get_Newest_Date()                
       
        try:
            with open("csv/Saving_diff.csv") as data1:
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
                    x = line[0].split("/")
                    date = datetime.datetime(int(x[2]), int(x[0]), int(x[1]))
                    
                    if date >= newest_date:
                        if "-" in price:
                            Aprroved_Transactions.add(line[2])
                            if messagebox.askyesno("There was a charge for " + price + " Was this for car stuff "):
                                self.update_Car_Parts(self.get_Car_Parts() - abs(float(price)))
                            else:
                                self.update_Fun(self.get_Fun() - abs(float(price)))
                
                       

        except:
            pass
                
        try:
            with open("csv/checkings_diff.csv") as data2:
                print("made it in here")
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
                    x = line[0].split("/")
                    
                    date = datetime.datetime(int(x[2]), int(x[0]), int(x[1]))
                    end_date = str(date.date())
                    end_date = end_date.replace("-","/")
                    if date >= newest_date:
                        if "-" in price:
                            if line[2] == Aprroved_Transactions:
                                continue
                            elif price == "-25.00" :
                                self.update_Fun(self.get_Fun() - 25.00)
                            elif "SMOKE" in line[1] or "smoke" in line[1] or "Smoke" in line[1]:
                                self.update_Fun(self.get_Fun() - abs(float(price))) 
                            elif "disney" in  line[1]:
                                self.update_Disney(self.get_Disney - abs(float(price)))
                            elif "ROBINHOOD" in  line[1]:
                                self.update_Investments(self.get_Investments + abs(float(price)))
                            else:
                                coffee = False
                                
                                for keyword in Coffee_key_words:
                                    if keyword in line[1]:
                                        coffee = True
                                        break
                                        
                                if coffee:
                                    self.update_Coffee(self.get_Coffee() - abs(float(price)))
                                else:
                                    food = False
                                    for keyword in food_key_words:
                                        if keyword in line[1]:
                                            food = True
                                            break
                                        
                                    if food:
                                        self.update_Food(self.get_Food() - abs(float(price)))
                                    else:
                                        self.update_My_Money(self.get_My_Money() - abs(float(price)))
                                
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
                                amount_of_money_to_move_to_savings =  (income * self.__Fun_Percent) + (income * self.__Car_Parts_Percent)
                                amount_of_money_to_invest = income * self.__Investments_Percent
                                if self.get_Disney() >= 11.00:
                                    self.update_My_Money(self.get_My_Money() + (income * self.__Disney_Percent))
                                else: 
                                    self.update_Disney(self.get_Disney() + (income * self.__Disney_Percent))  
                            else:
                                self.update_My_Money(self.get_My_Money() + abs(float(price)))
                
                if date > self.get_Newest_Date():
                    self.update_Newest_Date(end_date)
                
        except:
            pass
        
        if amount_of_money_to_move_to_savings == 0:
            pass
        else:
            texter = Texter.texter("HI ryan its wensnday move " + str(round(amount_of_money_to_move_to_savings, 2)) + " to your savings")
            texter.notify()

        if amount_of_money_to_invest == 0:
            pass
        else:
            texter = Texter.texter("HI ryan its wensnday move " + str(round(amount_of_money_to_invest, 2)) + " to Robinhood")
            texter.notify()
        
        
         
        
                        
         
           
def main():
    manager = Manager()
    print(manager.get_Newest_Date())
        
    
if __name__ == "__main__":
    main()