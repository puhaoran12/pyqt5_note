import sys
from PyQt5.QtWidgets import (QWidget, QTableWidget, QHBoxLayout, QApplication, QTableWidgetItem, QComboBox, QPushButton)
from PyQt5.QtGui import QBrush,QColor,QFont

class PlaceControlInCell(QWidget):
    def __init__(self):
        super(PlaceControlInCell, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('单元格中放置控件')
        self.resize(430, 300)
        layout = QHBoxLayout()
        tableWidget = QTableWidget()
        tableWidget.setRowCount(4)  # 行
        tableWidget.setColumnCount(3)  # 列

        layout.addWidget(tableWidget)

        tableWidget.setHorizontalHeaderLabels(['姓名', '性别', '体重（kg）'])

        newItem=QTableWidgetItem('雷神')
        newItem.setFont(QFont('Times',14,QFont.Black))#设置字体大小，默认颜色为黑色
        newItem.setForeground(QBrush(QColor(255,0,0)))#设置字体颜色
        tableWidget.setItem(0,0,newItem)

        newItem = QTableWidgetItem('女')
        newItem.setForeground(QBrush(QColor(255, 255, 0)))
        newItem.setBackground(QBrush(QColor( 0, 0,255)))#设置背景颜色
        tableWidget.setItem(0, 1, newItem)

        newItem = QTableWidgetItem('160')
        newItem.setFont(QFont('Times', 20, QFont.Black))
        newItem.setForeground(QBrush(QColor( 0, 0,255)))
        tableWidget.setItem(0, 2, newItem)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = PlaceControlInCell()
    main.show()
    sys.exit(app.exec_())
