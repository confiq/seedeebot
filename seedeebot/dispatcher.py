import logging

logger = logging.getLogger(__name__)


class MessageDispatcher(object):
    def __init__(self):
        pass


def unicode_compact(func):
    """
    Make sure the first parameter of the decorated method to be a unicode
    object.
    """


class Message(object):
    def __init__(self, slackclient, body):
        self._client = slackclient
        self._body = body
        self._plugins = PluginsManager()

    def _get_user_id(self):
        if 'user' in self._body:
            return self._body['user']

        return self._client.find_user_by_name(self._body['username'])

    @unicode_compact
    def _gen_at_message(self, text):
        text = u'<@{}>: {}'.format(self._get_user_id(), text)
        return text

    @unicode_compact
    def gen_reply(self, text):
        chan = self._body['channel']
        if chan.startswith('C') or chan.startswith('G'):
            return self._gen_at_message(text)
        else:
            return text

    @unicode_compact
    def reply_webapi(self, text, attachments=None, as_user=True, in_thread=None):
        """
            Send a reply to the sender using Web API

            (This function supports formatted message
            when using a bot integration)

            If the message was send in a thread, answer in a thread per default.
        """
        if in_thread is None:
            in_thread = 'thread_ts' in self.body

        if in_thread:
            self.send_webapi(text, attachments=attachments, as_user=as_user, thread_ts=self.thread_ts)
        else:
            text = self.gen_reply(text)
            self.send_webapi(text, attachments=attachments, as_user=as_user)

    @unicode_compact
    def send_webapi(self, text, attachments=None, as_user=True, thread_ts=None):
        """
            Send a reply using Web API

            (This function supports formatted message
            when using a bot integration)
        """
        self._client.send_message(
            self._body['channel'],
            text,
            attachments=attachments,
            as_user=as_user,
            thread_ts=thread_ts)

    @unicode_compact
    def reply(self, text, in_thread=None):
        """
            Send a reply to the sender using RTM API

            (This function doesn't supports formatted message
            when using a bot integration)

            If the message was send in a thread, answer in a thread per default.
        """
        if in_thread is None:
            in_thread = 'thread_ts' in self.body

        if in_thread:
            self.send(text, thread_ts=self.thread_ts)
        else:
            text = self.gen_reply(text)
            self.send(text)

    @unicode_compact
    def direct_reply(self, text):
        """
            Send a reply via direct message using RTM API

        """
        channel_id = self._client.open_dm_channel(self._get_user_id())
        self._client.rtm_send_message(channel_id, text)


    @unicode_compact
    def send(self, text, thread_ts=None):
        """
            Send a reply using RTM API

            (This function doesn't supports formatted message
            when using a bot integration)
        """
        self._client.rtm_send_message(self._body['channel'], text, thread_ts=thread_ts)

    def react(self, emojiname):
        """
           React to a message using the web api
        """
        self._client.react_to_message(
            emojiname=emojiname,
            channel=self._body['channel'],
            timestamp=self._body['ts'])

    @property
    def channel(self):
        return self._client.get_channel(self._body['channel'])

    @property
    def body(self):
        return self._body

    @property
    def user(self):
        return self._client.get_user(self._body['user'])

    @property
    def thread_ts(self):
        try:
            thread_ts = self.body['thread_ts']
        except KeyError:
            thread_ts = self.body['ts']

        return thread_ts

    def docs_reply(self):
        reply = [u'    • `{0}` {1}'.format(v.__name__, v.__doc__ or '')
                 for _, v in
                 six.iteritems(self._plugins.commands['respond_to'])]
        return u'\n'.join(reply)
