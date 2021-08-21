#日历控件：QCalendarWidet
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
class MyCalendar(QWidget):
    def __init__(self):
        super(MyCalendar,self).__init__()
        self.initUI()
    def initUI(self):
        self.cal=QCalendarWidget(self)
        self.cal.setMinimumDate(QDate(1988,1,1))
        self.cal.setMaximumDate(QDate(2088,1,1))

        self.cal.setGridVisible(True)#日历以网格形式呈现
        self.cal.move(20,20)
        self.cal.resize(1000,1000)
        #槽：关联
        self.cal.clicked.connect(self.showDate)
        self.label=QLabel(self)
        date=self.cal.selectedDate()#选择的日期
        self.label.setText(date.toString('yyyy-MM-dd dddd'))
        self.label.move(20,300)
        self.setWindowTitle('日历演示')
    #添加单击事件
    def showDate(self,date):
        self.label.setText((date.toString('yyyy-MM-dd dddd')))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MyCalendar()
    main.show()
    sys.exit(app.exec_())