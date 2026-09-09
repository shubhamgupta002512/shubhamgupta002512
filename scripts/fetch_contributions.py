import requests
from bs4 import BeautifulSoup
import json
from datetime import date, timedelta

USERNAME = "shubhamgupta002512"

today = date.today()
start = today - timedelta(days=364)

url = f"https://github.com/users/{USERNAME}/contributions?from={start}&to={today}"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

contributions = []

for rect in soup.select("td[data-date]"):
    contribution_date = rect.get("data-date")
    level = rect.get("data-level", "0")

    contributions.append({
        "date": contribution_date,
        "level": int(level)
    })

data = {
    "username": USERNAME,
    "contributions": contributions
}

with open("data/contributions.json", "w") as f:
    json.dump(data, f, indent=2)

print(f"Saved {len(contributions)} contribution days.")
