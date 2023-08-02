import requests

def nexusgraph_npm_pacakge_version_follows_semantic_versioning_format():
    """
    Valid version, for example, can be 0.1.124. Invalid versions include anything appended such as 0.1.123-1-G5F3GAR

    https://github.com/npm/registry/blob/master/docs/responses/package-metadata.md
    """

    metric_name = "[Nexus Graph NPM package](https://www.npmjs.com/package/@paiondata/nexusgraph) follows semantic versioning"

    return (metric_name, "-" not in requests.get("https://registry.npmjs.org/@paiondata/nexusgraph").json()["dist-tags"]["latest"])

if __name__ == "__main__":
   pass
