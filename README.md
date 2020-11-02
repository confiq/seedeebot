A chat bot for [Slack](https://slack.com) inspired by [llimllib/limbo](https://github.com/llimllib/limbo), [will](https://github.com/skoczen/will) and [slackbot](https://github.com/lins05/slackbot).

## Features

* Based on slack [Event API](https://api.slack.com/events-api)
* Simple plugins mechanism
* Messages can be handled concurrently
* bot can work in asyncio or in queue system (pubsub/sqs/rabbitmq)

## Installation

```
pip install TODO
```

## Usage

### Generate the slack api token
TODO: 

First you need to get the slack api token for your bot. You have two options:

1. If you use a [bot user integration](https://api.slack.com/bot-users) of slack, you can get the api token on the integration page.
2. If you use a real slack user, you can generate an api token on [slack web api page](https://api.slack.com/web).


### Configure the bot
First create a `slackbot_settings.py` and a `run.py` in your own instance of slackbot.

##### Configure the api token

Then you need to configure the `API_TOKEN` in a python module `slackbot_settings.py`, which must be located in a python import path. This will be automatically imported by the bot.

slackbot_settings.py:

```python
API_TOKEN = "<your-api-token>"
```

Alternatively, you can use the environment variable `SLACKBOT_API_TOKEN`.

##### Run the bot

```python
from slackbot.bot import Bot
def main():
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    main()
```

##### Configure the default answer

Add a DEFAULT_REPLY to `slackbot_settings.py`:
```python
DEFAULT_REPLY = "Sorry but I didn't understand you"
```

##### Configure the docs answer

The `message` attribute passed to [your custom plugins](#create-plugins) has an special function `message.docs_reply()` that will parse all the plugins available and return the Docs in each of them.

##### Send all tracebacks directly to a channel, private channel, or user
Set `ERRORS_TO` in `slackbot_settings.py` to the desired recipient. It can be any channel, private channel, or user. Note that the bot must already be in the channel. If a user is specified, ensure that they have sent at least one DM to the bot first.

```python
ERRORS_TO = 'some_channel'
# or...
ERRORS_TO = 'username'
```

##### Configure the plugins

Add [your plugin modules](#create-plugins) to a `PLUGINS` list in `slackbot_settings.py`:

```python
PLUGINS = [
    'slackbot.plugins',
    'mybot.plugins',
]
```

Now you can talk to your bot in your slack client!

## Create Plugins

A chat bot is meaningless unless you can extend/customize it to fit your own use cases.

To write a new plugin, simply create a function decorated by `slackbot.bot.respond_to` or `slackbot.bot.listen_to`:

`#TODO: write docs how to create the plugin`



## The `@default_reply` decorator


```python
@default_reply
def my_default_handler(message):
    message.reply('...')
```

Here is another variant of the decorator:

```python
@default_reply(r'hello.*)')
def my_default_handler(message):
    message.reply('...')
```

The above default handler would only handle the messages which must (1) match the specified pattern and (2) can't be handled by any other registered handler.
