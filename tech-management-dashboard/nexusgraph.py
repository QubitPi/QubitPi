import requests
from datetime import datetime, timedelta
from dateutil import parser


def nexusgraph_npm_pacakge_version_follows_semantic_versioning_format():
    """
    Valid version, for example, can be 0.1.124. Invalid versions include anything appended such as 0.1.123-1-G5F3GAR

    https://github.com/npm/registry/blob/master/docs/responses/package-metadata.md
    """

    metric_name = "[Nexus Graph NPM package](https://www.npmjs.com/package/@paiondata/nexusgraph) follows semantic versioning"

    return (metric_name, "-" not in requests.get("https://registry.npmjs.org/@paiondata/nexusgraph").json()["dist-tags"]["latest"])


def nexusgraph_latest_ci_cd_succeeded():
    metric_name = "[Nexus Graph master CI/CD](https://github.com/paion-data/nexusgraph/actions/workflows/ci-cd.yml)"

    today = datetime.today().strftime('%Y-%m-%d')
    seven_days_before_today = (datetime.today() - timedelta(days = 7)).strftime('%Y-%m-%d')

    runs = requests.get(
        "https://api.github.com/repos/paion-data/nexusgraph/actions/workflows/ci-cd.yml/runs",
        params = {
            "exclude_pull_requests": "true",
            "branch": "master",
            "created": "{start}..{end}".format(start=seven_days_before_today, end=today)
        }
    ).json()

    sorted_runs = sorted(runs["workflow_runs"], key=lambda x: parser.parse(x['created_at']), reverse=True)
    latest_run = sorted_runs[0]

    return (metric_name, latest_run["conclusion"] == "success")


def nexusgraph_sonar_quality_gate_passes():
    metric_name = "[Nexus Graph Quality Gate](https://sonarcloud.io/summary/new_code?id=paion-data_nexusgraph)"

    # https://stackoverflow.com/a/68804543
    # https://stackoverflow.com/a/606199
    return (metric_name, "failed" not in requests.get("https://sonarcloud.io/api/project_badges/measure?project=paion-data_nexusgraph&metric=alert_status").content.decode("utf-8"))

if __name__ == "__main__":
   pass
