#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from flight_search import FlightSearch
from data_manager import DataManager
SHEETY_API=SHEETY_API
SHEETY_API_PUT =SHEETY_API_PUT
token=token
headers={
    "Authorization":token
}

response=requests.get(SHEETY_API,headers=headers)
data=response.json()['sheet1']
print(data)

flight_search = FlightSearch(data)
data_manager = DataManager(flight_search,SHEETY_API_PUT,headers)

flight_search.write_testing()
data_manager.update_sheet()




