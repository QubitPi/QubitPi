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
from git import Repo, RemoteProgress
from tqdm import tqdm

# Credits to https://stackoverflow.com/a/65576165
class CloneProgress(RemoteProgress):
    def __init__(self):
        super().__init__()
        self.pbar = tqdm()

    def update(self, op_code, cur_count, max_count=None, message=''):
        self.pbar.total = max_count
        self.pbar.n = cur_count
        self.pbar.refresh()


def get_repo_name_from_git_url(url: str) -> str:
    """
    Credits to https://stackoverflow.com/a/55137835
    """
    last_slash_index = url.rfind("/")
    last_suffix_index = url.rfind(".git")
    if last_suffix_index < 0:
        last_suffix_index = len(url)

    if last_slash_index < 0 or last_suffix_index <= last_slash_index:
        raise Exception("Badly formatted url {}".format(url))

    return url[last_slash_index + 1:last_suffix_index]


if __name__ == "__main__":
    sync_configs = [
        ("git@github.com:QubitPi/mlflow.git", "git@github.com:mlflow/mlflow.git", "upstream/master", "https://github.com/QubitPi/mlflow"),
    ]

    failed_forks = []

    for sync_config in sync_configs:
        forked_repo = sync_config[0]
        upstream_repo = sync_config[1]
        rebase_branch = sync_config[2]
        repo_url = sync_config[3]

        print("Cloning {} ...".format(forked_repo))
        fork = Repo.clone_from(
            url=forked_repo,
            to_path="./daily-sync/{}".format(get_repo_name_from_git_url(forked_repo)),
            progress=CloneProgress()
        )

        fork.create_remote("upstream", upstream_repo) # https://gitpython.readthedocs.io/en/stable/tutorial.html#handling-remotes
        upstream_remote = fork.remotes.upstream
        fetch_info = upstream_remote.fetch()

        try:
            fork.git.rebase(rebase_branch)
        except fork.git.GitCommandError as e:
            if "CONFLICT" in str(e):
                failed_forks.append(repo_url)
            else:
                raise e

        f = open("temp.txt", "w")
        if len(failed_forks) > 0:
            f.write("The following forks failed to sync with upstream and requires immediate attention: \n")
            f.write("\n".join(["- [{repo_name}]({repo_url})".format(repo_name=get_repo_name_from_git_url(forked_repo), repo_url=repo_url) for failed_fork in failed_forks]))
        f.close()
