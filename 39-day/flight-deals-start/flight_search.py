class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self,data):
        self.prices_list=data

    def write_testing(self):
        # flight IATA Code api register page is not working so i hard coded the iata code in sheets
        # for item in self.prices_list:
        #     if item['iataCode'] == "":
        #         item['iataCode'] = "TESTING"
        return self.prices_list


