import requests
import serpapi
import datetime
import time
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
# Check second commit
# Skeleton snippet of execution loop in main.py
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager


# Replace with your Sheety endpoint URL
# Format: https://api.sheety.co/YOUR_USERNAME/YOUR_PROJECT_NAME/YOUR_SHEET_NAME
SHEETY_ENDPOINT = "https://api.sheety.co/3bf8f403b513b361bbb26ef0ccfd53bd/flightPrices/sheet1"
SERPAPI_KEY = "0da89cc1ad1aad2ce8410c00e1ae216d7c9f47e9f35360983b270db9128f7097"  # Replace with your actual SerpAPI key
DEPARTURE_CITY = "DFW"  # Your origin IATA code (e.g., LON for London)
CURRENCY = "USD"  # Currency code (e.g., USD, GBP, EUR)


# If your Sheety API requires authentication (Bearer Token)
"""
headers = {
    "Authorization": "Bearer YOUR_SHEETY_BEARER_TOKEN"
}
"""
# 1. Fetch cities and IATA codes from Sheety
response = requests.get(SHEETY_ENDPOINT)
response.raise_for_status()
data = response.json().get("sheet1", [])
print(data ) # Adjust the key based on your sheet name in Sheety




















"""

class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        #Sends a GET request to the Sheety API to fetch sheet rows.
        response = requests.get(url=SHEETY_ENDPOINT, headers=headers)
        response.raise_for_status()  # Raises an exception if the HTTP request failed

        data = response.json()

        # Sheety nests the returned JSON under the lowerCamelCase name of the sheet (e.g., 'prices')
        # Adjust 'prices' to match your sheet name key in the response JSON
        self.destination_data = data.get("prices", [])
        return self.destination_data


# --- Example Usage ---
if __name__ == "__main__":
    data_manager = DataManager()
    sheet_data = data_manager.get_destination_data()

    # Iterate through each row and print city + IATA code
    for row in sheet_data:
        city = row.get("city")
        iata_code = row.get("iataCode")  # Sheety camelCases column headers (e.g., 'IATA Code' -> 'iataCode')
        print(f"City: {city} | IATA Code: {iata_code}")


"""



"""
data_mgr = DataManager()
flight_search = FlightSearch()
notifier = NotificationManager()

sheet_data = data_mgr.get_destination_data()

for row in sheet_data:
    flight = flight_search.check_flights(
        origin_city_code="LON",
        destination_city_code=row["iataCode"],
        from_time=tomorrow,
        to_time=six_months_later
    )
    if flight and flight.price < row["lowestPrice"]:
        notifier.send_sms(
            message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_airport} to {flight.destination_airport}!"
        )


"""