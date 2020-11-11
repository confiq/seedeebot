import logging
from typing import Optional
from seedeebot.conf import settings
from slack_bolt import App

logger = logging.getLogger(__name__)


class SlackClient:
    def __init__(self,
                 signing_secret: Optional[str] = None,
                 token: Optional[str] = None,
                 ):
        self.token = token or settings.SLACK_TOKEN
        self.signing_secret = signing_secret or settings.SLACK_SIGNING_SECRET
        # TODO: Async
        self.slack_bolt_client = App(token=self.token, signing_secret=self.signing_secret)
