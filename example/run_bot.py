if __name__ == "__main__":
    # just for easier debugging we are adding root directory to PYTHONPATH
    import sys
    sys.path.insert(1, "..")

# start here
import logging
from seedeebot.conf import settings
from seedeebot.bot import Bot


if __name__ == "__main__":
    kw = {
        'format': '[%(asctime)s] %(message)s',
        'datefmt': '%H:%M:%S %d-%m-%Y',
        'level': logging.DEBUG if settings.DEBUG else logging.INFO,
        'stream': sys.stdout,
    }
    logging.basicConfig(**kw)
    Bot()
