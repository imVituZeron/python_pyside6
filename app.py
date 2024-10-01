from PySide6.QtWidgets import QApplication, QPushButton

app = QApplication()
button = QPushButton("texto to botao")
button.setStyleSheet('font-size: 40px;')
button.show()

# button2 = QPushButton("textodobotao2)
# button2.show()
app.exec()


