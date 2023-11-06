#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Daniel'
SITENAME = u'www.campingwonders.com'
SITEURL = 'https://www.campingwonders.com'

PATH = 'content'
STATIC_PATHS = [ 'images', 'php', 'css' ]

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

DELETE_OUTPUT_DIRECTORY = False

# Needed for tipue_search:
DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'search', 'tags')

#DISQUS_SITENAME = 'unixdude-net'

PLUGIN_PATHS = ["/usr/local/pelican-plugins","/usr/src/app/pelican-plugins"]
#PLUGINS = ["assets", "liquid_tags", "tag_cloud"]
#PLUGINS = ["tag_cloud", "assets", "read_more", "pelican_algolia"]
PLUGINS = ["tipue_search", "tag_cloud", "assets", "read_more"]
#DEFAULT_METADATA = (('tags', 'misc'),)

DEFAULT_PAGINATION = 10
PAGINATION_PATTERNS = (
    (1, '{base_name}/',               '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

# Default summary length = 50
#SUMMARY_MAX_LENGTH = None

# Feed generation is usually not desired when developing
TRANSLATION_FEED_ATOM = None
#AUTHOR_FEED_ATOM = 'feeds/author_%s.atom.xml'
#AUTHOR_FEED_RSS = 'feeds/author_%s.rss'
AUTHOR_FEED_ATOM = ''
AUTHOR_FEED_RSS = ''

FEED_ALL_ATOM = 'feeds/all.atom.xml'
#CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
FEED_ALL_RSS = 'feeds/rss'

DISPLAY_BREADCRUMBS = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True
THEME = 'theme'
MENUITEMS = [
#   ('Home', '/'),
    ('Archives', [
        ('By Category', '/categories/'),
        ('By Tag', '/tags/'),
        ('By Date', '/archives/'),
        ]),
#   ('Links', [
#       ('VMware', 'http://www.vmware.com'),
#       ('Cisco', 'http://www.cisco.com'),
#       ('F5', 'http://www.f5.com'),
#       ('Radware', 'http://www.radware.com'),
#       ('Ansible', 'http://www.ansible.com'),
#       ('Apple', 'http://www.apple.com'),
#       ('FreeBSD', 'http://www.freebsd.org'),
#       ]),
    ('About Me', '/pages/about/'),
#   ('Contact Me', '/pages/contact/'),
#   ('Search', '014635788047283224250:ebkqm56kagw'),
    ]

#LINKS = (
#        ('watchuseek', 'https://www.watchuseek.com/forums/'),
#        ('chronulator', 'https://www.sharebrained.com/chronulator/'),
#        ('Steinhart', 'https://www.steinhartwatches.de/'),
#        )
#SOCIAL = (('twitter', 'http://twitter.com/DaanDebie'),
#          ('linkedin', 'http://www.linkedin.com/in/danieldebie'),
#          ('github', 'http://github.com/DandyDev'),
#          ('stackoverflow', 'http://stackoverflow.com/users/872397/dandydev'))

CODE_HIGHLIGHT = 'https://www.campingwonders.com/theme/css/solarized-dark.css'
BS3_URL   = 'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css'
BS3_JS    = 'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js'
BS3_THEME = 'https://maxcdn.bootstrapcdn.com/bootswatch/3.3.7/spacelab/bootstrap.min.css'
#BS3_THEME = '/theme/css/mybootstrap.css'
BS3_THEME_NAME = 'Spacelab'
BS3_THEME_HOMEPAGE = 'https://bootswatch.com/3/spacelab/'

TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 1000
TAG_CLOUD_SORTING = 'alphabetically'
TAG_CLOUD_BADGE = True

# provided as examples, they make ‘clean’ urls. used by MENU_INTERNAL_PAGES.
CATEGORIES_URL     = 'categories/'
CATEGORIES_SAVE_AS = 'categories/index.html'
ARCHIVES_URL       = 'archives/'
ARCHIVES_SAVE_AS   = 'archives/index.html'

#---
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAGS_URL = 'tags/'
TAGS_SAVE_AS = 'tags/index.html'
#
AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
AUTHORS_URL = 'authors/'
AUTHORS_SAVE_AS = 'authors/index.html'
#
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
#----

ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'

YEAR_ARCHIVE_SAVE_AS = 'archives/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'archives/{date:%Y}/{date:%b}/index.html'
DAY_ARCHIVE_SAVE_AS = 'archives/{date:%Y}/{date:%b}/{date:%d}/index.html'

PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

FAVICON = u'/images/favicon.png'
FAVICON_TYPE = u'png'

#SHOW_CATEGORY_FEEDS_IN_SIDEBAR = True

# This indicates what goes inside the read more link
READ_MORE_LINK = '<span>Continue reading</span>'
# This is the format of the read more link
READ_MORE_LINK_FORMAT = ' <a class="label label-primary read-more" href="/{url}">{text}</a>'

DEFAULT_METADATA = {
    'status': 'draft',
}

SIDEBAR_ABOUT_TITLE = "Fun stuff"
SIDEBAR_ABOUT = "This site is about some of my interests: antique phones, Atari, watches, and electronics projects."
