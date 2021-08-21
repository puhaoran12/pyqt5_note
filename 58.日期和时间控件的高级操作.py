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
        dateTimeEdit1.setMinimumDate(QDate.currentDate().addDays(-365))#最大最小时间设置
        dateTimeEdit1.setMaximumDate(QDate.currentDate().addDays(365))
        self.dateTimeEdit=dateTimeEdit1
        dateTimeEdit2.setCalendarPopup(True)#改变形式


        dateEdit=QDateTimeEdit(QDate.currentDate())#当前日期
        timeEdit=QDateTimeEdit(QTime.currentTime())#当前时间

        dateTimeEdit1.setDisplayFormat('yyyy-MM-dd hh:mm:ss')
        dateTimeEdit2.setDisplayFormat('yyyy/MM/dd  hh/mm/ss')

        dateEdit.setDisplayFormat('yyyy.MM.dd')
        timeEdit.setDisplayFormat('hh:mm:ss')

        dateTimeEdit1.dateChanged.connect(self.onDateChanged)
        dateTimeEdit1.timeChanged.connect(self.onTimeChanged)
        dateTimeEdit1.dateTimeChanged.connect(self.onDateTimeChanged)

        layout.addWidget(dateTimeEdit1)
        layout.addWidget(dateTimeEdit2)
        layout.addWidget(dateEdit)
        layout.addWidget(timeEdit)

        self.btn=QPushButton('获取时间和日期')
        self.btn.clicked.connect(self.onButtonClick)
        layout.addWidget(self.btn)
        self.setLayout(layout)


        self.resize(300,90)
        self.setWindowTitle('设置不同风格的日期和时间')
    #日期变化
    def onDateChanged(self,date):
        print(date)
    #时间变化
    def onTimeChanged(self,time):
        print(time)
    #日期和时间变化
    def onDateTimeChanged(self,datetime):
        print(datetime)

    def onButtonClick(self):
        datetime=self.dateTimeEdit.dateTime()
        print(datetime)

        #最大日期
        print(self.dateTimeEdit.maximumDate())
        #最大日期和时间
        print(self.dateTimeEdit.maximumDateTime())
        #最小日期
        print(self.dateTimeEdit.minimumDate())
        #最小日期和时间
        print(self.dateTimeEdit.minimumDateTime())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DateTimeEdit()
    main.show()
    sys.exit(app.exec_())