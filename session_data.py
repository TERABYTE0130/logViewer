import json

class SessionLogData():
    def __init__(self):
        self.log_data = []

    def AddLog(self, data):
        self.log_raw_data.append(data)

    def ClearLog(self):
        self.log_data.clear()



