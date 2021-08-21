'''
设置单元格文本对齐方式
需使用setTextAlignment
Qt.AlignmentRight右对齐
Qt.AlignmentBotton下对齐
'''
import sys
from PyQt5.QtWidgets import (QWidget, QTableWidget, QHBoxLayout, QApplication, QTableWidgetItem)
from PyQt5.QtCore import Qt

class CellTextAlignment(QWidget):
    def __init__(self):
        super(CellTextAlignment, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('设置单元格文本对齐方式')
        self.resize(430, 300)
        layout = QHBoxLayout()
        tableWidget = QTableWidget()
        tableWidget.setRowCount(4)  # 行
        tableWidget.setColumnCount(3)  # 列
        layout.addWidget(tableWidget)

        tableWidget.setHorizontalHeaderLabels(['姓名', '性别', '体重（kg）'])

        newItem=QTableWidgetItem('雷神')
        newItem.setTextAlignment(Qt.AlignRight |Qt.AlignBottom)#'|'是或   在右下的位置
        tableWidget.setItem(0,0,newItem)

        self.setLayout(layout)

        self.label21 = QLabel('类型          名称          创建日期          大小          创建者          下载量          评价')
        self.label21.setStyleSheet("background-color:gray")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = CellTextAlignment()
    main.show()
    sys.exit(app.exec_())
