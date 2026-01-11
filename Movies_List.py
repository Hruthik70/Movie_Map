import requests
from datetime import datetime, timezone
from dotenv import load_dotenv
import os
load_dotenv()

headers = {
    "client": os.getenv("MOVIEGLU_CLIENT"),
    "x-api-key": os.getenv("MOVIEGLU_API_KEY"),
    "authorization": os.getenv("MOVIEGLU_AUTH"),
    "territory": "IN",
    "api-version": "v201",
    "geolocation": "12.9716;77.5946",
    "device-datetime": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ")
}
params =\
    {
    "n": 10
}
api_url = "https://api-gate2.movieglu.com/filmsNowShowing/"
response = requests.get(api_url, headers=headers, params=params)
data = response.json()


showtime_header = {
    "geolocation": "12.9716;77.5946"
}

params_showtime = {"n":10, "film_id":"356186", "date":"2026-01-11"}
show_time_url = "https://api-gate2.movieglu.com/filmShowTimes/"
response_showtime = requests.get(show_time_url, headers=headers, params=params)


#Makes a list of the movies available
movies_list = []
for film in data.get("films", []):
    movies_list.append(film.get("film_name"))
print(movies_list)
print(data)

