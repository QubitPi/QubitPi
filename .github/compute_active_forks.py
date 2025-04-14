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


def get_active_forks():
    page = 1
    active_forks = {}
    while True:
        paged_forks = requests.get(url="https://api.github.com/users/QubitPi/repos?type=forks&page={page}&per_page=10".format(page=page)).json()
        if len(paged_forks) == 0:
            break
        for fork in paged_forks:
            if fork["fork"] == False:
                continue
            repo_owner = fork["full_name"].split("/")[0]
            repo_name = fork["full_name"].split("/")[1]
            last_commit = fork["updated_at"]
            if datetime.strptime(last_commit, "%Y-%m-%dT%H:%M:%SZ") > RETROSPECT_WINDOW_START:
                active_forks[repo_name] = repo_owner
        page = page + 1
    write_active_forks(active_forks)


if __name__ == '__main__':
    get_active_forks()
