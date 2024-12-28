
from bs4 import BeautifulSoup
import requests
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

google_form_url = "https://forms.gle/8mtM7UwKRRUvEzYq7"

Zillow_Url = "https://appbrewery.github.io/Zillow-Clone/"

response =requests.get(Zillow_Url)
yc_soup=BeautifulSoup(response.text,"html.parser")
ul_list = yc_soup.find_all(name='li',class_='ListItem-c11n-8-84-3-StyledListCardWrapper')
# print(ul_list)
main =[]
for soup in range(len(ul_list)):
    obj={}
    address = ul_list[soup].find(name='address').getText().strip()
    print(address)
    price = ul_list[soup].find(name='span').getText().split('+')[0]
    print(price)
    anchor = ul_list[soup].find(name='a').get('href')
    print(anchor)
    obj['address'] = address
    obj['price'] = price
    obj['link'] = anchor
    main.append(obj)


driver = webdriver.Chrome(options=chrome_options)
driver.get(google_form_url)
time.sleep(1)
for item in range(len(main)):
    time.sleep(3)
    input_boxes = driver.find_elements(By.XPATH, "//div[@class='Xb9hP']/input")
    input_boxes[0].send_keys(main[item]['address'])
    time.sleep(0.5)
    input_boxes[1].send_keys(main[item]['price'])
    time.sleep(0.5)
    input_boxes[2].send_keys(main[item]['link'])
    time.sleep(0.5)
    submit_button = driver.find_element(By.XPATH,"//div[@class='DE3NNc CekdCb']/div/div")
    submit_button.click()
    time.sleep(2)
    driver.refresh()


