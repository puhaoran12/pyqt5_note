'''
选项卡控件：QTabWidget（多页面的）

'''
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
class TabWidgetDemo(QTabWidget):
    def __init__(self,parent=None):
        super(TabWidgetDemo,self).__init__(parent)
        self.setWindowTitle('选项卡控件：QTabWidget')
        #创建用于显示控件的窗口 创建了3个
        self.tab1=QWidget()
        self.tab2=QWidget()
        self.tab3=QWidget()

        self.addTab(self.tab1,'选项卡1')
        self.addTab(self.tab2, '选项卡2')
        self.addTab(self.tab3, '选项卡3')

        self.tab1UI()#调用(如果没有则不能使用对应的方法)
        self.tab2UI()
        self.tab3UI()

    def tab1UI(self):
        layout=QFormLayout()#在tab1中设置布局
        layout.addRow('姓名',QLineEdit())
        layout.addRow('住址',QLineEdit())
        self.setTabText(0,'联系方式')#动态的改变标题（0表示索引）
        self.tab1.setLayout(layout)#装载

    def tab2UI(self):
        layout=QFormLayout()
        sex=QHBoxLayout()
        sex.addWidget(QRadioButton('男'))
        sex.addWidget(QRadioButton('女'))
        layout.addRow(QLabel('性别'),sex)
        layout.addRow('生日',QLineEdit())
        self.setTabText(1,'个人详细信息')
        self.tab2.setLayout(layout)

    def tab3UI(self):
        layout=QHBoxLayout()
        layout.addWidget(QLabel('科目:'))
        layout.addWidget(QCheckBox('物理'))
        layout.addWidget(QCheckBox('高数'))
        self.setTabText(2,'受教育程度')
        self.tab3.setLayout(layout)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TabWidgetDemo()
    main.show()
    sys.exit(app.exec_())