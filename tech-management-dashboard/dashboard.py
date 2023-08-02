from nexusgraph import npm_pacakge_version_follows_semantic_versioning_format

if __name__ == "__main__":
    metircs = {}

    if npm_pacakge_version_follows_semantic_versioning_format():
        metircs["- Nexus Graph NPM package follows semantic versioning"] = "✅"
    else:
        metircs["- Nexus Graph NPM package follows semantic versioning"] = "❌"

    with open("temp.txt", "w") as f:
        for key, value in metircs.items():
            f.write("{key}: {value}\n".format(key=key, value=value))
