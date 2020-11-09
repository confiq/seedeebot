import logging
from seedeebot.conf import settings
from slack_bolt import App


logging.basicConfig(level=settings.DEBUG)

# export SLACK_SIGNING_SECRET=***
# export SLACK_BOT_TOKEN=xoxb-***
app = App(token=settings.SLACK_TOKEN, signing_secret=settings.SLACK_SIGNING_SECRET)


# Add functionality here
@app.event(event='message')
def hello_world(fu):
    print('message')
    logging.debug('yaaay')


if __name__ == "__main__":
    app.start(3000)  # POST http://localhost:3000/slack/events