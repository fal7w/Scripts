import requests

def get_github_project_status(owner, repo, project_number, token):
    headers = {
        "Accept": "application/vnd.github.inertia-preview+json",
        "Authorization": f"Bearer {token}"
    }
    url = f"https://api.github.com/repos/{owner}/{repo}/projects/{project_number}"
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        project_data = response.json()
        return project_data["state"]
    else:
        return None

# Set your GitHub repository details and personal access token here
owner = "fal7w"
repo = "Scripts"
project_number = 2
token = "C6SwzYTFQzx5yleCtVT0snlmdLMjuZBtSd55j2VFinE"

status = get_github_project_status(owner, repo, project_number, token)
if status:
    print(f"The status of GitHub project {project_number} is: {status}")
else:
    print("Failed to retrieve project status.")