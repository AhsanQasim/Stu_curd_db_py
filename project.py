import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import sqlite3
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
#connection
conn = sqlite3.connect('studentdb.db')
cursor = conn.cursor()
print("successfull")
command1="""CREATE TABLE IF NOT EXISTS students(Stuid INTEGER PRIMARY KEY AUTOINCREMENT, firstname TEXT, lastname TEXT, streetno TEXT, city TEXT, state TEXT, email TEXT, telephone INTEGER)"""
cursor.execute(command1)
count=0

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Student Task'
        self.left = 200
        self.top = 200
        self.width = 600
        self.height = 500
        self.window()

    def window(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)
        # Firstname
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Firstname:")
        self.label.move(20, 20)

        self.ftextbox = QLineEdit(self)
        self.ftextbox.move(20, 50)
        self.ftextbox.resize(90, 25)
        # Create a button in the window
        self.button1 = QPushButton('Display All', self)
        self.button1.move(200, 50)
        # connect button to function on_click
        self.button1.clicked.connect(self.on_click1dis)
        # Display label
        self.labeldis = QtWidgets.QLabel(self)
        self.labeldis.setText("")
        self.labeldis.move(200, 100)
        self.labeldis.resize(400,400)
        self.labeldis.setAlignment(QtCore.Qt.AlignLeft)

        #name(stuidlabel)
        self.labeldisplay = QtWidgets.QLabel(self)
        self.labeldisplay.setText("Fullname(stuid)")
        self.labeldisplay.move(200, 70)
        # Create a button in the window
        self.button2 = QPushButton('Delete Student', self)
        self.button2.move(330, 50)
        # connect button to function on_click
        self.button2.clicked.connect(self.on_click2)
        self.stutextbox = QLineEdit(self)
        self.stutextbox.move(450, 50)
        self.stutextbox.resize(90, 25)

        # lastname
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Lastname:")
        self.label.move(20, 80)

        self.ltextbox = QLineEdit(self)
        self.ltextbox.move(20, 110)
        self.ltextbox.resize(90, 25)

        # Street
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Street no:")
        self.label.move(20, 130)

        self.stextbox = QLineEdit(self)
        self.stextbox.move(20, 160)
        self.stextbox.resize(90, 25)

        # City
        self.label = QtWidgets.QLabel(self)
        self.label.setText("City:")
        self.label.move(20, 190)

        self.ctextbox = QLineEdit(self)
        self.ctextbox.move(20, 220)
        self.ctextbox.resize(90, 25)

        # State
        self.label = QtWidgets.QLabel(self)
        self.label.setText("State:")
        self.label.move(20, 250)

        self.sstextbox = QLineEdit(self)
        self.sstextbox.move(20, 280)
        self.sstextbox.resize(90, 25)

        # Email
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Email:")
        self.label.move(20, 310)

        self.etextbox = QLineEdit(self)
        self.etextbox.move(20, 340)
        self.etextbox.resize(90, 25)

        # Telephone
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Telephone:")
        self.label.move(20, 370)

        self.ttextbox = QLineEdit(self)
        self.ttextbox.move(20, 400)
        self.ttextbox.resize(90, 25)

        # Create a button in the window
        self.button = QPushButton('Add Student', self)
        self.button.move(20, 450)
        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        command2 = """INSERT INTO students(firstname, lastname, streetno, city, state, email, telephone) \
      VALUES ("{firstname}", "{lastname}", "{street}", "{city}","{state}","{email}","{telephone}" )""".format(firstname = self.ftextbox.text(),
        lastname = self.ltextbox.text(),
        street = self.stextbox.text(),
        state = self.sstextbox.text(),
        city = self.ctextbox.text(),
        telephone = self.ttextbox.text(),
        email = self.etextbox.text())
        print(command2)
        cursor.execute(command2)
        self.ftextbox.setText("")
        self.ltextbox.setText("")
        self.stextbox.setText("")
        self.sstextbox.setText("")
        self.ctextbox.setText("")
        self.ttextbox.setText("")
        self.etextbox.setText("")

        cursor.execute("SELECT * FROM students")
        results=cursor.fetchall()

        print(results)

    @pyqtSlot()
    def on_click1dis(self):
        #cursor.execute("SELECT firstname+' '+lastname+'('+cast(Stuid as varchar)+')' from students")
        cursor.execute("SELECT firstname,lastname,cast(Stuid as varchar) FROM students")
        results = cursor.fetchall()
        length=len(results)
        print(length)
        i=0
        mystring=""
        while i<length:
            result=results[i]
            print(result)
            mystring=mystring+result[0]+" "+result[1]+"("+result[2]+")"+"\n"
            i=i+1
        print(mystring)
        print(mystring)
        self.labeldis.setText(mystring)

    @pyqtSlot()
    def on_click2(self):
        command3="DELETE FROM students WHERE stuid={stuu};".format(stuu = self.stutextbox.text())
        cursor.execute(command3)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
