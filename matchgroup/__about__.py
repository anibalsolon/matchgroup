from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

CLASSIFIERS = [
    'Development Status :: 2 - Pre-Alpha', 'Environment :: Console',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: Apache Software License',
    'Operating System :: MacOS :: MacOS X',
    'Operating System :: POSIX :: Linux',
    'Operating System :: Microsoft :: Windows',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7', 'Topic :: Scientific/Engineering',
    'Topic :: Scientific/Engineering :: Information Analysis'
]

description = ''

long_description = """========================================================
MatchGroup
========================================================

"""

__packagename__ = 'matchgroup'
__author__ = __maintainer__ = 'Anibal Solon'
__email__ = 'anibalsolon@gmail.com'
__license__ = 'Apache License, 2.0'
__status__ = 'Pre-Alpha'
__description__ = description
__longdesc__ = long_description
__url__ = 'https://github.com/anibalsolon/matchgroup'

DOWNLOAD_URL = (
    'http://github.com/anibalsolon/{name}/archives/{ver}.tar.gz'.format(
        name=__packagename__, ver=__version__))

PLATFORMS = 'OS Independent'
MAJOR = __version__.split('.')[0]
MINOR = __version__.split('.')[1]
MICRO = __version__.replace('-', '.').split('.')[2]
ISRELEASE = (len(__version__.replace('-', '.').split('.')) == 3
             or 'post' in __version__.replace('-', '.').split('.')[-1])
VERSION = __version__
PROVIDES = ['matchgroup']
REQUIRES = [
    'pandas>=0.23.0',
]

SETUP_REQUIRES = ['setuptools>=27.0']
TESTS_REQUIRES = ['pytest-cov', 'codecov', 'pytest-env', 'pytest-xdist']
LINKS_REQUIRES = []

EXTRA_REQUIRES = {
    'tests': TESTS_REQUIRES,
    'dev': TESTS_REQUIRES + ['yapf>=0.22'],
}

EXTRA_REQUIRES['all'] = list(set(sum(EXTRA_REQUIRES.values(), [])))