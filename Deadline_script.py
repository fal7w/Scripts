import requests
from datetime import datetime, date, timedelta

# GitHub API endpoint to get projects
url = "https://api.github.com/repos//users/fal7w/projects/2"


headers = {
  "Authorization": "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",
  "Accept": "application/vnd.github.inertia-preview+json"
}

# Send GET request to GitHub API
response = requests.get(url, headers=headers)
projects = response.json()

# Iterate over projects and check deadline
deadline_str = 'Oct 31, 2023'
deadline = datetime.strptime(deadline_str, '%b %d, %Y').date()
today = deadline - datetime.datetime.now().date()

if today == deadline:
  notify = True
else:
  notify = False

print(f"Notify: {notify}")
print(f"Today's Date: {now}")
print(f"Deadline: {deadline}")

# Set the output variable
print(f"::set-output name=notify::{notify}")
