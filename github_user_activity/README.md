# GitHub User Activity
## Introduction
## Usage

- Enter the token if have
- Can only search for information that are open to everyone (events happen to public repos)
- Default can bulk 30 events per request (up to 100 events per request)
- Separate events into one-time events or cumulative event
- Deal with only part of but most of events in GitHub (support event and the action refer to the Supported Event Types)

## Supported Event Types
One-Time Event:
|Event Name|Description|
|---|---|
|`WatchEvent`| Star 某個 repo（不記錄 Unstar)|
|`ForkEvent`|	Fork 某個 repo（只記錄一次）|
|`CreateEvent`|	建立分支、tag 或 repo（每個 ref 一次）|
|`DeleteEvent`|	刪除分支或 tag（每個 ref 一次）|
|`MemberEvent`	|新增 collaborator（每人一次）|
|`PublicEvent`	|將 repo 設為公開（只記錄一次）|

Cumulative Events:
|Event Name|Description|
|---|---|
|`PushEvent`	|使用者推送程式碼，可累加 commit 或 push 次數|
|`IssuesEvent`	|開啟或關閉 issue，可累加 opened/closed 次數 (ONLY OPEN/CLOSE)|
|`IssueCommentEvent`	|對 issue 留言，可累加 comment 次數 (ONLY CREATED/DELETED)|
|`PullRequestEvent`	|開啟或關閉 pull request，可累加 opened/closed 次數 (ONLY OPEN/CLOSE)|