#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from GoogleScraper import scrape_with_config, GoogleSearchError
import json

with open('data/composers.json') as data_file:    
    data = json.load(data_file)

keywords = map((lambda item: item['name'] + ' compositions') ,filter(lambda x: 'name' in x, data))

# See in the config.cfg file for possible values
config = {
    'keywords': keywords,
    'search_engines': ['google'],
    'google_sleeping_ranges':  {
        1:  (2, 3)
    },
    'num_pages_for_keyword': 1,
    'scrape_method': 'http',
    'log_level': 'NOTSET',
    'do_caching': 'True',
    'database_name': 'google_scraper',
    'clean_cache_after': 4800
}

try:
    search = scrape_with_config(config)
except GoogleSearchError as e:
    print(e)
