'''
添加，修改和删除树控件中的节点
'''
import sys
from PyQt5.QtWidgets import *

class ModifyTree(QWidget):
    def __init__(self,parent=None):
        super(ModifyTree,self).__init__(parent)
        self.setWindowTitle('TreeWidget 例子')

        layout=QHBoxLayout()
        addBtn=QPushButton('添加节点')
        updateBtn=QPushButton('修改节点')
        deleteBtn=QPushButton('删除节点')

        layout.addWidget(addBtn)
        layout.addWidget(updateBtn)
        layout.addWidget(deleteBtn)

        addBtn.clicked.connect(self.addNode)
        updateBtn.clicked.connect(self.updateNode)
        deleteBtn.clicked.connect(self.deleteNode)

        self.tree = QTreeWidget()  # 创建树控件
        self.tree.setColumnCount(2)  # 创建控件列数
        self.tree.setHeaderLabels(['key', 'value'])  # 创建列标签
        # 创建节点
        root = QTreeWidgetItem(self.tree)
        root.setText(0, 'root')
        root.setText(1, '0')
        # 子节点
        child1 = QTreeWidgetItem(root)
        child1.setText(0, 'child1')
        child1.setText(1, '1')

        child2 = QTreeWidgetItem(root)
        child2.setText(0, 'child2')
        child2.setText(1, '2')

        child3 = QTreeWidgetItem(child2)
        child3.setText(0, 'child3')
        child3.setText(1, '3')


        mainlayout=QVBoxLayout(self)
        mainlayout.addLayout(layout)
        mainlayout.addWidget(self.tree)
        self.setLayout(mainlayout)



        def onTreeClicked(self, index):
            item = self.tree.currentItem()
            print(index.row())
            print('key=%s,value=%s' % (item.text(0), item.text(1)))

    #添加节点
    def addNode(self):
        print('添加节点')
        item=self.tree.currentItem()
        print(item)
        node=QTreeWidgetItem(item)
        node.setText(0,'新节点')
        node.setText(1,'新值')
    def updateNode(self):
        print('修改节点')
        item=self.tree.currentItem()
        item.setText(0,'修改节点')
        item.setText(1,'值已经被修改')
    def deleteNode(self):
        item=self.tree.currentItem()
        root=self.tree.invisibleRootItem()
        for item in self.tree.selectedItems():
            (item.parent() or root).removeChild(item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ModifyTree()
    main.show()
    sys.exit(app.exec_())