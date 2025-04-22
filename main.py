import requests
import pandas as pd
import psycopg2
import json

API_TOKEN = '40de67c3cbfe447493e2a4fcf1a54724'
headers = { 'X-Auth-Token': API_TOKEN }
url = 'https://api.football-data.org/v4/competitions/PL/matches?season=2023'

response = requests.get(url, headers=headers)
data = response.json()

print(data.keys())

with open("raw_matches.json", "w") as f:
    json.dump(data, f, indent=4)