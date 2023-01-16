AUTHOR = 'William Setterberg'
SITENAME = 'setterberg'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISPLAY_PAGES_ON_MENU = True
DEFAULT_PAGINATION = False
PAGE_ORDER_BY = 'basename'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

INDEX_BLURBS = (
    'physics PhD student at <a target="_blank" href="https://cse.umn.edu/physics">University of Minnesota</a>',
    'build solar X-ray instruments e.g. <a target="_blank" href="https://smallsat.umn.edu/impress">IMPRESS</a>',
    'contribute to software e.g. <tt><a target="_blank" href="https://github.com/sunpy/sunxspex/issues/83">sunkit-spex</a>,</tt>'
    '<tt><a target="_blank" href="https://github.com/i4Ds/stixdcpy/pull/24">stixdcpy</a></tt>',
    'mentor students',
)

STATIC_PATHS = [
    'static',
    'static/images',
]
