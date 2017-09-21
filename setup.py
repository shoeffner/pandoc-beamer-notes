# -*- coding: utf-8 -*-

from setuptools import setup

import re

from pandoc_beamer_notes import __version__

REPOSITORY = 'https://github.com/shoeffner/pandoc-beamer-notes'

README = ''
with open('README.rst', 'r') as f:
    README = f.read()
README = re.sub(r' _(.+): ([^(http)].+)', r' _\1: {}/blob/master/\2'
                .format(REPOSITORY), README)

setup(
  name='pandoc-beamer-notes',
  version=__version__,
  description='A pandoc filter to allow a markdown way of using notes for ' +
  'latex beamer presentations.',
  long_description=README,
  entry_points={'console_scripts':
                ['pandoc-beamer-notes = pandoc_beamer_notes:main']},
  scripts=['pandoc_beamer_notes/pandoc-beamer-notes.py'],
  author='Sebastian Höffner',
  author_email='info@sebastian-hoeffner.de',
  url=REPOSITORY,
  download_url='{}/tarball/{}'.format(REPOSITORY, __version__),
  packages=['pandoc_beamer_notes'],
  classifiers=[
      'Development Status :: 7 - Inactive',
      'Intended Audience :: Science/Research',
      'License :: OSI Approved :: MIT License',
      'Natural Language :: English',
      'Programming Language :: Python :: 3.6',
      'Topic :: Text Processing :: Filters',
  ],
  install_requires=['panflute'],
  license='MIT',
  keywords=['pandoc', 'beamer', 'notes', 'filter'],
)
