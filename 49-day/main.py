import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)


url="https://www.linkedin.com"
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)
driver.maximize_window()

# signin button
sigin_button = driver.find_element(By.CSS_SELECTOR,value="nav div .nav__button-secondary")
sigin_button.click()

#email and password box with content
email_box = driver.find_element(By.ID,value="username")
email_box.send_keys("linked_in_email")
password = driver.find_element(By.ID,value="password")
password.send_keys("linked_in_password")

#sigin button
submit_button = driver.find_element(By.CSS_SELECTOR,value=".login__form_action_container button")
submit_button.send_keys(Keys.ENTER)

# time.sleep(20)

#top job button
top_job_button = driver.find_elements(By.CSS_SELECTOR,value=".global-nav__content nav a")[2]
top_job_button.click()

time.sleep(3)
#job_search_box
job_search_box = driver.find_elements(By.CSS_SELECTOR,value='#global-nav-search input')[0]
job_search_box.send_keys("Python Developer", Keys.ENTER)

time.sleep(3)
#filters
Easy_Apply=driver.find_elements(By.CSS_SELECTOR,value='#search-reusables__filters-bar ul li')
Easy_Apply[len(Easy_Apply)-1].click()

time.sleep(2)

all_jobs=driver.find_elements(By.XPATH,value="//ul[@class='scaffold-layout__list-container']/li")
print(len(all_jobs))

for job in range(1,len(all_jobs)+1):
    # driver.execute_script("arguments[0].click();", job)
    test = driver.find_element(By.XPATH, "//ul[@class='scaffold-layout__list-container']/li["+str(job)+"]")
    driver.execute_script("arguments[0].scrollIntoView();", test)
    test.click()
    time.sleep(2)
    each_Save_button = driver.find_element(By.XPATH,value="//div[@class='mt5']/div/button")
    each_Save_button.click()
    time.sleep(5)


driver.quit()
