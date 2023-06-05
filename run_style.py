import sys
from ui import Calculadora
from PySide6.QtWidgets import QApplication
from qt_material import apply_stylesheet


if __name__=="__main__":
    app=QApplication(sys.argv)
    window=Calculadora()
    apply_stylesheet(window, theme='dark_purple.xml')
    sys.exit(app.exec())