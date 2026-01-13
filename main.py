#  Install the Python Requests library:
# `pip install requests`
import requests
import os
from dotenv import load_dotenv
load_dotenv()
def send_request():
    response = requests.get(
        url="https://app.scrapingbee.com/api/v1/store/google",
        params={
            "api_key": os.getenv('SCRAPINGBEE_API_KEY'),
            "search": "the raja saab showtimes bengaluru",
          "country_code": "in",
          "language": "en"
        },

    )
    print('Response HTTP Status Code: ', response.status_code)
    print('Response HTTP Response Body: ', response.content)
send_request()

