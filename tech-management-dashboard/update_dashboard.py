from nexusgraph import npm_pacakge_version_follows_semantic_versioning_format

if __name__ == "__main__":
    metircs = {}

    if npm_pacakge_version_follows_semantic_versioning_format():
        metircs["- Nexus Graph NPM package follows semantic versioning"] = "✅"
    else:
        metircs["- Nexus Graph NPM package follows semantic versioning"] = "❌"

    readme_lines = []

    with open("../README.md", "r") as file:
        readme_lines = [line for line in file]

    with open("../README.md", "w") as f:
        for line in readme_lines:
            f.write(line)
            if "<!-- TECH-MGMT-DASHBOARD:START -->" in line:
                for key, value in metircs.items():
                    f.write("{key}: {value}\n".format(key=key, value=value))
