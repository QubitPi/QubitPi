import json
import requests

def main():
    all_public_repos = requests.get(url="https://api.github.com/users/QubitPi/repos").json()
    names = [repo["name"] for repo in all_public_repos]

    f = open("config.json", "w")
    f.write(json.dumps({
        "devMode": "false",
        "advancedMode": "false",
        "language": "en-US",
        "repository": names
    }))
    f.write("\n")
    f.close()

    
if __name__ == '__main__':
    main()
