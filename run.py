import sys
from PySide6.QtWidgets import QApplication
from ui import Calculadora


if __name__ == "__main__":
    app=QApplication(sys.argv)
    window=Calculadora()
    sys.exit(app.exec())