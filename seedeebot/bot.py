from __future__ import absolute_import

import logging
import re
import time
from seedeebot.conf import settings
# from seedeebot.manager import PluginsManager
from seedeebot.client import Client
# from seedeebot.dispatcher import MessageDispatcher

logger = logging.getLogger(__name__)


class Bot(object):
    def __init__(self):
        self._client = Client()

    def run(self):
        self._plugins.init_plugins()
        self._dispatcher.start()
        if not self._client.connected:
            self._client.rtm_connect()


        logger.info('connected to slack RTM api')
        self._dispatcher.loop()

    def _keepactive(self):
        logger.info('keep active thread started')
        while True:
            time.sleep(30 * 60)
            self._client.ping()


def respond_to(matchstr, flags=0):
    def wrapper(func):
        PluginsManager.commands['respond_to'][
            re.compile(matchstr, flags)] = func
        logger.info('registered respond_to plugin "%s" to "%s"', func.__name__,
                    matchstr)
        return func

    return wrapper


def listen_to(matchstr, flags=0):
    def wrapper(func):
        PluginsManager.commands['listen_to'][
            re.compile(matchstr, flags)] = func
        logger.info('registered listen_to plugin "%s" to "%s"', func.__name__,
                    matchstr)
        return func

    return wrapper


# def default_reply(matchstr=r'^.*$', flags=0):
def default_reply(*args, **kwargs):
    """
    Decorator declaring the wrapped function to the default reply hanlder.

    May be invoked as a simple, argument-less decorator (i.e. ``@default_reply``) or
    with arguments customizing its behavior (e.g. ``@default_reply(matchstr='pattern')``).
    """
    invoked = bool(not args or kwargs)
    matchstr = kwargs.pop('matchstr', r'^.*$')
    flags = kwargs.pop('flags', 0)

    if not invoked:
        func = args[0]

    def wrapper(func):
        PluginsManager.commands['default_reply'][
            re.compile(matchstr, flags)] = func
        logger.info('registered default_reply plugin "%s" to "%s"', func.__name__,
                    matchstr)
        return func

    return wrapper if invoked else wrapper(func)
