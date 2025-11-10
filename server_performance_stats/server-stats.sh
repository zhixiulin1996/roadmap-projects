#!/bin/bash

# ANSI color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

echo -e "\n${CYAN}===== SERVER PERFORMANCE STATS =====${NC}"
#==========================================================================================================================#
# CPU usage
echo -e "${YELLOW}Total CPU Usage:${NC}"
top -bn1 | grep "Cpu(s)" | awk '{print "'${GREEN}'Used: " $2 + $4 "%'${NC}'"}'

#==========================================================================================================================#
# Memory usage
echo -e "\n${YELLOW}Total Memory Usage:${NC}"
read total used <<< $(free | awk '/Mem:/ {print $2, $3}') # read total/used memory (unit: KB)
# Unit conversion
read free_gb used_gb percent <<< $(awk -v t=$total -v u=$used 'BEGIN {
    free_gb = (t - u) / 1048576;
    used_gb = u / 1048576;
    percent = (u / t) * 100;
    printf "%.2f %.2f %.2f", free_gb, used_gb, percent
}')
# Result
echo -e "${GREEN}Free memory: ${free_gb} GB"
echo "Used memory: ${used_gb} GB"
echo -e "Used Percentage: ${percent} %${NC}"

#==========================================================================================================================#
# Disk usage
echo -e "\n${YELLOW}Total Disk Usage:${NC}"
read total used <<< $(df --total | awk '/total/ {print $2, $3}') # read total/used disk (unit: KB)
# Unit conversion
read total_gb used_gb free_gb percent <<< $(awk -v t=$total -v u=$used 'BEGIN {
    total_gb = t / 1048576;
    used_gb = u / 1048576;
    free_gb = (t - u) / 1048576;
    percent = (u / t) * 100;
    printf "%.2f %.2f %.2f %.2f", total_gb, used_gb, free_gb, percent
}')
# Result
echo -e "${GREEN}Total disk: ${total_gb} GB${NC}"
echo -e "${GREEN}Used disk: ${used_gb} GB${NC}"
echo -e "${GREEN}Free disk: ${free_gb} GB${NC}"
echo -e "${GREEN}Used Percentage: ${percent} %${NC}"

#==========================================================================================================================#
# Top 5 processes by CPU
echo -e "\n${YELLOW}Top 5 Processes by CPU:${NC}"
ps -eo pid,comm,%cpu --sort=-%cpu | head -n 6 | awk '{print "'${BLUE}'" $0 "'${NC}'"}'

#==========================================================================================================================#
# Top 5 processes by Memory
echo -e "\n${YELLOW}Top 5 Processes by Memory:${NC}"
ps -eo pid,comm,%mem --sort=-%mem | head -n 6 | awk '{print "'${BLUE}'" $0 "'${NC}'"}'

#==========================================================================================================================#
# OS information
echo -e "\n${YELLOW}OS Version:${NC}"
echo -e "${GREEN}$(grep 'PRETTY_NAME' /etc/os-release | cut -d = -f 2 | tr -d '\"')${NC}"

#==========================================================================================================================#
# Uptime
echo -e "\n${YELLOW}Uptime:${NC}"
uptime -p | awk '{print "'${GREEN}'" $0 "'${NC}'"}'

#==========================================================================================================================#
# Load average
echo -e "\n${YELLOW}Load Average:${NC}"
uptime | awk -F'load average:' '{print "'${GREEN}'" $2 "'${NC}'"}'

#==========================================================================================================================#
# Logged-in Users
echo -e "\n${YELLOW}Logged-in Users:${NC}"
who | awk '{print "'${GREEN}'" $0 "'${NC}'"}'

#==========================================================================================================================#
# Failed Login Attempts
echo -e "\n${YELLOW}Failed Login Attempts:${NC}"
if [ -s /var/log/btmp ]; then
  echo -e "${YELLOW}Failed Login Attempts:${NC}"
  sudo lastb | head -n 5 | awk '{print "'${RED}'" $0 "'${NC}'"}'
else
  echo -e "${GREEN}No failed login attempts recorded.${NC}"
fi

echo -e "\n${CYAN}===== SERVER PERFORMANCE STATS =====${NC}\n\n"