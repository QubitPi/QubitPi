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

import requests
from datetime import datetime, timedelta

MAX_NUM_ACTIVE_FORKS_TO_SHOW = 6
ALL_MY_PRS = "https://api.github.com/search/issues?q=merged:>{merged_after} author:QubitPi type:pr"
PIN_TEMPLATE = "[![{repo_name}](https://github-readme-stats.vercel.app/api/pin/?username={owner}&repo={repo_name}&show_owner=true&theme=ambient_gradient)](https://github.com/{owner}/{repo_name})"
ACTIVE_WINDOW_IN_HOURS = 24


def get_active_forks():
    retrospection_window = datetime.now() - timedelta(hours=ACTIVE_WINDOW_IN_HOURS)

    prs = requests.get(url=ALL_MY_PRS.format(merged_after=retrospection_window.strftime('%Y-%m-%dT%H:%M:%S'))).json()[
        "items"]

    repository_urls = list(set([pr["repository_url"] for pr in prs]))

    active_forks = {}
    for repository_url in repository_urls:
        repo = requests.get(url=repository_url).json()
        if repo["fork"] is True and len(active_forks) <= MAX_NUM_ACTIVE_FORKS_TO_SHOW:
            owner = repo["full_name"].split("/")[0]
            repo_name = repo["full_name"].split("/")[1]
            active_forks[repo_name] = owner

    if len(active_forks) == 0:
        active_forks = '''
<div align="center">
  <img src="https://github.com/QubitPi/QubitPi/blob/master/img/Madagascar%20Penguins.gif?raw=true" />
</div>
        '''
    else:
        active_forks = "\n".join(
            [PIN_TEMPLATE.format(owner=owner, repo_name=repo_name) for repo_name, owner in active_forks.items()])

    f = open("temp.txt", "w")
    f.write(active_forks)
    f.write("\n")
    f.close()


if __name__ == '__main__':
    get_active_forks()
