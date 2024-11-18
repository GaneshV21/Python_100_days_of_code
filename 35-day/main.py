import requests
from twilio.rest import Client
# import os
Api_Key=Api_Key
parameter={
    "lat":10.8462,
    "lon":78.6982,
    "appid":Api_Key,
    "cnt":4
}
# print(os.environ.get("Api_Key")) -- i dont know how to store in env.but retrieve it this is the line
response=requests.get("https://api.openweathermap.org/data/2.5/forecast",params=parameter)
response.raise_for_status()
weather_data=response.json()
# print(weather_data)


#sending sms to bring an umbrella  -- twillio api -- not registered in that so sms is not sending
account_sid="id"
auth_token="token"

will_rain=False
weather_list=weather_data['list']
for item in weather_data['list']:
    for weather in item['weather']:
        if weather['id']<700:
            will_rain=True

if will_rain:
    print("Bring Umbrella")
    client= Client(account_sid,auth_token)
    message=client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔",
        from_="your_twillio_phone_number",
        to="your_friend_number"
    )
    print(message.status)


# Use pythonanywhere to make your code run daily 7.00 am something like that --> uploaded in cloud

## --> not done that part