import requests

from nexusgraph import nexusgraph_npm_pacakge_version_follows_semantic_versioning_format
from ci_cd import latest_ci_cd_succeeded
from ci_cd import sonar_quality_gate_passes

def url_returns_200(metric_name: str, url: str):
    return ("Can visit [{metric_name}]({url})".format(metric_name=metric_name, url=url) , requests.get(url).status_code == 200)

if __name__ == "__main__":
    metircs = dict((metric, "✅" if status_ok else "❌") for metric, status_ok in (
        nexusgraph_npm_pacakge_version_follows_semantic_versioning_format(),

        latest_ci_cd_succeeded(
            "paion-data",
            "nexusgraph",
            "[Nexus Graph master CI/CD](https://github.com/paion-data/nexusgraph/actions/workflows/ci-cd.yml) passes",
            "ci-cd.yml"
        ),
        latest_ci_cd_succeeded(
            "paion-data",
            "prometheus",
            "[Prometheus master CI/CD](https://github.com/paion-data/prometheus/actions/workflows/ci-cd.yml) passes",
            "ci-cd.yml"
        ),

        sonar_quality_gate_passes(
            "[Nexus Graph Quality Gate](https://sonarcloud.io/summary/new_code?id=paion-data_nexusgraph) passes",
            "paion-data_nexusgraph"
        ),
        sonar_quality_gate_passes(
            "[Prometheus Quality Gate](https://sonarcloud.io/summary/new_code?id=paion-data_prometheus) passes",
            "paion-data_prometheus"
        ),

        url_returns_200("Theresa Machine Learning API", "https://theresa-api.com"),
        url_returns_200("Nexus Graph landing page", "https://nexusgraph.com/"),
        url_returns_200("Nexus Graph Doc", "https://paion-data.github.io/nexusgraph/"),
        url_returns_200("Nexus Graph API Doc", "https://paion-data.github.io/nexusgraph/api/"),
        url_returns_200("Paion Open Source", "https://paion-data.github.io/opensource.paion-data/"),
        url_returns_200("Paion Open Source Guide", "https://paion-data.github.io/opensource.guide/"),
        url_returns_200("Paion Artifactory", "https://nexus.paion-data.dev/")
    ))

    readme_lines = []

    with open("README.md", "r") as file:
        readme_lines = [line for line in file]

    with open("README.md", "w") as f:
        i = 0
        while i < len(readme_lines):
            line = readme_lines[i]
            f.write(line)
            if "<!-- TECH-MGMT-DASHBOARD:START -->" in line:
                for key, value in metircs.items():
                    f.write("- {key}: {value}\n".format(key=key, value=value))
                while "<!-- TECH-MGMT-DASHBOARD:END -->" not in readme_lines[i]:
                    i = i + 1
                f.write("<!-- TECH-MGMT-DASHBOARD:END -->\n")
            i = i + 1
