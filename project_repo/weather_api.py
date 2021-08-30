# pylint: disable=missing-module-docstring

import sys
#import urllib.parse
import requests

BASE_URI = "https://www.metaweather.com"


def search_city(query):
    '''Look for a given city and disambiguate between several candidates.
    Return one city (or None)'''

    url = f"{BASE_URI}/api/location/search/?query={query}"
    response = requests.get(url).json()
    city = None
    if len(response) == 1:
        city = response[0]
    elif len(response) > 1:
        print(f"Please select one of the following:")
        queries = []
        for index, city in enumerate(response):
            queries.append(city["title"])
            print(f"{index + 1} - {city['title']}")
        index = int(input("Enter index: "))
        city = response[index - 1]
    return city


def weather_forecast(woeid):
    '''Return a 5-element list of weather forecast for a given woeid'''
    url = f"{BASE_URI}/api/location/{woeid}/"
    response = requests.get(url).json()
    forecast = response['consolidated_weather']
    return forecast


def main():
    '''Ask user for a city and display weather forecast'''
    query = input("City?\n> ")
    city = search_city(query)
    if city:
        query = city['title']
        woeid = city['woeid']
        print(f"Here's the weather in {query}")
        five_d_forecast = weather_forecast(woeid)
        for forecast in five_d_forecast:
            print(f"""{forecast['applicable_date']}:
                  {forecast['weather_state_name']}
                  {round(forecast['max_temp'],1)}°C""")
    return print("Sorry, city not found.")


if __name__ == '__main__':
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print('\nGoodbye!')
        sys.exit(0)
