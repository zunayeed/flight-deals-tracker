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

# check
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
sheet_data = response.json().get("sheet1", [])
#print(sheet_data ) # Adjust the key based on your sheet name in Sheety

# 2. Define date range: Tomorrow -> 6 months (180 days) later
today = datetime.date.today()
start_date = today + datetime.timedelta(days=1)
end_date = start_date + datetime.timedelta(days=2)
#print(start_date, end_date)

# Function to generate daily dates
def get_date_range(start, end):
    curr = start
    while curr <= end:
        yield curr.strftime("%Y-%m-%d")
        curr += datetime.timedelta(days=1)

date_list = list(get_date_range(start_date, end_date))

print(f"Searching flights from {start_date} to {end_date} ({len(date_list)} days)...\n")

# 3. Iterate over cities and find lowest prices using SerpAPI
cheapest_prices = {}

for destination in sheet_data:
    city = destination.get("city")
    iata_code = destination.get("iataCode")

    if not iata_code:
        continue

    print(f"Checking flights to {city} ({iata_code})...")
    lowest_price_for_city = float("inf")
    best_date = None

    for travel_date in date_list:
        params = {
            "engine": "google_flights",
            "departure_id": DEPARTURE_CITY,
            "arrival_id": iata_code,
            "outbound_date": travel_date,
            "type": "2",  # 2 = One-way flight (use '1' for round-trip)
            "currency": CURRENCY,
            "api_key": SERPAPI_KEY
        }

        try:
            flight_res = requests.get("https://serpapi.com/search?engine=google_flights", params=params)
            data = flight_res.json()

            # Extract flights list from 'best_flights' or 'other_flights'
            flights = data.get("best_flights", []) + data.get("other_flights", [])

            for flight in flights:
                price = flight.get("price")
                if price and price < lowest_price_for_city:
                    lowest_price_for_city = price
                    best_date = travel_date

        except Exception as e:
            print(f"Error fetching data for {iata_code} on {travel_date}: {e}")

        # Optional: rate-limiting pause to prevent hitting SerpAPI quota limits too fast
        time.sleep(0.2)

    if lowest_price_for_city != float("inf"):
        cheapest_prices[iata_code] = {
            "city": city,
            "price": lowest_price_for_city,
            "date": best_date
        }
        print(f"-> Lowest price for {city}: {lowest_price_for_city} {CURRENCY} on {best_date}\n")
    else:
        print(f"-> No flights found for {city}\n")

print("--- FINAL SUMMARY ---")
print(cheapest_prices)














