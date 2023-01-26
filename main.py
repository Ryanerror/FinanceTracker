import Manager
import Texter
import Webscraper
from selenium import webdriver


def main():
    driver = webdriver.Chrome("C:/Users/ryang/OneDrive/Desktop/chromedriver.exe")
    manager = Manager.Manager()
    texter = Texter.texter("")
    scraper = Webscraper.WebScrapper("ryangarvin", "*************", driver)
    
    scraper.execute()
    manager.filter()
    texter.set_info(manager.print_table())
    texter.notify()

if __name__ == "__main__":
    main()
