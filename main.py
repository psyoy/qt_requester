import sys
from src.models.qt_window import HttpRequester
from PyQt6.QtWidgets import QApplication


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HttpRequester()
    window.show()
    sys.exit(app.exec())
