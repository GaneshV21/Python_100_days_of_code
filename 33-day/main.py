import requests
import datetime
import smtplib
import time

MY_LAT=MY_LAT
MY_LONG=MY_LONG
MY_EMAIL=useremail
MY_PASSWORD=userpassword

def is_iss_overhead():
    response=requests.get(url="http://api.open-notify.org/iss-now.json")
    print(response.status_code) # - 200
    print(response.json()) #- data comming
    response.raise_for_status() # automatically error raised -- requests.exceptions.HTTPError: 404 Client Error: Not Found for url: http://api.open-notify.org/issdd-now.json
    data = response.json()
    latitude= float(data['iss_position']['latitude'])
    longitude= float(data['iss_position']['longitude'])

    iss_position = (longitude,latitude)
    print(iss_position)

    if MY_LAT-5<=latitude <=MY_LAT+5 and MY_LONG-5<=longitude<=MY_LONG+5:
        return True

def is_night():
    parameter={
        "lat":MY_LAT,
        "lng":MY_LONG,
        "formatted":0
    }
    res=requests.get(url=f"https://api.sunrise-sunset.org/json",params=parameter)
    res.raise_for_status()
    data=res.json()

    sunrise=data['results']['sunrise']
    sunset=data['results']['sunset']

    date_today=datetime.datetime.now()
    sunrise_time=int(sunrise.split("T")[1].split(":")[0])
    sunset_time=int(sunset.split("T")[1].split(":")[0])

    print(sunrise_time)
    print(sunset_time)
    today_day=date_today.hour
    print(today_day)
    if today_day>=sunset_time or today_day<=sunrise_time:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL,MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject:Look Up \n\n The ISS is above you in the sky"
            )