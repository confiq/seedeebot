
# inspired from here: https://packaging.python.org/guides/creating-and-discovering-plugins/

class ClientInterface:
    def __init__(self): pass


class EventInterface:
    def __init__(self): pass


class BasePluginV1:
    def __init__(self):
        pass

    def event_message(self, client: ClientInterface, event: EventInterface) -> None: pass
