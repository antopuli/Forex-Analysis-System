
import json
import requests
from datetime import datetime

d = datetime.now()
year = d.strftime("%Y")    
month = d.strftime("%m")
day = d.strftime("%d")
current_date = year + "-" + month + "-" + day


def showTodayExRate(source, currencies):

    toformat_url = "https://api.apilayer.com/currency_data/change?start_date={start_date}&end_date={end_date}&source={source}&currencies={currencies}"
    url = toformat_url.format(start_date=current_date, end_date=current_date, source=source, currencies=currencies)

    payload = {}
    headers= { "apikey": "79qZ0SUUHwRLdh1z3Wp2QolbNK9sFWY2" }

    response = requests.request("GET", url, headers=headers, data = payload)

    status_code = response.status_code
    result = response.text

    print(result)


def showExRateFromASpecificDateToToday(from_date, source, currencies):

    toformat_url = "https://api.apilayer.com/currency_data/change?start_date={start_date}&end_date={end_date}&source={source}&currencies={currencies}"
    url = toformat_url.format(start_date=from_date, end_date=current_date, source=source, currencies=currencies)

    payload = {}
    headers= { "apikey": "79qZ0SUUHwRLdh1z3Wp2QolbNK9sFWY2" }

    response = requests.request("GET", url, headers=headers, data=payload)

    status_code = response.status_code
    result = response.text

    print(result)


def convertAmountFromDifferentCurrencies(initial_c, final_c, amount):

    toformat_url = "https://api.apilayer.com/currency_data/convert?to={to}&from={from_c}&amount={amount}"

    url = toformat_url.format(to=final_c, from_c=initial_c, amount=amount)
    payload = {}
    headers = { "apikey": "79qZ0SUUHwRLdh1z3Wp2QolbNK9sFWY2" }

    response = requests.request("GET", url, headers=headers, data=payload)
    result = response.text

    jl = json.loads(result)

    res = final_c + " " + str(jl["result"])

    print(res)