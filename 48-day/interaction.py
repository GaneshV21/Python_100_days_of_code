import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

#Learning
# url="https://en.wikipedia.org/wiki/Main_Page"
# driver =  webdriver.Chrome(options=chrome_options)
# driver.get(url)
#
# article_data=driver.find_element(By.CSS_SELECTOR,value="#articlecount a")
# print(article_data.text)
# # article_data.click()
#
# # Find element by Link text
# all_portals = driver.find_element(By.LINK_TEXT,value="Content portals")
# # all_portals.click()
#
# # Find the "search" <input> by name
# search=driver.find_element(By.NAME,value="search")
#
# #sending keyboard input to selenium
# search.send_keys( "Python",Keys.ENTER)
#
#
# #Task:
# url2="https://secure-retreat-92358.herokuapp.com/"
# driver2=webdriver.Chrome(options=chrome_options)
# driver2.get(url2)
#
# f_name=driver2.find_element(By.NAME,value="fName")
# l_name=driver2.find_element(By.NAME,value="lName")
# email=driver2.find_element(By.NAME,value="email")
#
# f_name.send_keys("Ganesh")
# l_name.send_keys("V")
# email.send_keys("ganesh@gmail.com")
#
# Button=driver2.find_element(By.CSS_SELECTOR,value="Button")
# Button.click()


#Bot Game
url3="http://orteil.dashnet.org/experiments/cookie/"
driver3=webdriver.Chrome(options=chrome_options)
driver3.get(url3)

#Cokkie Button
cookie_button=driver3.find_element(By.ID,value="cookie")

#calculation:

#Right side datas divs
right_side = driver3.find_elements(By.CSS_SELECTOR, value="#store div")
# print(right_side)

#Filter the right side datas only contain id -  click,grandma,factory datas stored in array
right_side_data_only = [item.get_attribute("id") for item in right_side]
# print(right_side_data_only)

#Amount list of that data
amount_list = driver3.find_elements(By.CSS_SELECTOR, value="#store div b")
# print(amount_list)

#spliting the data
amount_data = [(item.text.split("-")[-1]) for item in amount_list]
# print(amount_data)

#convert into integer
amount_data_split = [int(item.replace(",", "").strip()) for item in amount_data if item != ""]
# print(amount_data_split)


#current time + 5mins
five_min=time.time() + 60*5

#current time + 5 seconds
timeout = time.time() + 5

run=True
while (run):
    #cookie button is always clicked
    cookie_button.click()

    #after 5 minutes the game end
    if time.time()>five_min:
        run= False

    #every 5 seconds clicking can be done on right side
    if time.time() > timeout:
        #timout value is changed
        timeout = time.time() + 5

        button_enabled = driver3.find_elements(By.CSS_SELECTOR, value="#store div")
        button_All = [item.get_attribute('class') for item in button_enabled]
        # print(button_All)

        button_not_grayed = [{amount_data_split[index]:value} for index,value in enumerate(button_All) if value == ""]
        # print(button_not_grayed,len(button_not_grayed))

        if len(button_not_grayed)!=0:
            data = button_not_grayed[len(button_not_grayed)-1]
            # print(data)
            keys = [key for (key,value) in data.items()]
            # print(keys)
            index=amount_data_split.index(keys[0])

            # print(right_side[index])
            button_enabled[index].click()

score=driver3.find_elements(By.XPATH,value='//*[@id="cps"]')
print(score[0].text)







