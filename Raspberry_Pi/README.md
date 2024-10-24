# Clone a repository from a specific org
$ gh repo clone cli/cli

# Clone a repository from your own account
$ gh repo clone myrepo

# Clone a repo, overriding git protocol configuration
$ gh repo clone https://github.com/cli/cli
$ gh repo clone git@github.com:cli/cli.git

# Clone a repository to a custom directory
$ gh repo clone cli/cli workspace/cli

# Clone a repository with additional git clone flags
$ gh repo clone cli/cli -- --depth=1



gh repo add
gh repo commit
gh repo push
gh pr status