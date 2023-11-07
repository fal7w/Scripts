import requests
from datetime import datetime,date,timedelta

# GitHub API endpoint to get projects
url = "https://api.github.com/repos//users/fal7w/projects/2"


headers = {
  "Authorization": "C6SwzYTFQzx5yleCtVT0snlmdLMjuZBtSd55j2VFinE",
  "Accept": "application/vnd.github.inertia-preview+json"
}

# Send GET request to GitHub API
response = requests.get(url, headers=headers)
projects = response.json()

# Iterate over projects and check deadline
deadline = datetime.date(2023, 11,5)
today = datetime.date.today()
if today == deadline:
  notify = True
else:
  notify = False

print(f"Notify: {notify}")
print(f"Today's Date: {today}")
print(f"Deadline: {deadline}")

# Set the output variable
print(f"::set-output name=notify::{notify}")
