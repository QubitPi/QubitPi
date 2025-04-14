# Copyright Jiaqi Liu
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import sys

import requests
from datetime import datetime, timedelta

MAX_NUM_ACTIVE_FORKS_TO_SHOW = 30
PIN_TEMPLATE = "[![{repo_name}](https://github-readme-stats.vercel.app/api/pin/?username={owner}&repo={repo_name}&show_owner=true&theme=ambient_gradient)](https://github.com/{owner}/{repo_name})"
ACTIVE_WINDOW_IN_HOURS = 24

RETROSPECT_WINDOW_START = datetime.now() - timedelta(hours=ACTIVE_WINDOW_IN_HOURS)


def write_active_forks(active_forks: dict[str, str]):
    if len(active_forks) == 0:
        active_forks = '''
<div align="center">
  <img src="https://github.com/QubitPi/QubitPi/blob/master/img/Madagascar%20Penguins.gif?raw=true" width="60%" />
</div>
            '''
    else:
        active_forks = "\n".join(
            [PIN_TEMPLATE.format(owner=owner, repo_name=repo_name) for repo_name, owner in active_forks.items()])

    f = open("temp.txt", "w")
    f.write(active_forks)
    f.write("\n")
    f.close()

def based_on_push_events():
    qubitpi_events = "https://api.github.com/users/QubitPi/events?page={page}&per_page=10&sort=created&direction=desc"

    page = 1
    active_forks = {}
    while True:
        events = [event for event in requests.get(url=qubitpi_events.format(page=page)).json() if event["actor"]["login"] == "QubitPi"]
        for event in events:
            repo = event["repo"]["name"]
            repo_owner = repo.split("/")[0]
            repo_name = repo.split("/")[1]

            if repo_name in active_forks:
                continue

            if datetime.strptime(event["created_at"], "%Y-%m-%dT%H:%M:%SZ") > RETROSPECT_WINDOW_START:
                response = requests.get("https://api.github.com/repos/{OWNER_SLASH_REPO}".format(OWNER_SLASH_REPO=repo))
                if "fork" in response.json && response.json()["fork"]:
                    active_forks[repo_name] = repo_owner
            else:
                write_active_forks(active_forks)
                exit(0)

            if len(active_forks) >= MAX_NUM_ACTIVE_FORKS_TO_SHOW:
                write_active_forks(active_forks)
                exit(0)
        page = page + 1


def based_on_pr():
    qubitpi_prs = "https://api.github.com/search/issues?q=merged:>{merged_after} author:QubitPi type:pr"

    prs = requests.get(url=qubitpi_prs.format(merged_after=RETROSPECT_WINDOW_START.strftime('%Y-%m-%dT%H:%M:%S'))).json()["items"]

    repository_urls = list(set([pr["repository_url"] for pr in prs]))

    active_forks = {}
    for repository_url in repository_urls:
        repo = requests.get(url=repository_url).json()
        if repo["fork"] is True and len(active_forks) <= MAX_NUM_ACTIVE_FORKS_TO_SHOW:
            owner = repo["full_name"].split("/")[0]
            repo_name = repo["full_name"].split("/")[1]
            active_forks[repo_name] = owner

    write_active_forks(active_forks)


def get_active_forks():
    based_on_push_events()


if __name__ == '__main__':
    get_active_forks()
