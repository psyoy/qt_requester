import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel
import requests

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QT-Requester")
        self.setGeometry(100, 100, 500, 250)

        self.label = QLabel("Введите url:", self)
        self.label.setFixedWidth(200)
        self.label.setWordWrap(True)
        self.input = QLineEdit(self)
        self.button = QPushButton("Отправить", self)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.input)
        layout.addWidget(self.button)

        self.setLayout(layout)

        self.button.clicked.connect(self.on_button_click)

    def on_button_click(self):
        text = self.input.text()
        json = req(text)
        self.label.setText(f"Ответ:\n {json}")


def req(url):
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())