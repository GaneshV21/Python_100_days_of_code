
import requests
from datetime import datetime
import os

API_KEY = os.environ.get("API_KEY")
APP_ID = os.environ.get("APP_ID")
api_host_endpoints = os.environ.get("api_host_endpoints")
endpoint = os.environ.get("endpoint")
spread_sheet_api = os.environ.get("spread_sheet_api")
token = os.environ.get("token")

print(api_host_endpoints,endpoint)
parameter={
    "query":input("Tell me which exercises you did: "),
    "weight_kg":58,
    "height_cm":125,
    "age":21
}
headers={
    "x-app-id":APP_ID,
    "x-app-key":API_KEY
}

response=requests.post(f"{api_host_endpoints}{endpoint}",json=parameter,headers=headers)
data=response.json()['exercises'][0]
print(data)

calories = data['nf_calories']
duration = data['duration_min']
exercise = data['name'].title()

spread_sheet_header={
    "Authorization":token
}

today_date=datetime.now()
print(today_date)

post_parameter={
    "sheet1":{
        "date":today_date.strftime("%d/%m/%Y"),
        "time":today_date.strftime("%H:%M:%S"),
        "exercise":exercise,
        "duration":duration,
        "calories":calories
    }
}

res_post=requests.post(spread_sheet_api,json=post_parameter,headers=spread_sheet_header)
print(res_post.status_code)
res=requests.get(spread_sheet_api,headers=spread_sheet_header)
print(res.text);