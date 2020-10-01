import json


class SessionLog():
    def __init__(self):
        self.log_data = []

    def add(self, data: list):
        self.log_data.extend(data)

    def clear(self):
        self.log_data.clear()

    def save_to_file(self, path: str):
        data = json.dumps(self.log_data)
        fw = open(path, "w")
        json.dump(data, fw)

    def set_session_data(self, load_data: list):
        self.log_data = load_data
