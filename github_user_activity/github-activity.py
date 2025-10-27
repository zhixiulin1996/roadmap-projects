import requests
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

# 抓取 GitHub 使用者活動
def fetch_user_events(username, token=None):
    url = f"https://api.github.com/users/{username}/events"
    headers = {'Accept': 'application/vnd.github.v3+json'}
    if token:
        headers['Authorization'] = f'token {token}'
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Error fetching events: {response.status_code}")
        return []
    return response.json()

# 主程式
if __name__ == "__main__":
    username = "kamranahmedse"  # 可改成你要查的 GitHub 使用者
    token = None  # 可填入你的 GitHub token（可選）
    events = fetch_user_events(username, token)

    push_summary = summarize_push_events(events)
    other_events = [format_event(e) for e in events if e['type'] != 'PushEvent']
    other_events = [e for e in other_events if e]  # 過濾 None

    print("Output:")
    for line in push_summary + other_events:
        print(f"- {line}")

