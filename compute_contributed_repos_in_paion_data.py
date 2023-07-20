import requests
import datetime

ALL_ORG_PRS = "https://api.github.com/orgs/paion-data/repos"
PIN_TEMPLATE = "[![{repo_name}](https://github-readme-stats.vercel.app/api/pin/?username={owner}&repo={repo_name}&show_owner=true&theme=vue)](https://github.com/{owner}/{repo_name})"


def get_contributed_repos():
    contributed_repos = []

    repos = requests.get(url=ALL_ORG_PRS).json()

    for repo, contributors_url in {repo["full_name"]: repo["contributors_url"] for repo in repos}.items():
        contributors = requests.get(url=contributors_url).json()
        if "QubitPi" in [contributor["login"] for contributor in contributors]:
            contributed_repos.append(repo)

    f = open("contributed-paion-repos.txt", "w")
    f.write("\n".join([PIN_TEMPLATE.format(owner="paion-data", repo_name=contributed_repo.split("/")[1]) for contributed_repo in contributed_repos]))
    f.write("\n")
    f.close()
    
if __name__ == '__main__':
    get_contributed_repos()
