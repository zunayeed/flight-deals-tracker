# Define the date range used when searching for flights.
# The current implementation searches from tomorrow until the configured end date.
today = datetime.date.today()
start_date = today + datetime.timedelta(days=1)
end_date = start_date + datetime.timedelta(days=3)


def get_date_range(start, end):
    """
    Generate each date between start and end (inclusive).

    Dates are returned in the format required by the flight search API.
    """
    curr = start

    while curr <= end:
        yield curr.strftime("%Y-%m-%d")
        curr += datetime.timedelta(days=1)


date_list = list(get_date_range(start_date, end_date))

print(f"Searching flights from {start_date} to {end_date} ({len(date_list)} days)...\n")


# Stores the cheapest available flight found for each destination airport.
cheapest_prices = {}


# Check every destination from the spreadsheet and search available flights.
for destination in sheet_data:
    city = destination.get("city")
    iata_code = destination.get("iataCode")

    # Skip entries that cannot be searched because no airport code exists.
    if not iata_code:
        continue

    print(f"Checking flights to {city} ({iata_code})...")

    lowest_price_for_city = float("inf")
    best_date = None


    # Search each possible travel date to find the lowest available fare.
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
            flight_res = requests.get(
                "https://serpapi.com/search?engine=google_flights",
                params=params
            )

            data = flight_res.json()

            # SerpAPI separates results into recommended and alternative flights.
            flights = data.get("best_flights", []) + data.get("other_flights", [])

            for flight in flights:
                price = flight.get("price")

                # Keep only the lowest price found for this destination.
                if price and price < lowest_price_for_city:
                    lowest_price_for_city = price
                    best_date = travel_date

        except Exception as e:
            print(f"Error fetching data for {iata_code} on {travel_date}: {e}")

        # Prevent sending requests too quickly and exceeding API limits.
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


