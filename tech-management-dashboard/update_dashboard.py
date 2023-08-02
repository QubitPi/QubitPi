from nexusgraph import nexusgraph_npm_pacakge_version_follows_semantic_versioning_format
from nexusgraph import nexusgraph_latest_ci_cd_succeeded


if __name__ == "__main__":
    metircs = dict((metric, "✅" if status_ok else "❌") for metric, status_ok in (
        nexusgraph_npm_pacakge_version_follows_semantic_versioning_format(),
        nexusgraph_latest_ci_cd_succeeded()
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
