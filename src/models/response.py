import json
import requests
from PyQt6.QtCore import QThread, pyqtSignal

class ResponseWorker(QThread):
    finished = pyqtSignal(str, str)

    def __init__(self, url, request_type, json_data=""):
        super().__init__()
        self.url = url
        self.request_type = request_type
        self.json_data = json_data

    def run(self):
        try:
            if self.request_type == "GET":
                response = requests.get(self.url)
            elif self.request_type == "POST":
                response = requests.post(self.url, json=json.loads(self.json_data) if self.json_data else {})

            pretty_json = json.dumps(response.json(), indent=4)
            self.finished.emit(pretty_json, "")  # Успешный запрос
        except requests.exceptions.RequestException as e:
            self.finished.emit("", str(e))  # Ошибка запроса
