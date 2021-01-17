#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime 
from pathlib import Path

CURRENT_DIR_PATH = Path(__file__).resolve().parent

# Site Settings
AUTHOR = 'Tereza Iofciu'
SITENAME = 'Tereza Iofciu'
SITEURL =   'http://localhost:8000'  
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
FEED_DOMAIN = 'http://localhost:8000' 

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
GOOGLE_ANALYTICS_ID = 'G-BL4GZ3S84L'
GOOGLE_ANALYTICS_PROP = 'Personal'
USER_LOGO_URL = 'themes/images/tereza.png'
MANGLE_EMAILS = True
FUZZY_DATES = True
CURRENT_YEAR = datetime.now().year

# Sitemap
SITEMAP_SAVE_AS = 'sitemap.xml'
DIRECT_TEMPLATES = ['sitemap', 'index']

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
