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
Matchgroup
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
    'http://github.com/anibalsolon/{name}/archives/{__version__}.tar.gz'.format(
        name=__packagename__, __version__="{__version__}"))

PLATFORMS = 'OS Independent'
PROVIDES = ['matchgroup']
REQUIRES = [
    'pandas>=0.23.0',
    'numpy>=0.15.1',
]

SETUP_REQUIRES = ['setuptools>=27.0']
TESTS_REQUIRES = ['pytest-cov', 'codecov', 'pytest-env', 'pytest-xdist']
LINKS_REQUIRES = []

EXTRA_REQUIRES = {
    'tests': TESTS_REQUIRES,
    'dev': TESTS_REQUIRES + ['yapf>=0.22'],
}

EXTRA_REQUIRES['all'] = list(set(sum(EXTRA_REQUIRES.values(), [])))


def main():

    import os
    from setuptools import setup, find_packages
    from inspect import getfile, currentframe
    
    import versioneer

    pkg_data = {'matchgroup': []}
    root_dir = os.path.dirname(os.path.abspath(getfile(currentframe())))

    version = None
    cmdclass = {}
    if os.path.isfile(os.path.join(root_dir, 'matchgroup', 'VERSION')):
        with open(os.path.join(root_dir, 'matchgroup', 'VERSION')) as vfile:
            version = vfile.readline().strip()
        pkg_data['matchgroup'].insert(0, 'VERSION')

    if version is None:
        import versioneer
        version = versioneer.get_version()
        cmdclass = versioneer.get_cmdclass()

    setup(
        name=__packagename__,
        version=version,
        cmdclass=cmdclass,
        description=__description__,
        long_description=__longdesc__,
        author=__author__,
        author_email=__email__,
        maintainer=__maintainer__,
        maintainer_email=__email__,
        url=__url__,
        license=__license__,
        classifiers=CLASSIFIERS,
        download_url=DOWNLOAD_URL,
        provides=PROVIDES,
        setup_requires=SETUP_REQUIRES,
        install_requires=REQUIRES,
        tests_require=TESTS_REQUIRES,
        extras_require=EXTRA_REQUIRES,
        dependency_links=LINKS_REQUIRES,
        packages=find_packages(),
        zip_safe=False,
    )


if __name__ == "__main__":
    main()