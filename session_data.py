from PySide2.QtWidgets import QFileDialog
import json

class SessionLog():
    def __init__(self):
        self.log_data = []

    def Add(self, data):
        self.log_data.append(data)

    def Clear(self):
        self.log_data.clear()

    def SaveSettion(self):
        save_file = QFileDialog.getSaveFileName(None,"save as","*.log")
        data = json.dumps(self.log_data)
        fw = open(save_file[0],"w")
        json.dump(data,fw)


