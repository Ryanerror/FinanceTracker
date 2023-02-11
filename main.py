import Manager
import Texter
import webscraper
from selenium import webdriver


def main():
    driver = webdriver.Chrome("C:/Users/ryang/OneDrive/Desktop/chromedriver.exe")
    manager = Manager.Manager()
    texter = Texter.texter("")
    scraper = webscraper.WebScrapper("ryangarvin", "Spongebob,220679187", driver)
    
    manager.update_Newest_Date("2023/2/10")
    print(manager.get_Newest_Date())
    manager.update_Car_Parts(0)
    manager.update_Coffee(0)
    manager.update_My_Money(50.23)
    manager.update_Fun(0)
    manager.update_Food(1.40)
    manager.update_Investments(80.00)
    manager.update_Disney(0)
    manager.update_Newest_Date("1/12/2023")
    
    # print(manager.get_Newest_Date())
    print(manager.print_table())
    
    scraper.execute()
    manager.filter()
    texter.set_info(manager.print_table())
    texter.notify()
    print(manager.print_table())

if __name__ == "__main__":
    main()
