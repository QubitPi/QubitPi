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
import argparse
import json
import os
import requests

from gql import Client
from gql import gql
from gql.transport.aiohttp import AIOHTTPTransport

transport = AIOHTTPTransport(
    url="https://api.github.com/graphql",
    headers={"Authorization": "Bearer " + os.environ['GITHUB_MANAGEMENT_TOKEN']}
)
client = Client(transport=transport, fetch_schema_from_transport=True)


def _graphql_result_is_empty(results):
    return len(results["connectionType"]["fields"]["edges"]) == 0


def _graphql_paginated_query(repo_owner: str, repo_name: str, query_filename: str, callback, *args):
    """

    :param repo_owner:
    :param repo_name:
    :param query_filename: the query, since it's paginated, follows
    `GraphQL Cursor Connections Specification <https://qubitpi.github.io/relay/graphql/connections.htm>`_ and must be
    of the form::

        query getRepoLabels($repo_owner: String!, $repo_name: String! $after: String) {
          connectionType: selection1(owner: $repo_owner, name: $repo_name) {
            fields: selection2(first: 100, after: $after) {
              edges {
                node {
                  ...
                }
                cursor
              }
              pageInfo {
                hasNextPage
              }
            }
          }
        }

    :param callback:
    :param args:
    :return:
    """
    query_results = []
    hasNextPage: bool = True
    after: str = None
    while hasNextPage:
        with open(f"graphql/{query_filename}", 'r') as file:
            query = gql(file.read())
        results = client.execute(
            query,
            variable_values={"repo_owner": repo_owner, "repo_name": repo_name, "after": after}
        )

        if _graphql_result_is_empty(results):
            return query_results

        connections = results["connectionType"]["fields"]["edges"]

        for result in [connection["node"] for connection in connections]:
            query_results.append(callback(result))

        hasNextPage = results["connectionType"]["fields"]["pageInfo"]["hasNextPage"]
        after = connections[len(connections) - 1]["cursor"]

    return query_results


def _get_repo_labels(repo_owner: str, repo_name: str) -> list:
    return _graphql_paginated_query(
        repo_owner,
        repo_name,
        "get-repo-labels.graphql",
        lambda result: { "id": result["id"], "name": result["name"] }
    )


def _get_repo_prs(repo_owner: str, repo_name: str) -> list:
    return _graphql_paginated_query(
        repo_owner,
        repo_name,
        "get-repo-prs.graphql",
        lambda result: {
            "id": result["id"],
            "number": result["number"],
            "labels": [label_conn["node"]["name"] for label_conn in result["labels"]["edges"]]
        }
    )

def _attach_labels_to_pr(pr_id: str, label_ids: list[str]):
    with open("graphql/attach-labels-to-pr.graphql", 'r') as file:
        query = gql(file.read())
    client.execute(
        query,
        variable_values={
            "args": {
                "labelableId": pr_id,
                "labelIds": label_ids
            }
        }
    )

def _delete_repo_labels(repo_owner: str, repo_name: str) -> None:
    """
    Apparently there is no GraphQL endpoint for deleting a label... o_O
    :param repo_owner:
    :param repo_name:
    """
    headers = {
        'Accept': 'application/vnd.github+json',
        "Authorization": "Bearer " + os.environ['GITHUB_MANAGEMENT_TOKEN']
    }

    url = "https://api.github.com/repos/{repo_owner}/{repo_name}/labels".format(repo_owner=repo_owner, repo_name=repo_name)
    for label_url in [label["url"] for label in requests.get(url, headers=headers).json()]:
        requests.delete(label_url, headers=headers)

def _create_repo_labels(repo_owner: str, repo_name: str, label_to_color: dict[str, str]) -> None:
    """
    Apparently there is no GraphQL endpoint for creating a label... o_O

    :param repo_owner:
    :param repo_name:
    """
    headers = {
        'Accept': 'application/vnd.github+json',
        "Authorization": "Bearer " + os.environ['GITHUB_MANAGEMENT_TOKEN']
    }

    for label, color in label_to_color.items():
        requests.post(
            f"https://api.github.com/repos/{repo_owner}/{repo_name}/labels",
            headers=headers,
            data=json.dumps(
                {
                    "name": label,
                    "color": color
                }
            )
        )

if __name__ == '__main__':
    # https://stackoverflow.com/a/7427376
    parser = argparse.ArgumentParser(description="Managing repository labels")
    parser.add_argument('-o', '--owner', help='Repository owner', required=True)
    parser.add_argument('-r', '--repo', help='Repository name', required=True)
    args = vars(parser.parse_args())

    repo_owner = args["owner"]
    repo_name = args["repo"]

    backup = _get_repo_prs(repo_owner, repo_name)
    with open("repo_pr.backup", 'w') as file:
        file.write(json.dumps(backup, indent=4))
    print(f"Existing PR labels of {repo_owner}/{repo_name} have been backed up to repo_pr.backup")

    _delete_repo_labels(repo_owner, repo_name)
    print(f"All {repo_owner}/{repo_name} labels have been deleted")

    all_updated_labels: dict[str, str] = {}
    with open('github-labels.json') as json_file:
        file_content = json.load(json_file)
        for key in file_content:
            all_updated_labels[key] = file_content[key]
    _create_repo_labels(repo_owner, repo_name, all_updated_labels)

    repo_labels = {label["name"]: label["id"] for label in _get_repo_labels(repo_owner, repo_name)}

    for pr in backup:
        new_label_ids = []
        for label in pr["labels"]:
            if label in all_updated_labels.keys():
                new_label_ids.append(repo_labels[label])
        _attach_labels_to_pr(pr["id"], new_label_ids)

