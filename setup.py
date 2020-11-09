from os.path import join, dirname
from setuptools import setup, find_packages

__version__ = open(join(dirname(__file__), 'seedeebot/version.py')).read().strip()

install_requires = (
    'slack-sdk>=3.0.0rc1',
    'slackblocks>=0.2.2',
)

excludes = (
    '*test*',
    '*example*'
    '*local_settings*',
    '*venv*',
)

setup(name='seedeebot',  # TODO: move this to setup.cfg file as done in django
      version=__version__,
      license='MIT',
      description='A simple chat bot for Slack',
      author='Igor Konforti',
      author_email='seedeebot@confiq.org',
      url='https://github.com/confiq/seedeebot',
      platforms=['Any'],
      packages=find_packages(exclude=excludes),
      install_requires=install_requires,
      classifiers=['Development Status :: 4 - Beta',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 3.8',
                   'Programming Language :: Python :: 3.9',
                   ])
