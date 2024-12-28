import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)


url="https://thispersondoesnotexist.com/"
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)
driver.maximize_window()

for _ in range(10):
    driver.refresh()
    time.sleep(2)

