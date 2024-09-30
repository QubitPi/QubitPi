GitHub Management <sup>![Python Version Badge is Missing](https://img.shields.io/badge/Python-3.10-brightgreen?style=flat-square&logo=python&logoColor=white)</sup>
=================

Scripts
-------

### Setup

1. Install Python GraphQL client library: `pip3 install "gql[all]"`
2. `git clone https://github.com/QubitPi/QubitPi.git`
3. `cd QubitPi/create-repo-labels`
4. [Create a GitHub token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)
   with the following scrope

   ![Error loading scope.png](./scope.png)

5. Make the token an OS environment variable with

  ```bash
  export GITHUB_MANAGEMENT_TOKEN=ghp_MyTygnyo0HHsdfewf2efqwf34dwee1f82pp1pu
  ```

6. You are all set!

### Managing Repo Labels

This script refresh a GitHub repo with [most up-to-date labels](./github-labels.json):

```bash
python3 managing-repo-labels.py -h
python3 managing-repo-labels.py -o QubitPi -r my-repo
```

License
-------

The use and distribution terms for [github-management](https://github.com/QubitPi/github-management) are covered by the
[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0).

[Apache License, Version 2.0]: http://www.apache.org/licenses/LICENSE-2.0.html
