import os
import sys
import datetime
from dateutil.parser import parse
from github import Github
from github.GithubException import BadCredentialsException
from github.GithubException import UnknownObjectException
from github.GithubException import RateLimitExceededException


token = os.getenv("C6SwzYTFQzx5yleCtVT0snlmdLMjuZBtSd55j2VFinE")
repository_owner = os.getenv("fal7w")
repository_name = os.getenv("Scripts")

def get_project_data():
    try:
        g = Github(token)
        repo = g.get_repo(f"{repository_owner}/{repository_name}")
        projects = repo.get_projects(state="open")
        return projects
    except (BadCredentialsException, UnknownObjectException, RateLimitExceededException) as e:
        print(f"Error accessing repository: {str(e)}")
        sys.exit(1)

def notify_deadlines(projects):
    today = datetime.date.today()
    for project in projects:
        if project.updated_at.date() == today:
            print(f"Project '{project.name}' has a deadline today!")
        elif project.due_date and project.due_date.date() == today:
            print(f"Project '{project.name}' has a deadline today!")



if __name__ == "__main__":
    projects = get_project_data()
    notify_deadlines(projects)
