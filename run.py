#!/usr/bin/env python

import sys
import logging
import logging.config
from seedeebot import conf
from seedeebot.bot import Bot

local_setting = {

}

def main():
    kw = {
        'format': '[%(asctime)s] %(message)s',
        'datefmt': '%H:%M:%S %d-%m-%Y',
        'level': logging.DEBUG if settings.DEBUG else logging.INFO,
        'stream': sys.stdout,
    }
    logging.basicConfig(**kw)
    logging.getLogger('requests.packages.urllib3.connectionpool').setLevel(logging.WARNING)
    bot = Bot()
    bot.run()


if __name__ == '__main__':
    main()
