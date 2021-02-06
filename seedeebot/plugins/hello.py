from seedeebot.libs.basePlugin import BasePluginV1, ClientInterface, EventInterface


class Hello(BasePluginV1):

    def event_message(self, client: ClientInterface, event: EventInterface):
        pass

