from PySide6.QtWidgets import QApplication, QGridLayout, QPushButton, QWidget, QMainWindow, QTableWidget, QTableWidgetItem

app = QApplication()

main_window = QMainWindow() # main
main_widget = QWidget() # widget central
grid_layout = QGridLayout() # layout

main_window.setCentralWidget(main_widget)
main_window.setWindowTitle("table tests") #title

# table
table = QTableWidget(1, 4)
table.setHorizontalHeaderLabels(["Name", "Ip","Port", "Database type"])
item_name = QTableWidgetItem("crm")
item_ip = QTableWidgetItem("172.27.0.2")
item_port = QTableWidgetItem("8002")
item_database_type = QTableWidgetItem("mysql")

table.setItem(1, 0, item_name)
table.setItem(1, 1, item_ip)
table.setItem(1, 2, item_port)
table.setItem(1, 3, item_database_type)

grid_layout.addWidget(table, 1, 1, 1, 1)

main_widget.setLayout(grid_layout)
main_window.show()
app.exec()