import logging
from seedeebot.libs.slackClient import SlackClient
from seedeebot.manager import PluginsManager
from seedeebot.dispatcher import MessageDispatcher
logger = logging.getLogger(__name__)


class Client(SlackClient):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._dispatcher = MessageDispatcher()
        self._plugins = PluginsManager()


