import json


class SessionLog():
    def __init__(self):
        self.log_data = []

    def Add(self, data: list):
        self.log_data.extend(data)

    def Clear(self):
        self.log_data.clear()

    def SaveToFile(self, path: str):
        data = json.dumps(self.log_data)
        fw = open(path, "w")
        json.dump(data, fw)

    def SetSessionData(self, load_data: list):
        self.log_data = load_data
