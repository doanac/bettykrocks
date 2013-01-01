#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import os

AUTHOR = u'Andy Doan'
SITENAME = u'BettyKRocks'
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

"""
# Blogroll
LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
          ('Python.org', 'http://python.org'),
          ('Jinja2', 'http://jinja.pocoo.org'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)
"""

THEME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "theme")
DEFAULT_PAGINATION = False
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
GENERATE_SOURCE = True

MENU_ITEMS = [
    { 'label':'Home', 'url': '/' },
    { 'label':'Bethany', 'url': '/bethany.html' },
    { 'label':'Andy', 'url': '/andy.html' },
    { 'label':'About Us', 'url': '/about-us.html' },
]
