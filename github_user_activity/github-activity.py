#todo: add comment here
import requests
import sys
from collections import defaultdict

# 整理非 PushEvent 類型
def format_event(event):
    repo = event['repo']['name']
    type = event['type']
    payload = event.get('payload', {})

    if type == "IssuesEvent":
        action = payload.get('action')
        if action == "opened":
            return f"Opened a new issue in {repo}"
        elif action == "closed":
            return f"Closed an issue in {repo}"
    elif type == "PullRequestEvent":
        action = payload.get('action')
        if action == "opened":
            return f"Opened a pull request in {repo}"
        elif action == "closed":
            return f"Closed a pull request in {repo}"
    elif type == "WatchEvent":
        return f"Starred {repo}"
    elif type == "ForkEvent":
        return f"Forked {repo}"
    elif type == "CreateEvent":
        ref_type = payload.get('ref_type')
        ref = payload.get('ref')
        return f"Created {ref_type} {ref} in {repo}"
    return None

# 統計 PushEvent commit 數量（每個 repo 累加）
def summarize_push_events(events):
    push_summary = defaultdict(int)
    for event in events:
        if event['type'] == 'PushEvent':
            repo = event['repo']['name']
            count = len(event.get('payload', {}).get('commits', []))
            push_summary[repo] += count
    return [f"Pushed {count} commit{'s' if count != 1 else ''} to {repo}" for repo, count in push_summary.items() if count > 0]


def fetch_user_events(username, token=None):
    #todo: add comment here
    #todo: add more status code if exist
    ERROR_CODE = {
    401: "Unauthorized – Your token may be missing or incorrect",
    404: "Not Found – The specified user does not exist"}

    url = f"https://api.github.com/users/{username}/events"
    headers = {'Accept': 'application/vnd.github.v3+json'} # Request for GitHub V3 output in json format
    if token:
        headers['Authorization'] = f'token {token}'
    response = requests.get(url, headers=headers)
    # Exception handling
    if response.status_code != 200:
        print(f"Event code: {response.status_code} ({ERROR_CODE[response.status_code]})")
        return []
    return response.json()

def main():
    #todo: add comment here
    # Fetch user events from server and store to "events"(type: list)
    username = str(sys.argv[1])
    token = str(sys.argv[2]) if len(sys.argv)==3 else None # Default token will be none
    events = fetch_user_events(username, token)
    
    #TBC
    push_summary = summarize_push_events(events)
    other_events = [format_event(e) for e in events if e['type'] != 'PushEvent']
    #other_events = [e for e in other_events if e]  # 過濾 None

    print("Output:")
    for line in push_summary + other_events:
        print(f"- {line}")


if __name__ == "__main__":
    main()

#todo: add time stamp function
"""
from datetime import datetime, timezone

def convert_to_local_time(utc_str):
    # 將 GitHub API 的 UTC 字串轉換成 datetime 物件
    utc_time = datetime.strptime(utc_str, "%Y-%m-%dT%H:%M:%SZ")
    utc_time = utc_time.replace(tzinfo=timezone.utc)

    # 轉換成使用者系統的本地時間
    local_time = utc_time.astimezone()
    return local_time.strftime("%Y-%m-%d %H:%M")
"""