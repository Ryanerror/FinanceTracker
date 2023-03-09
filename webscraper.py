from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import shutil
import pathlib
import os

class WebScrapper:
    __slots__ = [ "__user_name", "__password", "__driver"]
    
    def __init__(self, user_name, password, driver):
        self.__password = password
        self.__user_name = user_name
        self.__driver = driver
        

    def get_loged_in_driver(self):
        
        self.__driver.get("https://secure.bankofamerica.com/login/sign-in/signOnV2Screen.go")

        time.sleep(1)
        
        user_element = self.__driver.find_element(By.ID, "enterID-input")
        user_element.send_keys(self.__user_name)
        
        # pasword_element = self.__driver.find_element_by_id("dummy-passcode")
        pasword_element = self.__driver.find_element(By.ID, "tlpvt-passcode-input")
        pasword_element.send_keys(self.__password)

        pasword_element.submit()
        
        # time.sleep(100)
        return self.__driver


    def get_checkings_account_data(self):
        time.sleep(4)
        self.__driver.find_element(By.NAME, "DDA_details").click()
        time.sleep(4)
        self.__driver.find_element(By.ID, "download-transactions").click()
        time.sleep(4)
        self.__driver.find_element(By.ID, "select_txnPeriod").click()
        time.sleep(4)
        curr_transaction_selection = Select(self.__driver.find_element(By.ID, "select_txnPeriod"))
        curr_transaction_selection.select_by_value("Current transactions")
        time.sleep(4)
        file_type_selection = Select(self.__driver.find_element(By.ID, "select_fileType"))
        file_type_selection.select_by_value("csv")
        time.sleep(4)
        self.__driver.find_element(By.ID, "btn-download-txn").click()
        time.sleep(4)
    
    def get_savings_account_data(self):
        time.sleep(4)
        self.__driver.find_element(By.LINK_TEXT, "Adv Plus Banking - 6015").click()
        time.sleep(4)
        self.__driver.find_element(By.ID, "download-transactions").click()
        time.sleep(4)
        self.__driver.find_element(By.ID, "select_txnPeriod").click()
        time.sleep(4)
        curr_transaction_selection = Select(self.__driver.find_element(By.ID, "select_txnPeriod"))
        curr_transaction_selection.select_by_value("Current transactions")
        time.sleep(4)
        file_type_selection = Select(self.__driver.find_element(By.ID, "select_fileType"))
        file_type_selection.select_by_value("csv")
        time.sleep(4)
        self.__driver.find_element(By.ID, "btn-download-txn").click()
        time.sleep(4)
    
    
    def make_new_csv(self, code):
        if code == "C":
            with open('csv/CheckingAccData.csv', 'r') as csv1, open('csv/CheckingAccData(1).csv', 'r') as csv2: 
                next(csv1)
                next(csv1)
                next(csv1)
                next(csv1)
                next(csv1)
                # ryan fix this later this is dumb 
                next(csv1)
                next(csv1)
                next(csv1)
                next(csv2)
                next(csv2)
                next(csv2)
                next(csv2)
                next(csv2)
                # ryan fix this later this is dumb 
                next(csv2)
                next(csv2)
                next(csv2)
                
                
                import1 = csv1.readlines()
                import2 = csv2.readlines()
                
                with open('csv/checkings_diff.csv', 'w') as outFile:
                    outFile.write("\n")
                    outFile.write("\n")
                    outFile.write("\n")
                    outFile.write("\n")
                    outFile.write("\n")
                    outFile.write("\n")
                    outFile.write("\n")
                    outFile.write("\n")
                    # Create CSV file with differences
                    for row in import2:
                        if row not in import1:
                            outFile.write(row)
                            
        elif code == "S":
            with open('csv/SavingAccData.csv', 'r') as csv1, open('csv/SavingAccData(1).csv', 'r') as csv2:  # Import CSV files
                next(csv1)
                next(csv1)
                next(csv1)
                next(csv1)
                next(csv1)
                # ryan fix this later this is dumb 
                next(csv1)
                next(csv1)
                next(csv1)
                next(csv2)
                next(csv2)
                next(csv2)
                next(csv2)
                next(csv2)
                # ryan fix this later this is dumb 
                next(csv2)
                next(csv2)
                next(csv2)
                
                
                import1 = csv1.readlines()
                import2 = csv2.readlines()
                
                with open('csv/saving_diff.csv', 'w') as outFile:
                # Create CSV file with differences
                    for row in import2:
                        outFile.write("\n")
                        outFile.write("\n")
                        outFile.write("\n")
                        outFile.write("\n")
                        outFile.write("\n")
                        outFile.write("\n")
                        outFile.write("\n")
                        outFile.write("\n")
                        if row not in import1:
                            outFile.write(row)
        
    def execute(self):
        SavingAccData = "SavingAccData"
        CheckingAccData = "CheckingAccData"
        # dir = 'C:/Users/ryang/OneDrive/Desktop/FinanceTracker/csv'
        
        try:
            os.remove("C:/Users/ryang/OneDrive/Desktop/FinanceTracker/csv/checkings_diff.csv")
        except:
            pass
        
        time.sleep(1)
        self.get_loged_in_driver()
        
        self.get_checkings_account_data()
        time.sleep(1)
          
        src_path = "C:/Users/ryang/Downloads/stmt.csv"
        dst_path = "C:/Users/ryang/OneDrive/Desktop/FinanceTracker/csv/CheckingAccData(1).csv"
        shutil.move(src_path, dst_path)
        self.make_new_csv("C")
        time.sleep(1)
        os.remove("C:/Users/ryang/OneDrive/Desktop/FinanceTracker/csv/CheckingAccData.csv")
        os.rename("C:/Users/ryang/OneDrive/Desktop/FinanceTracker/csv/CheckingAccData(1).csv", "C:/Users/ryang/OneDrive/Desktop/FinanceTracker/csv/CheckingAccData.csv")
    
        
        time.sleep(2)
        
        try:
            os.remove("C:/Users/ryang/OneDrive/Desktop/FinanceTracker/csv/saving_diff.csv")
        except:
            pass
        
        time.sleep(1)
        self.get_loged_in_driver()
        self.get_savings_account_data()
        time.sleep(1)

        src_path = "C:/Users/ryang/Downloads/stmt.csv"
        dst_path = "C:/Users/ryang/OneDrive/Desktop/FinanceTracker/csv/SavingAccData(1).csv"
        shutil.move(src_path, dst_path)
        self.make_new_csv("S")
        time.sleep(1)
        os.remove("C:/Users/ryang/OneDrive/Desktop/FinanceTracker/csv/SavingAccData.csv")
        os.rename("C:/Users/ryang/OneDrive/Desktop/FinanceTracker/csv/SavingAccData(1).csv", "C:/Users/ryang/OneDrive/Desktop/FinanceTracker/csv/SavingAccData.csv")
       
            
        
               
        
            
                

def main():
    driver = webdriver.Chrome("C:/Users/ryang/OneDrive/Desktop/chromedriver.exe")
    webscrapper = WebScrapper("ryangarvin", "Spongebob,220679187", driver)
    
    webscrapper.execute()
    
    
if __name__ == "__main__":
    main()
