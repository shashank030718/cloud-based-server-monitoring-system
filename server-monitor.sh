#!/bin/bash


#Linux Server Monitoring Script


echo "================================"
echo "         SERVER HEALTH REPORT"
echo "================================"



echo ""
echo "Hostname:"
hostname


echo ""
echo "Date and time:"
date 

#CPU Load 

echo ""
echo "CPU Load:"
uptime


#Memory Usage
echo ""
echo "Memory Usage:"
free -h


# Memory Alert
MEMORY_USAGE=$(free | awk '/Mem:/ {printf "%.0f", $3/$2 * 100}')

if [ "$MEMORY_USAGE" -gt 80 ]; then
    echo "WARNING: High Memory Usage: ${MEMORY_USAGE}%"
else
    echo "OK: Memory Usage: ${MEMORY_USAGE}%"
fi


#Disk usage
echo ""
echo "Disk Usage:"
df -h /

# Disk Alert
DISK_USAGE=$(df / | awk 'NR==2 {gsub("%","",$5); print $5}')

if [ "$DISK_USAGE" -gt 80 ]; then
    echo "WARNING: High Disk Usage: ${DISK_USAGE}%"
else
    echo "OK: Disk Usage: ${DISK_USAGE}%"
fi


#TOP Memory Processes
echo ""
echo "Top 5 memory-consuming processes:"
ps aux --sort=-%mem | head -n 6

echo ""
echo "=========================="
echo "      Monitoring Completed"
echo "==========================="
