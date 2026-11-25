import unittest
from unittest.mock import patch, Mock

from weather import(
    get_coordinates,
    get_noaa_endpoint,
    get_noaa_forecast
)

class TestWeather(unittest.TestCase):

    @patch("weather.requests.get")
    def test_get_coordinates(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = [
            {
                "lat": "42.5748",
                "lon": "-71.9981"
            }
        ]
        mock_get.return_value = mock_response

        result = get_coordinates("Gardner, MA")
        self.assertEqual(result, (42.5748, -71.9981))

    @patch("weather.requests.get")
    def test_get_noaa_endpoint(self, mock_get):
        mock_response = Mock()

        mock_response.json.return_value = {
            "properties": {
                "forecast": "https://api.weather.gov/gridpoints/BOX/1,2/forecast"
            }
        }

        mock_get.return_value = mock_response
        result = get_noaa_endpoint(42.5748, -71.9981)
        self.assertEqual(
            result,
            "https://api.weather.gov/gridpoints/BOX/1,2/forecast"
        )
    @patch("Weather.requests.get")
    def test_get_noaa_forecast(self, mock_get):
        mock_response = Mock()

        mock_response.json.return_value = {
            "properties": {
                "periods": [
                    {
                        "name": "Tonight",
                        "temperature": 48,
                        "temperatureUnit": "F",
                        "shortForecast": "Clear"
                    }
                ]
            }
        }

        mock_get.return_value = mock_response

        result= get_noaa_forecast(
            "https://api.weather.gov/gridpoints/BOX/1,2/forecast"
        )

        self.assertEqual(
            result["properties"]["periods"][0]["temperature"],
            48
        )

        @patch("weather.requests.get")
        def test_get_coordinates_Location_not_found(self, mock_get):
            mock_response = Mock()
            mock_response.json.return_value = []
            mock_get.retrun_value = mock_response
            with self.assertRaises(ValueError):
                get_coordinates("Invalid City")

if __name__ == "__main__":
    unittest.main()