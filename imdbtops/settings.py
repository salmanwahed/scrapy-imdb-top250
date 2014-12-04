# -*- coding: utf-8 -*-

# Scrapy settings for imdbtops project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'imdbtops'

SPIDER_MODULES = ['imdbtops.spiders']
NEWSPIDER_MODULE = 'imdbtops.spiders'

DEPTH_LIMIT = 2

DEPTH_STATS_VERBOSE = True

LOG_LEVEL = 'DEBUG'

ITEM_PIPELINES = {
    'imdbtops.pipelines.ImdbtopsPipeline': 100,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'imdbtops (+http://www.yourdomain.com)'
