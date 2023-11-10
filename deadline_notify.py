import requests
from datetime import datetime
from smtplib import SMTP_SSL
from email.mime.text import MIMEText

# GitHub API endpoint
BASE_URL = "https://api.github.com"

# GitHub project information
OWNER = "fal7w"
REPO = "Scripts"

# Email configuration
# SMTP_HOST = "mail.fintechsys.net"
# SMTP_PORT = 465
# EMAIL_FROM = "github-actions@gmail.com"
# EMAIL_TO = "f.alfalahi@fintechsys.net"
# EMAIL_SUBJECT = "GitHub Project Status"

# GitHub personal access token
TOKEN = "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"

def get_project_status():
    url = f"{BASE_URL}/repos/{OWNER}/{REPO}/projects/2"
    headers = {"Authorization": f"Bearer {TOKEN}"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        projects = response.json()
        if projects:
            project = projects[0]  # Assuming the first project is the one of interest
            project_name = project["name"]
            project_url = project["html_url"]
            project_state = project["state"]
            project_created_at = project["created_at"]
            project_updated_at = project["updated_at"]

            status = f"Project: {project_name}\n"
            status += f"URL: {project_url}\n"
            status += f"State: {project_state}\n"
            status += f"Created at: {project_created_at}\n"
            status += f"Updated at: {project_updated_at}\n"

            return status

    return None

# def send_email_notification(content):
    message = MIMEText(content)
    message["Subject"] = EMAIL_SUBJECT
    message["From"] = EMAIL_FROM
    message["To"] = EMAIL_TO

    with SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(EMAIL_FROM, "your_email_password")
        server.send_message(message)

def main():
    project_status = get_project_status()
    # if project_status:
        # send_email_notification(project_status)
        # print("Notification sent successfully!")
    # else:
    #     print("Failed to retrieve project status.")

if __name__ == "__main__":
    main()



