# ✈️ Flight Deals Tracker

A Python application that automatically searches for cheap flights from your preferred departure airport to multiple destinations and alerts you when prices drop below your target price.

This project was built to practice working with REST APIs, object-oriented programming, caching, and external services in Python.

---

## Features

* Search flights from a departure airport (default: **DFW**)
* Track multiple destinations from a Google Sheet
* Store airport IATA codes and target prices
* Automatically search within a configurable date range
* Cache API requests to reduce API usage
* Modular, object-oriented codebase
* Ready for email or SMS notifications when deals are found

---

## Project Structure

```text
flight-deals-tracker/
│
├── main.py                    # Application entry point
├── data_manager.py            # Reads/writes destination data
├── flight_search.py           # Searches flights using an API
├── flight_data.py             # Processes flight results
├── notification_manager.py    # Sends deal notifications
├── requirements.txt
└── README.md
```

---

## How It Works

1. Read destination information from a Google Sheet.
2. Load each destination's:

   * City
   * Airport IATA code
   * Lowest acceptable price
3. Search for available flights.
4. Find the cheapest available flight.
5. Compare the flight price with the target price.
6. Notify the user if a better deal is found.

---

## Technologies Used

* Python 3
* Requests
* requests-cache
* Sheety API
* Flight Search API
* REST APIs
* Object-Oriented Programming (OOP)

---

## Installation

Clone the repository:

```bash
git clone https://github.com/zunayeed/flight-deals-tracker.git
```

Navigate to the project:

```bash
cd flight-deals-tracker
```

Create a virtual environment (recommended):

```bash
python -m venv venv
```

Activate it.

**Windows**

```bash
venv\Scripts\activate
```

**macOS/Linux**

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Configuration

Before running the application, configure your API credentials and endpoints.

Depending on your implementation, you may need:

* Flight Search API key
* Sheety API endpoint
* Sheety authentication token
* Email or SMS credentials (if notifications are enabled)

A common approach is to store these values in a `.env` file.

Example:

```env
FLIGHT_API_KEY=your_api_key
SHEETY_ENDPOINT=https://api.sheety.co/...
SHEETY_TOKEN=your_token
EMAIL_ADDRESS=your_email
EMAIL_PASSWORD=your_password
```

---

## Running the Project

```bash
python main.py
```

The application will:

* Read your destinations
* Search for flights
* Compare prices
* Notify you when a cheaper flight is found

---

## Example Destination Data

| City   | IATA Code | Lowest Price |
| ------ | --------- | -----------: |
| Dhaka  | DAC       |          450 |
| London | LHR       |          700 |
| Paris  | CDG       |          650 |

---

## Request Caching

The application uses `requests-cache` to reduce repeated API calls.

```python
requests_cache.install_cache(
    "flight_cache",
    urls_expire_after={
        "*.sheety.co*": requests_cache.DO_NOT_CACHE,
        "*": 7200,
    }
)
```

* Flight API responses are cached for **2 hours**
* Google Sheet requests are never cached to ensure the latest data

---

## Future Improvements

* Support round-trip and one-way searches
* Search nearby airports automatically
* Multi-city tracking
* Web dashboard
* Docker support
* Scheduled daily searches
* Price history charts
* Telegram and Discord notifications
* Unit tests

---

## Learning Objectives

This project demonstrates:

* Python modules and packages
* Classes and object-oriented programming
* Working with REST APIs
* JSON parsing
* Environment variables
* HTTP requests
* Request caching
* Working with dates and times
* Clean project organization

---

## License

This project is available under the MIT License.

---


