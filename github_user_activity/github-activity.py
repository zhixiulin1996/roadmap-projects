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
import urllib.request
import json
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
        summary.append(f"- Starred {repo}.")
    elif type == "ForkEvent":
        summary.append(f"- Forked {repo}.") 
    elif type == "CreateEvent":
        ref_type = payload.get('ref_type')
        ref = payload.get('ref')
        summary.append(f"- Created {ref_type} ({ref}) in {repo}.")
    elif type == "DeleteEvent": 
        ref_type = payload.get('ref_type')
        ref = payload.get('ref')
        summary.append(f"- Deleted {ref_type} ({ref}) in {repo}.")
    elif type == "MemberEvent":
        action = payload.get('action')
        member = payload.get("member",{}).get("login")
        if action =="added" and member:
            summary.append(f"- Added {member} as a collaborator in {repo}.")
    elif type == "PublicEvent":
        summary.append(f"- Made {repo} public.")

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
            summary.append(f"- Pushed {val} commit(s) to {key[1]}.")
        elif key[0] == "PullRequestEvent":
            summary.append(f"- {'Opened' if key[1]=='opened' else 'Closed'} {val} pull request(s) in {key[2]}.")
        elif key[0] == "IssuesEvent":
            summary.append(f"- {'Opened' if key[1]=='opened' else 'Closed'} {val} issue(s) in {key[2]}.")
        elif key[0] == "IssueCommentEvent":
            summary.append(f"- {'Created' if key[1]=='created' else 'Deleted'} {val} comment(s) in {key[2]} issue(s).")



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

    # Data required to send HTTP request
    #url = f"https://api.github.com/users/{username}/events" # 30 events
    url = f"https://api.github.com/users/{username}/events?page=1&per_page=100" # 100 events(page 1)
    headers = {"Accept": "application/vnd.github.v3+json","User-Agent": "Python-urllib"}
    if token:
        headers["Authorization"] = f"token {token}"

    # Send http request
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            data = response.read()
            return json.loads(data)
    except urllib.error.HTTPError as e:
        code = e.code
        message = error_code.get(code, f"HTTP Error {code}") #if code is not in dictionary, return formatted string
        print(f"Event code: {code} ({message})")
        return []
    except urllib.error.URLError as e:
        print(f"URL Error: {e.reason}")
        return []
    

def find_time_range(events):
    """
    1. Iterate through the events find the max/min time stamp of these events 
    2. Convert them to user's local time zone
    :param events: (list) the recent 30 events of user in json form
    :return: (list) the min/max time stamp string from GitHub API in user's time zone
    """
    time_stamp = []
    dt_list = []
    for event in events:
        time_stamp.append(event['created_at'])
    
    for utc_str in time_stamp:
        # Convert time stamp string to datetime object
        utc_time = datetime.strptime(utc_str, "%Y-%m-%dT%H:%M:%SZ")
        # Specify the time stamp time zone which is UTC
        utc_time = utc_time.replace(tzinfo=timezone.utc)
        # Convert to user's system time zone
        local_time = utc_time.astimezone()
        # Formatted
        formatted = local_time.strftime("%Y-%m-%d %H:%M (UTC%z)")
        dt_list.append(formatted)

    return [min(dt_list),max(dt_list)]

def main():
    # todo: add comment here
    
    # Fetch user events from server and store to "events"(type: list)
    username = str(sys.argv[1])
    token = str(sys.argv[2]) if len(sys.argv) == 3 else None  # Default token will be none
    events = fetch_user_events(username, token)
    generate_event_summary(events)
    
    if summary:
        # Time range
        time_range = find_time_range(events) 
        # Output  
        print(f"[Time Range] From {time_range[0]} To {time_range[1]}")
        print(f"[Fetched User] {username}")
        print("[Output]")
        print("\n".join(summary))


if __name__ == "__main__":
    main()
