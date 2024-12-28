import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

url = "https://www.speedtest.net/"

class InternetSpeedTwitterBot:
    def __init__(self,up,down):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(url)
        self.driver.maximize_window()

        self.up = up
        self.down = down

    def get_internet_speed(self):
        time.sleep(10)
        go_button = self.driver.find_element(By.XPATH,"//div[@class='start-button']/a/span[@class='start-text']")
        go_button.click()
        status = True
        result_id = ""

        # time.sleep(60)
        while(status):
            try:
                result_id = self.driver.find_element(By.XPATH,"//div[@class='result-item result-item-inline result-item-align-center result-item-id']/div/a")
                status = False
            except:
                time.sleep(10)
                print(f"An error occurred")
        internet_Datas =  self.driver.find_elements(By.XPATH,"//div[@class='result-data u-align-left']")
        self.down=internet_Datas[0].text
        self.up =internet_Datas[1].text
        self.tweet_at_provider()


    def tweet_at_provider(self):
        print(self.up)
        print(self.down)



bot = InternetSpeedTwitterBot(0,0)
bot.get_internet_speed()