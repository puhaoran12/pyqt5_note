#QDateTimeEdit
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
class DateTimeEdit(QWidget):
    def __init__(self):
        super(DateTimeEdit,self).__init__()
        self.initUI()
    def initUI(self):
        layout=QVBoxLayout()
        dateTimeEdit1=QDateTimeEdit()#日期时间
        dateTimeEdit2=QDateTimeEdit(QDateTime.currentDateTime())#当前日期时间

        dateEdit=QDateTimeEdit(QDate.currentDate())#当前日期
        timeEdit=QDateTimeEdit(QTime.currentTime())#当前时间

        dateTimeEdit1.setDisplayFormat('yyyy-mm-dd hh:mm:ss')
        dateTimeEdit2.setDisplayFormat('yyyy/mm/dd  hh/mm/ss')

        dateEdit.setDisplayFormat('yyyy.mm.dd')
        timeEdit.setDisplayFormat('hh:mm:ss')

        layout.addWidget(dateTimeEdit1)
        layout.addWidget(dateTimeEdit2)
        layout.addWidget(dateEdit)
        layout.addWidget(timeEdit)

        self.setLayout(layout)


        self.resize(300,90)
        self.setWindowTitle('设置不同风格的日期和时间')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DateTimeEdit()
    main.show()
    sys.exit(app.exec_())