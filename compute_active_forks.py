import requests
import datetime

NUM_ACTIVE_FORKS_TO_SHOW = 4
ALL_MY_PRS = "https://api.github.com/search/issues?q=merged:>{merged_after} author:QubitPi type:pr"
PIN_TEMPLATE = "[![{repo_name}](https://github-readme-stats.vercel.app/api/pin/?username={owner}&repo={repo_name}&show_owner=true&theme=vue)](https://github.com/{owner}/{repo_name})"


def get_active_forks():
    today = datetime.date.today()
    five_days_ago = today - datetime.timedelta(days=5)

    prs = requests.get(url=ALL_MY_PRS.format(merged_after=five_days_ago)).json()["items"]

    repository_urls = list(set([pr["repository_url"] for pr in prs]))

    active_forks = {}
    for repository_url in repository_urls:
        repo = requests.get(url=repository_url).json()
        if repo["fork"] is True and len(active_forks) < NUM_ACTIVE_FORKS_TO_SHOW:
            owner = repo["full_name"].split("/")[0]
            repo_name = repo["full_name"].split("/")[1]
            active_forks[repo_name] = owner

    active_forks = "\n".join([PIN_TEMPLATE.format(owner=owner, repo_name=repo_name) for repo_name, owner in active_forks.items()])

    f = open("temp.txt", "w")
    f.write(active_forks)
    f.write("\n")
    f.close()

if __name__ == '__main__':
    get_active_forks()
