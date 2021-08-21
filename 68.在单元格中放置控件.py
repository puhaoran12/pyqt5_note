'''
通过setItem将文本放到单元格中
通过setCellWidget将控件放到指定的单元格里面
通过setStyleSheet设置控件的样式
'''

import sys
from PyQt5.QtWidgets import (QWidget,QTableWidget,QHBoxLayout,QApplication,QTableWidgetItem,QComboBox,QPushButton)

class PlaceControlInCell(QWidget):
    def __init__(self):
        super(PlaceControlInCell,self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('单元格中放置控件')
        self.resize(430,300)
        layout=QHBoxLayout()
        tableWidget=QTableWidget()
        tableWidget.setRowCount(4)#行
        tableWidget.setColumnCount(3)#列


        layout.addWidget(tableWidget)

        tableWidget.setHorizontalHeaderLabels(['姓名','性别','体重（kg）'])
        tableWidget.setRowHeight(0, 300)  # 改变行的高度   第一个参数是行的索引，第二个为改变高度的值
        tableWidget.setColumnWidth(2, 300)  # 改变列的高度   第一个参数是列的索引，第二个为改变高度的值
        textItem=QTableWidgetItem('小米')
        tableWidget.setItem(0,0,textItem)

        comBox=QComboBox()
        comBox.addItem('男')
        comBox.addItem('女')


        #QSS
        comBox.setStyleSheet('QComboBox{margin:3px)}')
        tableWidget.setCellWidget(0,1,comBox)

        modifyButton=QPushButton('修改')
        modifyButton.setDown(True)
        modifyButton.setStyleSheet('QComboBox{margin：3px}')
        tableWidget.setCellWidget(0,2,modifyButton)

        self.setLayout(layout)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = PlaceControlInCell()
    main.show()
    sys.exit(app.exec_())
