from PySide6.QtWidgets import QApplication, QGridLayout, QPushButton, QWidget, QMainWindow, QLabel, QLineEdit
import mysql.connector

def fetch_the_app_informatiom(input_field, gl):
   query = f"select * from apps where app_name = '{input_field.text()}';"
   conn = mysql.connector.connect(host="172.27.0.102", user="root", database="rbdocker", password="Gj49h3kh")
   cursor = conn.cursor()
   cursor.execute(query)
   rslt = cursor.fetchall()

   input_field.clear() # cleaning the input field

   label_name = QLabel(text=f"Name: {rslt[0][1]}")
   label_ip = QLabel(text=f"IP: {rslt[0][2]}")
   label_nginx_port = QLabel(text=f"Nginx Port: {rslt[0][3]}")
   label_php_version = QLabel(text=f"PHP Version: {rslt[0][4]}")
   label_database_type = QLabel(text=f"Type: {rslt[0][5]}")

   gl.addWidget(label_name, 3, 1, 1, 1)
   gl.addWidget(label_ip, 4, 1, 1, 1)
   gl.addWidget(label_nginx_port, 5, 1, 1, 1)
   gl.addWidget(label_php_version, 6, 1, 1, 1)
   gl.addWidget(label_database_type, 7, 1, 1, 1)


app = QApplication()

main_window = QMainWindow() # main
main_widget = QWidget() # widget central
grid_layout = QGridLayout() # layout
input_field = QLineEdit()

main_window.setCentralWidget(main_widget)
main_window.setWindowTitle("table tests") #title

btn_trigger = QPushButton("Get information")
btn_trigger.clicked.connect(
   lambda: fetch_the_app_informatiom(
      input_field,
      grid_layout
   )
)
   
grid_layout.addWidget(input_field, 1, 1, 1, 1)
grid_layout.addWidget(btn_trigger, 2, 1, 1, 1)

main_widget.setLayout(grid_layout)
main_window.show()
app.exec()
