from PySide6.QtWidgets import (
    QMainWindow,
    QLabel,
    QGridLayout,
    QWidget,
    QComboBox,
    QSpinBox,
    QCheckBox,
    QPushButton,
    QLineEdit
)
from PySide6.QtGui import Qt
from cheats import runes, rune_result


class Calculadora(QMainWindow):
    """ Interfaz de la calculadora, contiene 2 selectores de runa y un selector de cantidad. """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("D2-Calculadora Runas")
        self.setFixedSize(300,270)

        # --- Primera Runa entrada --- 
        runa1_ent = QLabel("Primera Runa:")
        runa1_ent.setFixedSize(100,40)
        runa1_ent.setAlignment(Qt.AlignmentFlag.AlignCenter)

        ent1 = QComboBox()
        for i in runes().keys():
            ent1.addItem(i)
        ent1.setFixedSize(75,30)

        # --- Segunda Runa entrada --- 
        runa2_ent = QLabel("Segunda Runa:")
        runa2_ent.setFixedSize(100,40)
        runa2_ent.setAlignment(Qt.AlignmentFlag.AlignCenter)

        ent2 = QComboBox()
        for i in runes().keys():
            ent2.addItem(i)
        ent2.setFixedSize(75,30)

        # --- Ajusta la cantidad a calcular --- 
        cant_show = QCheckBox("Ajustar cantidad")
        cant_show.clicked.connect(lambda e: self.cant.show() if e else self.cant_reset())

        self.cant = QSpinBox()
        self.cant.setMinimum(1)
        self.cant.setMaximum(99)
        self.cant.hide()

        # --- Resultado ---
        self.result = QLineEdit()
        self.result.setEnabled(False)
        self.result.setText("0")
        self.result.setFixedWidth(150)
        self.result.setStyleSheet("color: black; background-color:rgb(255,255,255)")
        self.result.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # --- Boton calcular --- 
        self.boton_calcular = QPushButton("Calcular")
        self.boton_calcular.setMaximumWidth(150)
        self.boton_calcular.clicked.connect(lambda e: 
            self.result.setText(f"{round(self.resultado(ent1.currentText(),ent2.currentText()))}")
        )

        # --- Layout ---
        layout = QGridLayout()
        layout.addWidget(runa1_ent,1,1,alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(cant_show,1,0,alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.cant,2,0,alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(ent1,2,1,alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(runa2_ent,3,1,alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(ent2,4,1,alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.boton_calcular,5,1,alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.result,6,1,alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.setSpacing(10)

        # --- Widget y carga ---
        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)
        self.show()
        

    def cant_reset(self) -> None:
        """ - Esconde y setea a '1' el ajuste de cantidad
        """
        self.cant.setValue(1)
        self.cant.hide()

    def resultado(self,r1,r2) -> float:
        runas=runes()
        r1=runas[r1]
        r2=runas[r2]
        cant=self.cant.value()

        return rune_result(r1,r2,cant)