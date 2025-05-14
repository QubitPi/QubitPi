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
import os
import re
import sys
from git.exc import GitCommandError
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
    import argparse
    parser = argparse.ArgumentParser(description="Sync forks with rebase")
    parser.add_argument('-f', '--fork', help='Git URL of fork', required=True)
    parser.add_argument('-u', '--upstream', help='Git URL of upstream', required=True)
    parser.add_argument('-ub', '--upstream_default_branch', help='Default branch of upstream repo', required=True)
    args = vars(parser.parse_args())

    forked_repo = args["fork"]
    upstream_repo = args["upstream"]
    upstream_default_branch = args["upstream_default_branch"]

    forked_repo_name = get_repo_name_from_git_url(forked_repo)
    path = "./daily-sync/{}".format(forked_repo_name)

    if os.path.exists(path):
        print("./daily-sync/{} already exists".format(forked_repo_name))
        fork = Repo(path)
    else:
        print("Cloning {} ...".format(forked_repo))
        fork = Repo.clone_from(
            url=forked_repo,
            to_path=path,
            progress=CloneProgress()
        )
        fork.create_remote("upstream", upstream_repo)

    upstream_remote = fork.remotes.upstream
    fetch_info = upstream_remote.fetch()

    # check if upstram's default branch is equal to upstream_default_branch
    show_result = fork.git.remote("show", "upstream")
    matches = re.search(r"\s*HEAD branch:\s*(.*)", show_result)
    if matches:
        if upstream_default_branch != matches.group(1):
            sys.exit("{}'s default branch changes to {} in upstream".format(forked_repo_name, matches.group(1)))

    try:
        print("Rebasing ...")
        fork.git.rebase("upstream/{branch}".format(branch=upstream_default_branch))
    except GitCommandError as e:
        if "CONFLICT" in str(e):
            raise e
        else:
            raise e

    fork.remote("origin").push(refspec='master:master', force=True)
