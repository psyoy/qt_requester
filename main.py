import sys
import json
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QTextEdit, QLabel
import requests

class GetWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QT-Requester")
        self.setGeometry(100, 100, 500, 250)

        self.output = QTextEdit(self)
        self.output.setFixedWidth(500)
        self.output.setReadOnly(True)

        self.label = QLabel("Enter url for request:", self)
        self.input = QLineEdit(self)
        self.button = QPushButton("Send", self)

        layout = QVBoxLayout()
        layout.addWidget(self.output)
        layout.addWidget(self.label)
        layout.addWidget(self.input)
        layout.addWidget(self.button)

        self.setLayout(layout)

        self.button.clicked.connect(self.on_button_click)

    def on_button_click(self):
        text = self.input.text()
        json_line = req(text)
        self.output.setText(f"{json_line}")


def req(url):
    response = requests.get(url)

    if response.status_code == 200:
        result = json.dumps(response.json(), indent=4)
        return result


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GetWindow()
    window.show()
    sys.exit(app.exec())