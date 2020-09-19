class EventDispatcher():
    def __init__(self):
        self.__action_events = {}

    def AddEvent(self, key: str, event):
        self.__action_events[key] = event

    def DeleteEvent(self, key: str):
        self.__action_events.pop(key)

    def Call(self, key: str, arg_data):
        event = self.__action_events[key]
        event(arg_data)


dispatcher = EventDispatcher()


def InitDispatcher():
    print("start dispatcher")


def AddEvent(key: str, event):
    dispatcher.AddEvent(key, event)


def DeleteEvent(key: str):
    dispatcher.DeleteEvent(key)


def EmitEvent(key: str, arg_data):
    dispatcher.Call(key, arg_data)
