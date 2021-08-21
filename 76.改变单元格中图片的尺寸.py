'''
改变单元格中图片的尺寸

setIconSize(QSize(width,height))
'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
class CellImageText(QWidget):
    def __init__(self):
        super(CellImageText, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('在单元格中实现图文混排的效果')
        self.resize(1000, 900)
        layout = QHBoxLayout()
        tableWidget = QTableWidget()
        tableWidget.setRowCount(4)  # 行
        tableWidget.setColumnCount(4)  # 列
        layout.addWidget(tableWidget)

        tableWidget.setHorizontalHeaderLabels(['图片1', '图片2', '图片3','图片4'])

        #让列的宽度和图片的宽度相同
        for i in range(4):
            tableWidget.setColumnWidth(i,300)
        #让行的高度和图片的高度相同
        for i in range(4):
            tableWidget.setRowHeight(i,200)
        for k in range(16):
            i=k/4  #行
            j=k%4  #列
            item=QTableWidgetItem()
            item.setIcon(QIcon('./book%d.png' %k))
            tableWidget.setItem(i,j,item)
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = CellImageText()
    main.show()
    sys.exit(app.exec_())