AUTHOR = 'William Setterberg'
SITENAME = 'setterberg'
SITEURL = ''

def link(txt, url):
    return f'<a target="_blank" href="{url}">{txt}</a>'

def code(txt):
    return f'<tt>{txt}</tt>'

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

DIRECT_TEMPLATES = ['index', 'blog']
ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False
PAGE_ORDER_BY = 'basename'

# Manually pick what we want in the menu bar
DISPLAY_PAGES_ON_MENU = False
MENUITEMS = (
    ('cv + resume', f'{SITEURL}/pages/cv-resume.html'),
    ('personal', f'{SITEURL}/blog.html')
)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

umn = link("University of Minnesota", "https://cse.umn.edu/physics")
impress = link("IMPRESS", "https://smallsat.umn.edu/impress")
wtmm = link("WTMM", "https://en.wikipedia.org/wiki/Wavelet_transform_modulus_maxima_method")
sunkit_spex = code(link("sunkit-spex", "https://github.com/sunpy/sunxspex/issues/83"))
stixdcpy = code(link("stixdcpy", "https://github.com/i4Ds/stixdcpy/pull/24"))
INDEX_BLURBS = (
    f'physics PhD student at {umn}',
    f'build solar X-ray instruments e.g. {impress}',
    f'analyze (e.g. {wtmm}) and image solar X-ray data',
    f'contribute to software e.g. {sunkit_spex}, {stixdcpy}',
    'mentor students',
)

STATIC_PATHS = [
    'static',
    'static/images',
]
