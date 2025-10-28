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
from datetime import datetime, timezone

# global variable
summary = [] # Use to stored summarized event data
tmp_dict = {} # Use to deal with cumulative events

def one_time_event(event):
    #todo: add comment here
    # event: dict
    global summary
    repo = event['repo']['name']
    type = event['type']
    payload = event.get('payload', {})

    # Judge Event Type and Add to summary
    if type == "WatchEvent":
        summary.append(f"Starred {repo}.")
    elif type == "ForkEvent":  #todo: need sample and verify
        summary.append(f"Forked {repo}.") 
    elif type == "CreateEvent":
        ref_type = payload.get('ref_type')
        ref = payload.get('ref')
        summary.append(f"Created {ref_type} ({ref}) in {repo}.")
    elif type == "DeleteEvent": 
        ref_type = payload.get('ref_type')
        ref = payload.get('ref')
        summary.append(f"Deleted {ref_type} ({ref}) in {repo}.")
    elif type == "MemberEvent": #todo: need sample and verify
        action = payload.get('action')
        member = payload.get("member",{}).get("login")
        if action =="added" and member:
            summary.append(f"Added {member} as a collaborator in {repo}.")
    elif type == "PublicEvent": #todo: need sample and verify
        summary.append(f"Made {repo} public.")

def cumulative_event(event):
    #todo: add comment here
    # event: dict
    global summary, tmp_dict
    repo = event['repo']['name']
    type = event['type']
    payload = event.get('payload', {})
    if type == "PushEvent":
        tmp_dict[(type, repo)] = tmp_dict.get((type, repo), 0) + 1
    elif type in ["IssuesEvent","PullRequestEvent"]:
        action = payload.get('action')
        if action in ["opened","closed"]:
            tmp_dict[(type, action, repo)] = tmp_dict.get((type, action, repo), 0) + 1
    elif type == "IssueCommentEvent":
        action = payload.get('action')
        if action in ["created","deleted"]:
            tmp_dict[(type, action, repo)] = tmp_dict.get((type, action, repo), 0) + 1




def generate_event_summary(events):
    # todo: add comment here
    global summary, tmp_dict

    # Deal with events one by one
    for event in events:
        if event['type'] in ["WatchEvent","ForkEvent","CreateEvent","DeleteEvent","MemberEvent","PublicEvent"]:
            one_time_event(event)
        elif event['type'] in ["PushEvent","PullRequestEvent","IssuesEvent","IssueCommentEvent"]:
            cumulative_event(event)
    
    # Append cumulative event information to summary
    for key, val in tmp_dict.items():
        if key[0] == "PushEvent":
            summary.append(f"Pushed {val} commit(s) to {key[1]}.")
        elif key[0] == "PullRequestEvent":
            summary.append(f"{'Opened' if key[1]=='opened' else 'Closed'} {val} pull request(s) in {key[2]}.")
        elif key[0] == "IssuesEvent":
            summary.append(f"{'Opened' if key[1]=='opened' else 'Closed'} {val} issue(s) in {key[2]}.")
        elif key[0] == "IssueCommentEvent":
            summary.append(f"{'Created' if key[1]=='created' else 'Deleted'} {val} comment(s) in {key[2]} issue(s).")



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

    #url = f"https://api.github.com/users/{username}/events" # 30 events
    url = f"https://api.github.com/users/{username}/events?page=1&per_page=100" # 100 events(page 1)
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
    generate_event_summary(events)

    print("\n".join(summary))


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