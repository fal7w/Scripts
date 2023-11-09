from github import Github

# Replace with your GitHub personal access token
access_token = 'C6SwzYTFQzx5yleCtVT0snlmdLMjuZBtSd55j2VFinE'

# Replace with the URL of your GitHub repository
repository_url = 'https://github.com/fal7w/Scripts'

# Replace with the project number
project_number = 2

def print_card_status(card):
    print(f"Card Title: {card.note}")
    print(f"Card Status: {card.column.name}")
    print("-" * 50)

# Create a GitHub instance
g = Github(access_token)

# Get the repository
repo = g.get_repo(repository_url)

# Get the project
project = repo.get_project(project_number)

# Get all columns in the project
columns = project.get_columns()

# Iterate over each column
for column in columns:
    print(f"Column: {column.name}")
    print("-" * 50)

    # Get all cards in the column
    cards = column.get_cards()

    # Iterate over each card and print its status
    for card in cards:
        print_card_status(card)