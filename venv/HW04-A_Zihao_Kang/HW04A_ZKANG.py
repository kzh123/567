"""
Using Web API's and JSON
@author:10456094
"""
import json
import urllib.error
import urllib.request


def repo(username):
    result = []
    """result will be saved as a list of string"""
    path_all_repo = "https://api.github.com/users/" + username + "/repos"
    """API request path"""
    try:
        all_repo = urllib.request.urlopen(path_all_repo).read()
    except urllib.error.HTTPError:
        print("Page not found")

    else:
        data = json.loads(all_repo)
        repo_list = []
        """save the name of each repo"""
        for repo_item in data:
            repo_list.append(repo_item["name"])

        for name in repo_list:
            path_repo = "https://api.github.com/repos/" + username + "/" + name + "/commits"
            repo_commit = urllib.request.urlopen(path_repo).read()
            repo_commit_json = json.loads(repo_commit)
            result.append(f"Repo: {name} Number of commits: {len(repo_commit_json)}")

        return result


if __name__ == '__main__':
    # user = input("Please input username")
    result_me = repo("richkempinski")
    print(result_me)
    for item in result_me:

        print(item)
