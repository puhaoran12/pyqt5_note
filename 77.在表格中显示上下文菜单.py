'''
1.如何让弹出菜单-QMenu.exec_
2.如何在满足条件的情况下弹出菜单

'''
import sys
from PyQt5.QtWidgets import (QMenu,QPushButton,QWidget,QTableWidget,QHBoxLayout,QApplication,QTableWidgetItem,QHeaderView)
from PyQt5.QtCore import QObject,Qt

class TableWidgetContextMenu(QWidget):
    def __init__(self):
        super(TableWidgetContextMenu,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('在表格中显示上下文菜单')
        self.resize(500,300)
        layout=QHBoxLayout()
        self.tableWidget=QTableWidget()
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(3)
        layout.addWidget(self.tableWidget)

        self.tableWidget.setHorizontalHeaderLabels(['姓名','年龄','体重'])

        newItem = QTableWidgetItem('李宁')
        self.tableWidget.setItem(0, 0, newItem)
        newItem = QTableWidgetItem('男')
        self.tableWidget.setItem(0, 1, newItem)
        newItem = QTableWidgetItem('160')
        self.tableWidget.setItem(0, 2, newItem)

        newItem = QTableWidgetItem('李四')
        self.tableWidget.setItem(1, 0, newItem)
        newItem = QTableWidgetItem('女')
        self.tableWidget.setItem(1, 1, newItem)
        newItem = QTableWidgetItem('150')
        self.tableWidget.setItem(1, 2, newItem)

        newItem = QTableWidgetItem('李')
        self.tableWidget.setItem(2, 0, newItem)
        newItem = QTableWidgetItem('男')
        self.tableWidget.setItem(2, 1, newItem)
        newItem = QTableWidgetItem('180')
        self.tableWidget.setItem(2, 2, newItem)

        self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)#允许tableWidget控件单击后回响应一个事件
        self.tableWidget.customContextMenuRequested.connect(self.generateMenu)#关联

        self.setLayout(layout)

    def generateMenu(self,pos):
        print(pos)
        for i in self.tableWidget.selectionModel().selection().indexes():
            rowNum=i.row()#索引选择的行数
        #如果选择的行索引小于2，弹出上下文菜单
        if rowNum<2:
            menu=QMenu()
            item1=menu.addAction('菜单项1')
            item2=menu.addAction('菜单项2')
            item3=menu.addAction('菜单项3')
            screenPos=self.tableWidget.mapToGlobal(pos)#窗口坐标和屏幕坐标转换
            print(screenPos)
            #被阻塞
            action=menu.exec(screenPos)
            if action==item1:
                print('选择了第1个菜单项',self.tableWidget.item(rowNum,0).text(),self.tableWidget.item(rowNum,1).text(),self.tableWidget.item(rowNum,2).text())

            elif action == item2:
                print('选择了第2个菜单项', self.tableWidget.item(rowNum, 0).text(), self.tableWidget.item(rowNum, 1).text(),
                      self.tableWidget.item(rowNum, 2).text())

            elif action == item3:
                print('选择了第3个菜单项', self.tableWidget.item(rowNum, 0).text(), self.tableWidget.item(rowNum, 1).text(),
                      self.tableWidget.item(rowNum, 2).text())
            else:
                return

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TableWidgetContextMenu()
    main.show()
    sys.exit(app.exec_())
