'''
setColumnWidth
setRowHeight
'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QBrush,QColor,QFont
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

        tableWidget.setRowHeight(0,150)#改变行的高度   第一个参数是行的索引，第二个为改变高度的值
        tableWidget.setColumnWidth(2,600)#改变列的高度   第一个参数是列的索引，第二个为改变高度的值
        newItem = QTableWidgetItem('雷神')
        newItem.setFont(QFont('Times', 40, QFont.Black))  # 设置字体大小，默认颜色为黑色
        newItem.setForeground(QBrush(QColor(255, 0, 0)))  # 设置字体颜色
        tableWidget.setItem(0, 0, newItem)

        newItem = QTableWidgetItem('女')
        newItem.setForeground(QBrush(QColor(255, 255, 0)))
        newItem.setBackground(QBrush(QColor(0, 0, 255)))  # 设置背景颜色
        tableWidget.setItem(0, 1, newItem)

        newItem = QTableWidgetItem('160')
        newItem.setFont(QFont('Times', 60, QFont.Black))
        newItem.setForeground(QBrush(QColor(0, 0, 255)))
        tableWidget.setItem(0, 2, newItem)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = CellTextAlignment()
    main.show()
    sys.exit(app.exec_())
