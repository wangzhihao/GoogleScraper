#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from GoogleScraper import scrape_with_config, GoogleSearchError

# See in the config.cfg file for possible values
config = {
    'keyword': 'chopin compositions',
    'search_engines': ['google'],
    'num_pages_for_keyword': 1,
    'scrape_method': 'http',
    'log_level': 'NOTSET',
    'do_caching': 'True'
}

try:
    search = scrape_with_config(config)
except GoogleSearchError as e:
    print(e)

for serp in search.serps:
    print(serp)
    for link in serp.links:
        print(link)
