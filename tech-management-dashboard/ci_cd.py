import requests
from datetime import datetime, timedelta
from dateutil import parser

def latest_ci_cd_succeeded(org: str, repo: str, metric_name: str, ci_ci_file_name: str):
    today = datetime.today().strftime('%Y-%m-%d')
    seven_days_before_today = (datetime.today() - timedelta(days = 7)).strftime('%Y-%m-%d')

    runs = requests.get(
        "https://api.github.com/repos/{org}/{repo}/actions/workflows/{ci_ci_file_name}/runs".format(
            org=org,
            repo=repo,
            ci_ci_file_name=ci_ci_file_name
        ),
        params = {
            "exclude_pull_requests": "true",
            "branch": "master",
            "created": "{start}..{end}".format(start=seven_days_before_today, end=today)
        }
    ).json()

    sorted_runs = sorted(runs["workflow_runs"], key=lambda x: parser.parse(x['created_at']), reverse=True)
    latest_run = sorted_runs[0]

    return (metric_name, latest_run["conclusion"] == "success")

def sonar_quality_gate_passes(metric_name: str, project: str):
    # https://stackoverflow.com/a/68804543
    # https://stackoverflow.com/a/606199
    return (metric_name, "failed" not in requests.get(
        "https://sonarcloud.io/api/project_badges/measure?project={project}&metric=alert_status".format(project=project)
    ).content.decode("utf-8"))


if __name__ == "__main__":
   pass
