class EventDispatcher:
    def __init__(self):
        self.__action_events = {}

    def add_event(self, key: str, event):
        if key in self.__action_events:
            if event in self.__action_events[key]:
                print("key{}:event{} is contain event".format(key, event))
                return
            self.__action_events[key].append(event)
        else:
            self.__action_events[key] = []
            self.__action_events[key].append(event)

    def delete_event(self, key: str, event):
        if not key in self.__action_events:
            print("key {} not found".format(key))
            return
        function_array = self.__action_events[key]
        index = function_array.index(event)
        function_array.pop(index)
        if len(function_array) == 0:
            self.__action_events.pop(key)

    def call(self, key: str, arg_data):
        event = self.__action_events[key]
        for func in event:
            func(arg_data)


dispatcher = EventDispatcher()


def startup_dispatcher():
    print("start dispatcher")


def add_event(key: str, event):
    dispatcher.add_event(key, event)


def delete_event(key: str, event):
    dispatcher.delete_event(key, event)


def emit_event(key: str, arg_data):
    dispatcher.call(key, arg_data)
