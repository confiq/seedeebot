"""
the idea is to have something similar to django settings: https://docs.djangoproject.com/en/3.1/topics/settings/#using-settings-in-python-code
but much simpler

Look at global_settings.py for all variables possible.
In order to overwrite you can have env variable starting with SEEDEEBOT_[variable] or change it right after init.
"""

from seedeebot.conf import global_settings
import logging
import os
try:
    import local_settings
except ImportError:
    pass

logger = logging.getLogger(__name__)


class LazySettings:
    _wrapped = None

    def __init__(self):
        pass

    def __getattr__(self, item):
        if self._wrapped is None:
            self._setup()
        return getattr(self._wrapped, item)

    def get(self, key, default=None):
        if hasattr(self._wrapped, key):
            return getattr(self, key)
        else:
            return default

    def _setup(self):
        logger.debug('initiating the configuration')
        self._wrapped = SettingsObject()
        self._validation()

    def _validation(self):
        if not self.get('SLACK_TOKEN'):
            logger.error('Bot User OAuth Access Token is missing, please add it as OS environment "SEEDEEBOT_SLACK_TOKEN"')


class SettingsObject:
    def __init__(self):
        try:
            local_settings = local_settings
        except NameError:
            local_settings = {}
        for conf_key in dir(global_settings):
            if conf_key.isupper():
                # explicit has always the priority
                if os.environ.get(f"SEEDEEBOT_{conf_key}", False):
                    setattr(self, conf_key, os.environ[f"SEEDEEBOT_{conf_key}"])
                elif conf_key in local_settings:
                    setattr(self, conf_key, getattr(local_settings, conf_key))
                else:
                    setattr(self, conf_key, getattr(global_settings, conf_key))


settings = LazySettings()
