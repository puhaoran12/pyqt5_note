'''
合并单元格的方法：setSpan(row,col,要合并的行数，要合并的列数)   括号中为四个参数：row，col都是起始的位置
'''
import sys
from PyQt5.QtWidgets import (QWidget, QTableWidget, QHBoxLayout, QApplication, QTableWidgetItem)
from PyQt5.QtCore import Qt

class CellTextAlignment(QWidget):
    def __init__(self):
        super(CellTextAlignment, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('合并单元格')
        self.resize(430, 300)
        layout = QHBoxLayout()
        tableWidget = QTableWidget()
        tableWidget.setRowCount(4)  # 行
        tableWidget.setColumnCount(3)  # 列
        layout.addWidget(tableWidget)

        tableWidget.setHorizontalHeaderLabels(['姓名', '性别', '体重（kg）'])

        newItem=QTableWidgetItem('雷神')
        tableWidget.setItem(0,0,newItem)
        tableWidget.setSpan(0,0,3,1)

        newItem = QTableWidgetItem('女')
        tableWidget.setItem(0, 1, newItem)
        tableWidget.setSpan(0, 1, 2, 1)



        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = CellTextAlignment()
    main.show()
    sys.exit(app.exec_())
