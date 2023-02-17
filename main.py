import Manager
import Texter
import webscraper
from selenium import webdriver


def main():
    driver = webdriver.Chrome("C:/Users/ryang/OneDrive/Desktop/chromedriver.exe")
    manager = Manager.Manager()
    texter = Texter.texter("")
    scraper = webscraper.WebScrapper("ryangarvin", "Spongebob,220679187", driver)
    
   
    
    
    # print(manager.get_Newest_Date())
    print(manager.print_table())
    
    scraper.execute()
    manager.filter()
    texter.set_info(manager.print_table())
    texter.notify()
    print(manager.print_table())

if __name__ == "__main__":
    main()
