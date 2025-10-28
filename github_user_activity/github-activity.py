"""
File: github-activity.py
Name: Zhi-Xiu Lin
-------------------------------
In this project, you will able to fetch the recent
activity of a GitHub user and display it in the terminal.
-------------------------------
Note.
- Please refer to README.md for the usage and detailed introduction
"""
import requests
import sys
from collections import defaultdict
from datetime import datetime, timezone

# global variable
summary = []

def generate_event_summary(events):
    # todo: add comment here
    global summary

    # Deal with events one by one
    for event in events:
        repo = event['repo']['name']
        type = event['type']
        payload = event.get('payload', {})

        # One-Time Event
        if type == "WatchEvent":
            summary.append(f"Starred {repo}")
        elif type == "ForkEvent": #todo: need sample and verify
            summary.append(f"Forked {repo}")
        elif type == "CreateEvent":
            ref_type = payload.get('ref_type')
            ref = payload.get('ref')
            summary.append(f"Created {ref_type} ({ref}) in {repo}")
        elif type == "DeleteEvent": 
            ref_type = payload.get('ref_type')
            ref = payload.get('ref')
            summary.append(f"Deleted {ref_type} ({ref}) in {repo}")
        elif type == "MemberEvent": #todo: need sample and verify
            pass
        elif type == "PublicEvent": #todo: need sample and verify
            pass




    #     if type == "IssuesEvent":
    #         action = payload.get('action')
    #         if action == "opened":
    #             summary.append(f"Opened a new issue in {repo}")
    #         elif action == "closed":
    #             summary.append(f"Closed an issue in {repo}")
    #     elif type == "PullRequestEvent":
    #         action = payload.get('action')
    #         if action == "opened":
    #             summary.append(f"Opened a pull request in {repo}")
    #         elif action == "closed":
    #             summary.append(f"Closed a pull request in {repo}")

    #     
    #     elif type == "PushEvent":
    #         summary.append(f"Pushed to {repo}")

    # 加上項目符號並輸出
    return [f"- {line}" for line in summary]

def fetch_user_events(username, token=None):
    """
    Fetch 30 user events by default w/ or w/o token provided.
    :param username: (str) the username to be queried
    :param token: (str) the content of the token
    :return: (list) the recent 30 events of user in json form
    """
    # todo: add more status code if exist
    error_code = {
        401: "Unauthorized – Your token may be missing or incorrect",
        404: "Not Found – The specified user does not exist"}

    url = f"https://api.github.com/users/{username}/events" # 30 events
    #url = f"https://api.github.com/users/{username}/events?page=1&per_page=100" # 100 events
    headers = {'Accept': 'application/vnd.github.v3+json'}  # Request for GitHub V3 output in json format
    if token:
        headers['Authorization'] = f'token {token}'
    response = requests.get(url, headers=headers)
    # Exception handling
    if response.status_code != 200:
        print(f"Event code: {response.status_code} ({error_code[response.status_code]})")
        return []
    return response.json()


def convert_to_local_time(utc_str):
    """
    Convert a UTC timestamp string from the GitHub API to the user's local time zone.
    :param utc_str: (str) the time stamp string from GitHub API
    :return: (str)the formatted timestamp string in the user's local time zone
    """
    # Convert time stamp string from GitHub API to datetime object
    utc_time = datetime.strptime(utc_str, "%Y-%m-%dT%H:%M:%SZ")
    # Specify the time stamp time zone which is UTC
    utc_time = utc_time.replace(tzinfo=timezone.utc)
    # Convert to user's system time zone
    local_time = utc_time.astimezone()
    # Return the time stamp string with desired format
    return local_time.strftime("%Y-%m-%d %H:%M")


def main():
    # todo: add comment here
    
    # Fetch user events from server and store to "events"(type: list)
    username = str(sys.argv[1])
    token = str(sys.argv[2]) if len(sys.argv) == 3 else None  # Default token will be none
    events = fetch_user_events(username, token)

    

    print("\n".join(generate_event_summary(events)))
    # print("Output:")
    # for line in push_summary + other_events:
    #     print(f"- {line}")


if __name__ == "__main__":
    main()

# todo: add time information(range) to the output
"""
timestamps = [
    "2025-10-27T14:05:00Z",
    "2025-10-27T18:30:00Z",
    "2025-10-26T22:15:00Z"
]

# 轉成 datetime 物件
dt_list = [datetime.strptime(t, "%Y-%m-%dT%H:%M:%SZ") for t in timestamps]

# 找最早與最晚
earliest = min(dt_list)
latest = max(dt_list)

print("最早事件時間：", earliest)
print("最晚事件時間：", latest)

"""