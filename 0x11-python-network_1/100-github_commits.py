#!/usr/bin/python3
"""posts data to star wars api
"""
if __name__ == "__main__":
    import requests
    import sys
    import json
    repo_owner = sys.argv[2]
    repo_name = sys.argv[1]
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits"
    response = requests.get(url)
    result = response.json()
    try:
        for i in range(10):
            print(f"{result[i].get('sha')}: ", end="")
            print(result[i]["commit"]["author"]["name"])
    except IndexError:
        pass
