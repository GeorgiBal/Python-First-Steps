import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get("https://forecast.weather.gov/MapClick.php?lat=34.09976000000006&lon=-118.33197499999994#.YXwb7p5Bw2w")
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id="seven-day-forecast-body")
items = week.find_all(class_='tombstone-container')

period_names = [item.find(class_='period-name').get_text() for item in items]
"""
Upper 'for' loop is the same as that:

period_names = []
for item in items:
    day = [item.find(class_='period-name').get_text()]
    period_names += day
"""
short_descriptions = [item.find(class_='short-desc').get_text() for item in items]
temperatures = [item.find(class_='temp').get_text() for item in items]

weather = pd.DataFrame(
    {
     'period': period_names,
     'short descriptions': short_descriptions,
     'temperatures': temperatures,
     }
)

weather.to_csv('weather.csv')
