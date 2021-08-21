from PyQt5.QtWidgets import *
import sys
class QSSSubControl(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QSS子控件选择器')
        combo=QComboBox(self)
        combo.setObjectName("myComboBox")#设置窗口id：MainWindow
        combo.addItem('window')
        combo.addItem('linux')
        combo.addItem('ios')

        combo.move(50,50)
        self.setGeometry(100,100,100,200)

if __name__ == '__main__':
        app = QApplication(sys.argv)
        main = QSSSubControl()
        qssStyle='''
           QComboBox#myComboBox::drop-down{
             image:url(./images/book.png)
           } 
        '''
        main.show()
        sys.exit(app.exec_())