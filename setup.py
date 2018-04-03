# -*- coding: utf-8 -*-

from glob import glob

DISTUTILS_DEBUG = "True"

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

config = {}

config['classifiers'] = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: GNU General Public License (GPL)',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: JavaScript',
    'Topic :: Scientific/Engineering',
    'Topic :: Software Development :: Code Generators',
]

setup(name='mosaicode_javascript_webaudio',
      install_requires=['mosaicode'],
      tests_require=[],
      test_suite='',
      version='1.2',
      packages=[
          'mosaicode_javascript_webaudio',
          'mosaicode_javascript_webaudio.extensions',
          'mosaicode_javascript_webaudio.extensions.webaudio',
          'mosaicode_javascript_webaudio.extensions.ports'],
      scripts=[],
      description='Code generation for Digital art',
      author='Bits & Beads Research Lab',
      author_email='mosaicode-dev@googlegroups.com',
      maintainer="Bits & Beads Research Lab",
      maintainer_email="mosaicode-dev@googlegroups.com",
      license="GNU GPL3",

      url='https://mosaicode.github.io', 
      download_url = 'https://github.com/Mosaicode/mosaicode.git',
      keywords = ['VLP', 'Blocks','Code Generation', 'Digital art'],  

      # this is fucked up! must put it in package_data!!
      data_files=[],
      **config
      )
