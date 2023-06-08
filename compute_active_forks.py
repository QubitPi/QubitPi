import requests
import datetime

NUM_ACTIVE_FORKS_TO_SHOW = 4
ALL_MY_PRS = "https://api.github.com/search/issues?q=merged:>{merged_after} author:QubitPi type:pr"
PIN_TEMPLATE = "[![{repo_name}](https://github-readme-stats.vercel.app/api/pin/?username=QubitPi&repo={repo_name}&show_owner=true&theme=vue)](https://github.com/QubitPi/{repo_name})"


def get_active_forks():
    today = datetime.date.today()
    five_days_ago = today - datetime.timedelta(days=5)

    prs = requests.get(url=ALL_MY_PRS.format(merged_after=five_days_ago)).json()["items"]

    repository_urls = list(set([pr["repository_url"] for pr in prs]))

    repo_names = []
    for repository_url in repository_urls:
        repo = requests.get(url=repository_url).json()
        if repo["fork"] is True and len(repo_names) < NUM_ACTIVE_FORKS_TO_SHOW:
            repo_names.append(repo["name"])

    active_forks = "\n".join([PIN_TEMPLATE.format(repo_name=repo_name) for repo_name in repo_names])

    f = open("temp.txt", "w")
    f.write(active_forks)
    f.write("\n")
    f.close()

    
if __name__ == '__main__':
    get_active_forks()
