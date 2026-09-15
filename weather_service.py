import os
import requests
from dotenv import load_dotenv

load_dotenv()

class WeatherServiceError(Exception):
    """
    Custom exception
    """
    pass

class WeatherService:

    @staticmethod
    def fetch_data(city: str) -> dict:

        api_key = os.getenv("WEATHER_API_KEY")

        if not api_key:
            raise WeatherServiceError("API key not found:\nPlease set WEATHER_API_KEY")

        if not city.strip():
            raise WeatherServiceError("Bad request:\nPlease enter a city name")

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            response = requests.get(url, timeout=10)        

            response.raise_for_status()

            return response.json()

        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    raise WeatherServiceError("Bad request:\nPlease check your input")

                case 401:
                    raise WeatherServiceError("Unauthorized:\nInvalid API key")

                case 403:
                    raise WeatherServiceError("Forbidden:\nAccess is denied")

                case 404:
                    raise WeatherServiceError("Not found:\nCity not found")

                case 500:
                    raise WeatherServiceError("Internal Server Error:\nPlease try again later")

                case 502:
                    raise WeatherServiceError("Bad gateway:\nInvalid response from the server")

                case 503:
                    raise WeatherServiceError("Service Unavailable:\nServer is down")

                case 504:
                    raise WeatherServiceError("Gateway Timeout:\nNo from the response server")

                case _:
                    raise WeatherServiceError(f"HTTP error occured:\n{http_error}")

        except requests.exceptions.ConnectionError:
            raise WeatherServiceError("Connection Error:\nCheck your internet connection")

        except requests.exceptions.Timeout:
            raise WeatherServiceError("Timeout Error:\nThe request timed out")

        except requests.exceptions.TooManyRedirects:
            raise WeatherServiceError("Too many Redirects:\nCheck the URL")
        
        except requests.exceptions.RequestException as req_error:
            raise WeatherServiceError(f"Request Error:\n{req_error}")