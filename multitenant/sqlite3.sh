#!/bin/bash
set -e
## declare an array variable
declare -a ips=(
#"159.203.105.254"
#"159.203.105.219"
#"159.203.106.56"
#"159.203.98.79"
#"159.203.111.87"
#"45.55.217.115"
#"45.55.216.203"
#"45.55.214.239"
#"45.55.214.153"
#"159.203.166.3"
)

## now loop through the above array
for ip in "${ips[@]}"
do
   server="root@""$ip"
   #echo "apt-get install sqlite3 libsqlite3-dev" | ssh $server bash -s -
   echo ' 
   cd ~/GoogleScraper;
   for i in {0..10}; do 
     db_name=google_scraper$i.db
     if [ $i -eq 10 ]; then
       db_name=google_scraper.db
     fi
     if [ -s $db_name ]; then
       #echo "found "$db_name" for "$HOSTNAME
       echo $HOSTNAME has already executed these queries:
       sqlite3 $db_name "select count(*) from serp;" 
       #echo $HOSTNAME has already collected these compositions:
       #sqlite3 $db_name "select count(*) from link;" 
     fi
   done
   ' | ssh $server bash -s -
done
