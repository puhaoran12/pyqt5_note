'''
安列排序
1.按那一列排序
2.排序类型：升序或者降序
sortItems方法进行排序
columnIndex：列索引
orderType：排序类型
'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
class ColumnSort(QWidget):
    def __init__(self):
        super(ColumnSort, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('单元格中放置控件')
        self.resize(430, 300)
        layout = QHBoxLayout()
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(4)  # 行
        self.tableWidget.setColumnCount(3)  # 列

        layout.addWidget(self.tableWidget)

        self.tableWidget.setHorizontalHeaderLabels(['姓名', '性别', '体重（kg）'])

        newItem=QTableWidgetItem('张三')
        self.tableWidget.setItem(0,0,newItem)
        newItem = QTableWidgetItem('男')
        self.tableWidget.setItem(0, 1, newItem)
        newItem = QTableWidgetItem('165')
        self.tableWidget.setItem(0, 2, newItem)

        newItem = QTableWidgetItem('李四')
        self.tableWidget.setItem(1, 0, newItem)
        newItem = QTableWidgetItem('nv')
        self.tableWidget.setItem(1, 1, newItem)
        newItem = QTableWidgetItem('160')
        self.tableWidget.setItem(1, 2, newItem)

        newItem = QTableWidgetItem('王五')
        self.tableWidget.setItem(2, 0, newItem)
        newItem = QTableWidgetItem('男')
        self.tableWidget.setItem(2, 1, newItem)
        newItem = QTableWidgetItem('170')
        self.tableWidget.setItem(2, 2, newItem)

        self.button=QPushButton('排序')
        self.button.clicked.connect(self.order)
        layout.addWidget(self.button)

        self.orderType=Qt.DescendingOrder#排序类型（降序）
        self.setLayout(layout)

    def order(self):
        if self.orderType==Qt.DescendingOrder:
            self.orderType=Qt.AscendingOrder#如果排序类型为降序，则为升序
        else:
            self.orderType=Qt.DescendingOrder
        self.tableWidget.sortItems(2,self.orderType)#将第三列排序


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ColumnSort()
    main.show()
    sys.exit(app.exec_())
