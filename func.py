
import requests
from datetime import datetime


def showTodayExRate(source, currencies):

    d = datetime.now()
    year = d.strftime("%Y")
    month = d.strftime("%m")
    day = d.strftime("%d")
    current_date = year + "-" + month + "-" + day

    toformat_url = "https://api.apilayer.com/currency_data/change?start_date={start_date}&end_date={end_date}&source={source}&currencies={currencies}"
    url = toformat_url.format(start_date=current_date, end_date=current_date, source=source, currencies=currencies)

    payload = {}
    headers= { "apikey": "79qZ0SUUHwRLdh1z3Wp2QolbNK9sFWY2" }

    response = requests.request("GET", url, headers=headers, data = payload)

    status_code = response.status_code
    result = response.text

    print(result)

    