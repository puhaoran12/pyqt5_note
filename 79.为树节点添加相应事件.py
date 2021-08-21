import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class TreeEvent(QMainWindow):
    def __init__(self,parent=None):
        super(TreeEvent,self).__init__(parent)
        self.setWindowTitle('为树节点添加响应事件')
        self.tree=QTreeWidget()#创建树控件
        self.tree.setColumnCount(2)#创建控件列数
        self.tree.setHeaderLabels(['key','value'])#创建列标签
        #创建节点
        root=QTreeWidgetItem(self.tree)
        root.setText(0,'root')
        root.setText(1,'0')
        #子节点
        child1=QTreeWidgetItem(root)
        child1.setText(0,'child1')
        child1.setText(1,'1')

        child2=QTreeWidgetItem(root)
        child2.setText(0,'child2')
        child2.setText(1,'2')

        child3=QTreeWidgetItem(child2)
        child3.setText(0,'child3')
        child3.setText(1,'3')

        self.tree.clicked.connect(self.onTreeClicked)
        self.setCentralWidget(self.tree)

    def onTreeClicked(self,index):
        item=self.tree.currentItem()
        print(index.row())
        print('key=%s,value=%s' % (item.text(0),item.text(1)))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TreeEvent()
    main.show()
    sys.exit(app.exec_())