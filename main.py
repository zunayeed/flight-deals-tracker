import requests_cache
import requests
import serpapi
from pprint import pprint
from datetime import datetime, timedelta

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager

# ==================== Conserve requests and preserve your free plan ====================
# Here we are not caching anything ending in *.sheety.co
# everything else is cached for 1 hour (3600 seconds).
# feel free to experiment!
requests_cache.install_cache(
    "flight_cache",
    urls_expire_after={
        "*.sheety.co*": requests_cache.DO_NOT_CACHE,
        "*": 7200,
    }
)



DEPARTURE_CITY = "DFW"
CURRENCY = "USD"


# ==================== Talk to Sheety ====================
# 4. Pass the data back to the main.py file to print the data from main.py
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

# 5. Try importing pretty print and printing the data out again using pprint() to see it formatted.
# Print the sheet_data and verify that it includes the airport IATA codes for each city.
pprint("##### sheet_data from main.py #####")
pprint(sheet_data)
#[{'city': 'Dhaka', 'iataCode': 'DAC', 'id': 2, 'lowestPrice': 450}]

flight_search = FlightSearch()
# Create an instance of the NotificationManager
#notification_manager = NotificationManager()





# ==================== Set the Dates ====================

start_date = datetime.now() + timedelta(days=5)
end_date = start_date + timedelta(days=180)
ORIGIN_CITY_IATA = "DFW"  # dallas

#tomorrow = datetime.now() + timedelta(days=1)
#six_month_from_today = datetime.now() + timedelta(days=(6 * 30))


# ==================== Do a Flight Search ====================



flights = flight_search.check_flights(
    origin_city_code="DFW",
    destination_city_code="DAC",
    from_time= start_date,
    to_time=end_date
)

for destination in sheet_data:
    pprint(f"Getting direct flights for {destination['city']}...")
    flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=start_date,
        to_time=end_date
    )

#pprint(flights)

# ==================== Show the Cheapest Flight ====================

    cheapest_flight = find_cheapest_flight(flights, return_date=end_date.strftime("%Y-%m-%d"))
    pprint(f"{sheet_data[0]['city']}: USD {cheapest_flight.price}")

    if cheapest_flight.price == "N/A":
        print(f"No direct flight to {destination['city']}. Looking for indirect flights...")
        stopover_flights = flight_search.check_flights(
            ORIGIN_CITY_IATA,
            destination["iataCode"],
            from_time= start_date,
            to_time=end_date,
            is_direct=False
        )
        cheapest_flight = find_cheapest_flight(stopover_flights, return_date=end_date.strftime("%Y-%m-%d"))
        print(f"Cheapest indirect flight price is: USD {cheapest_flight.price}")




    data_manager.update_lowest_price(sheet_data[0]["id"], cheapest_flight.price)
    # notification_manager.send_sms(
    #     message_body=f"Low price alert! Only GBP {cheapest_flight.price} to fly "
    #                  f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
    #                  f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
    # )
    # SMS not working? Try whatsapp instead.
    # notification_manager.send_whatsapp(
    #     message_body=f"Low price alert! Only GBP {cheapest_flight.price} to fly "
    #                  f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
    #                  f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
    # )








