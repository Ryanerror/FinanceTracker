import Manager
import Texter
import webscraper
from selenium import webdriver


def main():
    driver = webdriver.Chrome("C:/Users/ryang/OneDrive/Desktop/chromedriver.exe")
    manager = Manager.Manager()
    texter = Texter.texter("")
    scraper = webscraper.WebScrapper("ryangarvin", "Spongebob,220679187", driver)
    
    # manager.update_My_Money(202.26)
    # manager.update_Food(152.77)
    # manager.update_Car_Parts(42.15)
    # manager.update_Disney(3.01)
    # manager.update_Coffee(21.07)
    # manager.update_Fun(27.10)
    
    
    print(manager.get_Newest_Date())
    print(manager.print_table())
    
    scraper.execute()
    manager.filter()
    texter.set_info(manager.print_table()) 
    print(manager.print_table())
    texter.notify()
   

if __name__ == "__main__":
    main()
