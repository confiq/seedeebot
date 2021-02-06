import logging
from seedeebot.conf import settings
from seedeebot.client import Client

logging.basicConfig(level=settings.DEBUG)


if __name__ == "__main__":
    client = Client()
    client.slack_bolt_client.start(3000)
