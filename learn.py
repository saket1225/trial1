import git

# Path to your local repository
repo_path = 'clone/'

# Load the repository
repo = git.Repo(repo_path)

# Fetch changes from the remote named 'origin'
origin = repo.remotes.origin
origin.fetch()

# Pull changes from the remote
origin.pull()
print(origin)
