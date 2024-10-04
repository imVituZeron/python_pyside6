from PySide6.QtWidgets import QApplication, QGridLayout, QPushButton, QWidget, QMainWindow
import os

def create_file(number:int, sttb):
	os.system(f"touch ~/Documents/file_{number}")
	sttb.showMessage(f"file {number} created")
	
app = QApplication()

main_window = QMainWindow()
status_bar = main_window.statusBar()
main_widget = QWidget()
grid_layout = QGridLayout()
main_window.setCentralWidget(main_widget)
main_window.setWindowTitle("button test with function")

btn1 = QPushButton("File 1")
btn2 = QPushButton("File 2")
btn3 = QPushButton("File 3")
btn1.clicked.connect(lambda: create_file(1, status_bar))
btn2.clicked.connect(lambda: create_file(2, status_bar))
btn3.clicked.connect(lambda: create_file(3, status_bar))

grid_layout.addWidget(btn1, 1, 1, 1, 1)
grid_layout.addWidget(btn2, 2, 1, 1, 1)
grid_layout.addWidget(btn3, 3, 1, 1, 1)

main_widget.setLayout(grid_layout)
main_window.show()
app.exec()
