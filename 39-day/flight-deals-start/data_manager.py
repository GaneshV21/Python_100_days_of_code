import requests
from flight_search import FlightSearch

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self,flight:FlightSearch,Api,headers):
        self.flight=flight
        self.api=Api
        self.headers=headers

    def update_sheet(self):
        data=self.flight.write_testing()
        for item in data:
            parameter={
                "sheet1":{
                    "iataCode":item['iataCode']
                }
            }
            requests.put(f"{self.api}{item['id']}",json=parameter,headers=self.headers)