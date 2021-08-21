'''
扩展的表格控件（QTableWidget）

每一个cell（单元格）是一个QTableWidgetItem
'''

import sys
from PyQt5.QtWidgets import (QWidget,QTableWidget,QHBoxLayout,QApplication,QTableWidgetItem,QAbstractItemView)
class TableWidgetDemo(QWidget ):
    def __init__(self):
        super(TableWidgetDemo,self).__init__()
        self.setWindowTitle('QListWidget 例子')
        self.resize(500,300)

        layout=QHBoxLayout()
        tablewidget=QTableWidget()
        tablewidget.setRowCount(4)#设置行数
        tablewidget.setColumnCount(3)#设置列数

        layout.addWidget(tablewidget)

        tablewidget.setHorizontalHeaderLabels(['姓名','年龄','籍贯'])
        nameItem=QTableWidgetItem('小米')#创建文本
        tablewidget.setItem(0,0,nameItem)#添加文本到单元格中
        ageItem=QTableWidgetItem('20')
        tablewidget.setItem(0,1,ageItem)
        jgItem=QTableWidgetItem('四川')
        tablewidget.setItem(0,2,jgItem)

        #禁止编辑
        tablewidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        #整行选择
        tablewidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        #调整列和行
        tablewidget.resizeColumnsToContents()
        tablewidget.resizeRowsToContents()
        #隐藏表格头名
        #tablewidget.horizontalHeader().setVisible(False)
        #tablewidget.verticalHeader().setVisible(False)
        #设置头名
        tablewidget.setVerticalHeaderLabels(['a','b','c'])
        #隐藏表格线
        tablewidget.setShowGrid(False)


        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TableWidgetDemo()
    main.show()
    sys.exit(app.exec_())