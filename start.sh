#!/bin/bash
set -e
rm -rf google_scraper.db .scrapecache/
sed -i -e 's/composers/composer$1/g' get_composition.py 
nohup python3 get_composition.py &
tail -f nohup.out
