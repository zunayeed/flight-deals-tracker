from dataclasses import dataclass


@dataclass
class FlightData:
    price: float | str
    origin_airport: str
    destination_airport: str
    out_date: str
    return_date: str

    @classmethod
    def from_api(cls, flight_dict: dict, return_date: str):
        """Helper to instantiate FlightData directly from a raw flight dictionary."""
        first_leg = flight_dict["flights"][0]
        last_leg = flight_dict["flights"][-1]

        return cls(
            price=flight_dict["price"],
            origin_airport=first_leg["departure_airport"]["id"],
            destination_airport=last_leg["arrival_airport"]["id"],
            out_date=first_leg["departure_airport"]["time"].split(" ")[0],
            return_date=return_date
        )


def find_cheapest_flight(data: dict, return_date: str) -> FlightData:
    all_flights = (data.get("best_flights", []) + data.get("other_flights", [])) if data else []
    valid_flights = [f for f in all_flights if "price" in f]

    if not valid_flights:
        print("No flight data")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")

    cheapest = min(valid_flights, key=lambda f: f["price"])
    return FlightData.from_api(cheapest, return_date)