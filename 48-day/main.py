from selenium import webdriver
from selenium.webdriver.common.by import By

# keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
url="https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
url_2="https://www.python.org"
driver =  webdriver.Chrome(options=chrome_options)
driver.get(url)

driver2 =  webdriver.Chrome(options=chrome_options)
driver2.get(url_2)

#class name
# price_dollar=driver.find_element(By.CLASS_NAME,value="a-price-whole")
# price_cents=driver.find_element(By.CLASS_NAME,value="a-price-fraction")

# print(f"the price is{price_dollar.text}.{price_cents.text}")

#Name
# search_bar=driver2.find_element(By.NAME,value="q")
# print(search_bar.tag_name)
# print(search_bar.get_attribute("placeholder"))

#id
# button=driver2.find_element(By.ID,value="submit")
# print(button.text)
# print(button.get_attribute("title"))
# print(button.size)

#css_selector
documentation_link=driver2.find_element(By.CSS_SELECTOR,value=".documentation-widget a")
print(documentation_link.text)

#x-path
xpath=driver2.find_element(By.XPATH,value='//*[@id="container"]/li[2]/ul/li[1]/a')
print(xpath.text)

driver.close() # -- close the particular page
# driver.quit() # -- close the entire browser
