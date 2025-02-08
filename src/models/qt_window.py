from PyQt6.QtWidgets import (
    QMainWindow, QPushButton, QTextEdit, QLineEdit, QVBoxLayout, QWidget, QHBoxLayout
)
from .response import ResponseWorker

class HttpRequester(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QT-Requester")
        self.resize(600, 400)

        self.layout = QVBoxLayout()

        self.get_button = QPushButton("GET")
        self.post_button = QPushButton("POST")
        self.get_button.clicked.connect(self.setup_get_ui)
        self.post_button.clicked.connect(self.setup_post_ui)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.get_button)
        button_layout.addWidget(self.post_button)

        self.layout.addLayout(button_layout)

        self.response_area = QTextEdit()
        self.response_area.setReadOnly(True)
        self.layout.addWidget(self.response_area)

        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("Enter URL for request")
        self.layout.addWidget(self.url_input)

        self.json_input = QTextEdit()
        self.json_input.setPlaceholderText("Enter JSON for POST request")
        self.layout.addWidget(self.json_input)
        self.json_input.hide()

        self.send_button = QPushButton("Send")
        self.send_button.clicked.connect(self.send_request)
        self.layout.addWidget(self.send_button)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

        self.current_request_type = "GET"

    def setup_get_ui(self):
        self.json_input.hide()
        self.current_request_type = "GET"

    def setup_post_ui(self):
        self.json_input.show()
        self.current_request_type = "POST"

    def send_request(self):
        url = self.url_input.text().strip()
        json_data = self.json_input.toPlainText().strip() if self.current_request_type == "POST" else ""

        if not url:
            self.response_area.setText("URL is required!")
            return

        self.worker = ResponseWorker(url, self.current_request_type, json_data)
        self.worker.finished.connect(self.handle_response)
        self.worker.start()

    def handle_response(self, response_text, error_text):
        if error_text:
            self.response_area.setText(f"Error: {error_text}")
        else:
            self.response_area.setText(response_text)
