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

for element in soup.select("[data-date]"):
    contribution_date = element.get("data-date")

    level = element.get("data-level")

    if level is None:
        classes = element.get("class", [])
        level = 0

        for cls in classes:
            if cls.startswith("ContributionCalendar-day--"):
                try:
                    level = int(cls.split("--")[-1])
                except ValueError:
                    level = 0

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
