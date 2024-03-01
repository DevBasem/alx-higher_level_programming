#!/usr/bin/python3
"""
Takes GitHub credentials (username and personal access token) and
uses the GitHub API to display the user id.
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    url = "https://api.github.com/user"

    # Use Basic Authentication with the personal access token as the password
    auth = (username, token)

    response = requests.get(url, auth=auth)

    try:
        user_info = response.json()
        user_id = user_info.get('id')
        print(user_id)
    except ValueError:
        print("None")
