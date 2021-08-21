'''
树控件：QTreeWidget
'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon,QBrush,QColor

class BasicTreeWidget(QMainWindow):
    def __init__(self,parent=None):
        super(BasicTreeWidget,self).__init__(parent)
        self.setWindowTitle('树控件（QTreeWidget）的基本用法')
        #创建树控件
        self.tree=QTreeWidget()
        #为树控件指定列数
        self.tree.setColumnCount(2)
        #指定列标签
        self.tree.setHeaderLabels(['key','value'])
        #添加节点
        root=QTreeWidgetItem(self.tree)#将root放到tree上
        root.setText(0,'根节点')
        root.setIcon(0,QIcon('./book1.png'))#设置图标
        self.tree.setColumnWidth(0,250)#设置列宽度

        #添加子节点1
        child1=QTreeWidgetItem(root)#child1是root的子节点
        child1.setText(0,'子节点1')#子节点第一列
        child1.setText(1,'子节点1的数据')#子节点第二列
        child1.setCheckState(0,Qt.Checked)#为其添加复选框

        #添加子节点2
        child2=QTreeWidgetItem(root)
        child2.setText(0,'子节点2')

        #为child2添加子节点
        child3=QTreeWidgetItem(child2)
        child3.setText(0,'子节点2-1')
        child3.setText(1,'新的值')

        self.setCentralWidget(self.tree)#将树控件充满整个屏幕（将树控件显示出来）

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = BasicTreeWidget()
    main.show()
    sys.exit(app.exec_())