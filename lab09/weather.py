import argparse
from copy import error
import requests

def get_coordinates(city):
    """Get latitude and longitude for a city using OpenStreetMap"""
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": city,
        "format": "json",
        "limit": 1
    }
    headers = {
        "User-Agent": "MWCC"
    }
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()

    data = response.json()

    if not data:
        raise ValueError(f"Location not found: {city}")

    lat = float(data[0]["lat"])
    lon = float(data[0]["lon"])
    return lat, lon

def get_noaa_endpoint(lat, lon):
    """Get the NOAA forecast for the given coordinates"""

    url = f"https://api.weather.gov/points/{lat},{lon}"
    headers = {
        "User-Agent": "MWCC"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    data = response.json()
    forecast_url = data["properties"]["forecast"]

    return forecast_url

def get_noaa_forecast(url):
    """Get the NOAA forecast data"""
    headers = {
        "User-Agent": "MWCC"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    data = response.json()

    return data

def main():
    parser = argparse.ArgumentParser(
        description= "Get the weather forecast for your location"
    )

    parser.add_argument(
        "-l",
        "--Location",
        required=True,
        help="City and state to get the weather for"
    )

    parser.add_argument(
        "-d",
        "--detailed",
        action="store_true",
        help="Show detailed forecast"
    )

    parser.add_argument(
        "-w",
        "--week",
        action="store_true",
        help="Display the weekly forecast"
    )

    parser.add_argument(
        "-a",
        "--average",
        action="store_true",
        help="Display the average forecast for the week"
    )

    args = parser.parse_args()

    lat, lon = get_coordinates(args.Location)
    forecast_url = get_noaa_endpoint(lat, lon)
    forecast_data = get_noaa_forecast(forecast_url)
    periods = forecast_data["properties"]["periods"]

    print("\n" + "+" * 50)
    print(f"Weather Forecast for {args.Location.upper()}")
    print("+" * 50)

    if args.average:
        temperatures = []

        for period in periods:
            temperatures.append(period["temperature"])

        if temperatures:
            average = sum(temperatures) / len(temperatures)

            print(f"\nAverage forecast Temperature: {average:.1f}°F")
            print(f"based on {len(temperatures)} forecast periods")
        else:
            print("No temperature available")

    elif args.week:
        print("\nWeekly Forecast:")
        print("-" * 50)

        for period in periods[:14]:
            print(
                f"\n{period['name']}"
                f"{period['temperature']}°{period['temperatureUnit']}"
            )
            print(period["shortForecast"])

    elif args.detailed:
        period = periods[0]

        print(f"\n{period['name']}")
        print(
            f"Temperature: "
            f"{period['temperature']}°{period['temperatureUnit']}"
        )
        print(f"\n{period['shortForecast']}")
        print(f"\n{period['detailedForecast']}")

    else:
        period = periods[0]

        print(f"\n{period['name']}")
        print(
            f"Temperature: "
            f"{period['temperature']}°{period['temperatureUnit']}"
        )
        print(f"Forecast: {period['shortForecast']}")

    print("\n" + "+" * 50)

if __name__ == "__main__":
    main()