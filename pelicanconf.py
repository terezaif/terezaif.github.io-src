#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime 
from pathlib import Path

CURRENT_DIR_PATH = Path(__file__).resolve().parent

# Site Settings
AUTHOR = 'Tereza Iofciu'
SITENAME = 'Tereza Iofciu'
SITEURL =   'http://terezaiofciu.com'  
THEME = '{}/voce'.format(CURRENT_DIR_PATH)
PATH = 'content'

# General Settings
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'en'
DEFAULT_PAGINATION = 6
SUMMARY_MAX_LENGTH = 30

# Feed Generation
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'fees/all.rss.xml'
FEED_DOMAIN = 'http://terezaiofciu.com' 

# Page Settings
PAGE_SAVE_AS = '{slug}.html'
TAGS_URL = 'tags.html'
ARCHIVES_URL = 'archive.html'

# Blogroll
LINKS = (('Home', '/index.html'),
         ('About', '/about.html'),
         ('Speaker Info', '/speaker-info.html'),
     	 ('Talks', '/talks.html'))

# Social Accounts
SOCIAL = (('Email', 'mailto:terezaif@gmail.com'),
          ('GitHub', 'http://github.com/terezaif'),
	  	  ('Twitter', 'https://twitter.com/terezaif'),
	  	  ('Linkedin', 'https://www.linkedin.com/in/tereza-iofciu'))

# Plugins
PLUGINS = ['pelican_webassets']
PLUGIN_PATHS = ['{}/plugins'.format(THEME)]

# Publish
DELETE_OUTPUT_DIRECTORY = False

# Custom Vars
GOOGLE_ANALYTICS_ID = 'G-BQY8XBH619'
GOOGLE_ANALYTICS_PROP = 'Tereza Iofciu Personal'
USER_LOGO_URL = 'theme/images/tereza.png'
MANGLE_EMAILS = True
FUZZY_DATES = True
CURRENT_YEAR = datetime.now().year

# Sitemap
SITEMAP_SAVE_AS = 'sitemap.xml'
DIRECT_TEMPLATES = ['sitemap', 'index']

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Markdown
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'pymdownx.details': {}
    },
    'output_format': 'html5',
}

OUTPUT_RETENTION = ['CNAME', '.git', 'README.md']
