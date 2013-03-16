#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import os

AUTHOR = u'Andy Doan'
SITENAME = u'BettyKRocks'
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

THEME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "theme")
DEFAULT_PAGINATION = False
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
OUTPUT_SOURCES = True
OUTPUT_SOURCES_EXTENSION = '.rst'

andymenu = [
    {'label': 'About Me', 'url': '/andy.html', 'slug': 'andy'},
    {'label': 'Hire Me', 'url': '/hire-andy.html', 'slug': 'hire-andy'},
]

MENU_ITEMS = [
    { 'label':'Home', 'url': '/' },
    { 'label':'Bethany', 'url': '/bethany.html' },
    { 'label':'Andy', 'url': '/andy.html', 'submenu': andymenu },
    { 'label':'About Us', 'url': '/about-us.html' },
]
