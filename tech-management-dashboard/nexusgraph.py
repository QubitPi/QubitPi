import requests

def npm_pacakge_version_follows_semantic_versioning_format():
    """
    Valid version, for example, can be 0.1.124. Invalid versions include anything appended such as 0.1.123-1-G5F3GAR
    :return:
    """
    # https://github.com/npm/registry/blob/master/docs/responses/package-metadata.md
    return "-" not in requests.get("https://registry.npmjs.org/@paiondata/nexusgraph").json()["dist-tags"]["latest"]


if __name__ == "__main__":
   pass
