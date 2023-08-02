AUTHOR = 'Jesus Caro'
SITENAME = "Jesus Caro's Blog"
SITEURL = ''

BIO = 'Hello! My name is Jesus Caro, I am a Data Engineer with 6 years of experience in Data Engineering, analytics and data science. This blog is a collection of things I find interesting, as well as some personal stuff!'


PATH = 'content'

TIMEZONE = 'MST'

DEFAULT_LANG = 'en'

THEME = '/Users/jcaro-work/VSCODE/theme_repo/pelican-hyde'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

## pelican-ipynb
MARKUP = ("md", "ipynb")

from pelican_jupyter import markup as nb_markup
PLUGINS = [nb_markup]
IPYNB_MARKUP_USE_FIRST_CELL = True

IGNORE_FILES = [".ipynb_checkpoints"]

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

COLOR_THEME = 'theme-base-08'
PROFILE_IMAGE = 'me.png'
FONT_AWESOME_JS = 'https://use.fontawesome.com/ada6f22d07.js'
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True