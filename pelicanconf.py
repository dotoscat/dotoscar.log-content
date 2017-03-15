#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "Oscar Triano 'dotoscat'"
SITENAME = 'cat dotoscat.log'
SITEURL = 'https://dotoscat.github.io'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
#RELATIVE_URLS = True

# Blogroll
# ('You can modify those links in your config file', '#')
LINKS = ()

# Social widget
#('You can add links in your config file', '#'),
SOCIAL = (
          ('My twitter \'@cat_dotoscat\'', 'https://twitter.com/cat_dotoscat'),
          ('Checkout my github.com/dotoscat', 'https://github.com/dotoscat')
    )


DEFAULT_PAGINATION = 3

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
