#!/usr/bin/env python

import sys
import logging
from seedeebot.conf import settings
from slack_bolt import App

kw = {
    'format': '[%(asctime)s] %(message)s',
    'datefmt': '%H:%M:%S %d-%m-%Y',
    'level': logging.DEBUG if settings.DEBUG else logging.INFO,
    'stream': sys.stdout,
}
logging.basicConfig(**kw)

app = App(token=settings.SLACK_TOKEN, signing_secret=settings.SLACK_SIGNING_SECRET)


# Add functionality here
@app.event(event='message')
def hello_world(fu):
    print('message')
    logging.debug('yaaay')


def main():
    pass

if __name__ == '__main__':
    main()
    app.start(3000)  # POST http://localhost:3000/slack/events

