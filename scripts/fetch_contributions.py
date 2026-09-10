import requests
import json

USERNAME = "shubhamgupta002512"

url = f"https://github-contributions-api.jogruber.de/v4/{USERNAME}"

response = requests.get(url)
response.raise_for_status()

github_data = response.json()

contributions = []

for item in github_data["contributions"]:
    contributions.append({
        "date": item["date"],
        "level": item["level"]
    })

data = {
    "username": USERNAME,
    "contributions": contributions
}

with open("data/contributions.json", "w") as f:
    json.dump(data, f, indent=2)

print(f"Saved {len(contributions)} contribution days.")
