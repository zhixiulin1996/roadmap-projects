# GitHub User Activity

## Introduction
This Python project allows users to fetch and display the recent public activity of any GitHub user directly in the terminal.  
The project idea is inspired by [roadmap.sh](https://roadmap.sh/projects/github-user-activity).

Currently, it supports querying 10 types of events from the GitHub API (see the list of supported event types below).

## Usage

### Command
- **Linux**  
  ```bash
  python3 github-activity.py <username> <token_if_available>
  ```
- **Windows**  
  ```bash
  python github-activity.py <username> <token_if_available>
  ```

### Notes
- Only public events (i.e., those occurring in public repositories) can be retrieved.
- By default, up to 30 events are fetched per request.
- Events are categorized into **one-time** or **cumulative** types.
- The tool covers most common GitHub event types (see Supported Event Types below).
- The time range of the retrieved events will be displayed in the user's local time zone.

## Supported Event Types

### One-Time Events
| Event Name     | Description                          |
|----------------|--------------------------------------|
| `WatchEvent`   | Starred a repository                 |
| `ForkEvent`    | Forked a repository                  |
| `CreateEvent`  | Created a branch, tag, or repository |
| `DeleteEvent`  | Deleted a branch or tag              |
| `MemberEvent`  | Added as a collaborator              |
| `PublicEvent`  | Made a repository public             |

### Cumulative Events
| Event Name           | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| `PushEvent`          | User pushed code; counts total commits or pushes                            |
| `IssuesEvent`        | Opened or closed issues; counts total open/close actions (ONLY opened/closed actions) |
| `IssueCommentEvent`  | Commented on issues; counts total comments (ONLY created/deleted actions)|
| `PullRequestEvent`   | Opened or closed pull requests; counts total open/close actions (ONLY opened/closed actions) |
```