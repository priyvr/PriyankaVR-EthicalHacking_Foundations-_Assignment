#!/bin/bash

if [ -z "$1" ]
then
  echo "Usage: ./port_report.sh <IP>"
  exit 1
fi

IP=$1
DATE=$(date +%Y%m%d)
FILE="scan_${IP}_${DATE}.txt"

ports=(21 22 80 443 3306)

open_count=0

echo "Scanning $IP..." > $FILE

for port in "${ports[@]}"
do
  timeout 1 bash -c "echo > /dev/tcp/$IP/$port" 2>/dev/null

  if [ $? -eq 0 ]; then
    echo "Port $port: OPEN" >> $FILE
    open_count=$((open_count+1))
  else
    echo "Port $port: CLOSED" >> $FILE
  fi
done

echo "Total Open Ports: $open_count" >> $FILE
echo "Scan complete. Results saved in $FILE"