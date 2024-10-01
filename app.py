from PySide6.QtWidgets import QApplication, QGridLayout, QPushButton, QWidget

app = QApplication()

# buttons
button = QPushButton("texto to botao")
button.setStyleSheet('font-size: 40px;')

button2 = QPushButton("textodobotao2")
button2.setStyleSheet('font-size: 40px;')

button3 = QPushButton("textodobotao3")
button3.setStyleSheet('font-size: 40px;')

# layout
layout = QGridLayout()
layout.addWidget(button, 1, 1, 1, 1)
layout.addWidget(button2, 1, 2, 1, 1)
layout.addWidget(button3, 3, 1, 1, 2)

# central
central = QWidget()
central.setLayout(layout)

central.show()
app.exec()

