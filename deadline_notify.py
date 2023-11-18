from github import Github

access_token = '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'

g = Github(access_token)

# Repository information
repo_owner = 'fal7w'
repo_name = 'Scripts'

project_number = 2  

repo = g.get_repo(f'{repo_owner}/{repo_name}')

project = repo.get_project(project_number)

columns = project.get_columns()

# Iterate over the columns
for column in columns:
    print(f"Column: {column.name}")
    print("Issues:")
    cards = column.get_cards()
    for card in cards:
        issue = card.get_content()
        status = 'Todo' if issue.state == 'open' else 'Done' if issue.state == 'closed' else 'In progress'
        print(f"Issue: {issue.title} - Status: {status}")
    print()
