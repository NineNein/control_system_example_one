#from distutils.core import setup
from setuptools import setup

#intendet to be called with develop

setup(
  name = 'devicecom',         # How you named your package folder (MyLib)
  packages = ['devicecom'],   # Chose the same as "name"
  version = '0.11',      # Start with a small number and increase it with every change you make
  license='GPL-3.0',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'package which contains device server for the penning trap experiment',   # Give a short description about your library
  author = 'Alexander Rischka',                   # Type in your name
  author_email = 'alexander.rischka@t-online.de',      # Type in your E-Mail
  url = 'https://github.sydney.edu.au/QCL/devicecom',   # Provide either the link to your github or to your website
  download_url = '',    # I explain this later on
  keywords = ['epics', 'server', 'client'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'pyepics',
          'pcaspy',
          'sefra',
          'multiprocess'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',   # Again, pick a license
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)