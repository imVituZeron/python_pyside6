from PySide6.QtWidgets import QApplication, QGridLayout, QPushButton, QWidget, QMainWindow

def slot_example(sb):
	sb.showMessage("clickado!")
app = QApplication()

# main window
window = QMainWindow()
central = QWidget()
window.setCentralWidget(central)
window.setWindowTitle("haha")

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

# status bar
status_bar = window.statusBar()
status_bar.showMessage("haha")

# menu
menu = window.menuBar()
first_menu = menu.addMenu('Home')
first_action = first_menu.addAction("hi")
first_action.triggered.connect(lambda: slot_example(status_bar))

# central
central.setLayout(layout)

window.show()
app.exec()

