from selenium import webdriver
from selenium.webdriver.common.by import By
# keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
url="https://www.python.org"
driver =  webdriver.Chrome(options=chrome_options)
driver.get(url)

date_class=driver.find_elements(By.CSS_SELECTOR,value=".event-widget time")
anchor_class=driver.find_elements(By.CSS_SELECTOR,value=".event-widget ul a")
task_obj={}
for item in range(0,len(date_class)):
    obj={}
    obj['time']=date_class[item].text
    obj['name']=anchor_class[item].text
    task_obj[item]=obj
    # print(date_class[item].text,anchor_class[item].text)

print(task_obj)

