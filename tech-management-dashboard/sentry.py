import requests
import os
def sentry_issues_all_cleared(displayed_project_name: str, sentry_url: str, org_slug: str, project_slug: str):
    metric_name = "[{project} production issues]({sentry_url}) all cleared".format(project=displayed_project_name, sentry_url=sentry_url)
    return (
        metric_name,
        len(
            requests.get(
                "https://sentry.io/api/0/projects/{org_slug}/{project_slug}/issues/".format(org_slug=org_slug, project_slug=project_slug),
                headers={
                    "Authorization": "Bearer {token}".format(token=os.environ["SENTRY_TOKEN"]) # https://stackoverflow.com/a/5971326
                }
            ).json()
        ) == 0
    )


if __name__ == "__main__":
    pass
