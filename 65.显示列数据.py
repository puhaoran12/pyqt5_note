'''
显示列表数据（QListView控件）
'''
from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QListView,QMessageBox
from PyQt5.QtCore import QStringListModel
import sys

class ListViewDemo(QWidget):
    def __init__(self,parent=None):
        super(ListViewDemo,self).__init__(parent)
        self.setWindowTitle('QListView例子')
        self.resize(300,270)
        layout=QVBoxLayout()

        listview=QListView()
        listModel=QStringListModel()
        self.list=['列表项1','列表项2','列表项3']

        listModel.setStringList(self.list)#关联

        listview.setModel(listModel)#关联
        listview.clicked.connect(self.clicked)
        layout.addWidget(listview)

        self.setLayout(layout)

    def clicked(self,item):
        QMessageBox.information(self,'QListView','你选择了：'+self.list[item.row()])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ListViewDemo()
    main.show()
    sys.exit(app.exec_())