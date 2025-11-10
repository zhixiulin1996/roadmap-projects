# Server Performance Stats CLI Tool
A lightweight Bash script to analyze basic server performance metrics in real time. Designed for Linux environments, this tool provides a quick overview of system health including CPU, memory, disk usage, and more.(**Inspired by:** [Server Performance Stats](https://roadmap.sh/projects/server-stats))

---
## Features

- **CPU Usage** — Total usage percentage
- **Memory Usage** — Free, used, and usage percentage (in GB)
- **Disk Usage** — Free, used, total, and usage percentage (in GB)
- **Top 5 Processes** — Sorted by CPU and memory usage
- **OS Version** — Distribution and version
- **Uptime** — Human-readable system uptime
- **Load Average** — 1, 5, and 15-minute averages
- **Logged-in Users** — Active sessions
- **Failed Login Attempts** — Recent failed login attempts (via `lastb`)

---

## Usage
Run the script with:

```bash
./server-stats.sh
```
You may need `sudo` access for failed login detection:
```bash
sudo ./server-stats.sh
```
---

## Sample Output

```
===== SERVER PERFORMANCE STATS =====

Total CPU Usage:
Used: 4.5%

Total Memory Usage:
Free memory: 5.23 GB
Used memory: 2.77 GB
Used Percentage: 34.63 %

Total Disk Usage:
Total disk: 238.47 GB
Used disk: 121.32 GB
Free disk: 117.15 GB
Used Percentage: 50.87 %

Top 5 Processes by CPU:
  PID COMMAND %CPU
  1234 chrome 25.0
  ...

Top 5 Processes by Memory:
  PID COMMAND %MEM
  1234 firefox 12.3
  ...

OS Version:
Ubuntu 22.04.3 LTS

Uptime:
up 3 days, 4 hours, 12 minutes

Load Average:
0.12, 0.18, 0.22

Logged-in Users:
user1  pts/0  2025-11-10 14:22 (00:03)

Failed Login Attempts:
admin  ssh:notty  192.168.1.101  Fri Nov 10 14:30 - 14:30  (00:00)

===== SERVER PERFORMANCE STATS =====
```

---

## Notes

- Tested on Ubuntu 
- Requires `awk`, `ps`, `df`, `free`, `top`, `uptime`, `who`, and `lastb`.
- For failed login attempts, ensure `/var/log/btmp` exists and is readable (may require `sudo`).