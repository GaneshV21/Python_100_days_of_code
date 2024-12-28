import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
url="https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
my_email = my_email
password=password
headers={"Accept-Language":"en-GB,en-US;q=0.9,en;q=0.8","User-Agent":"Mozilla/5.0(Macintosh; Intel Mac OS X 10_15_5) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"}
response=requests.get(url=url,headers=headers)
soup=BeautifulSoup(response.text,"lxml")
# print(soup)

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

text=soup.find(id="productTitle").get_text().strip()
if price_as_float<200:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="xyz@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\n{text}\n{url}".encode("utf-8")
        )

