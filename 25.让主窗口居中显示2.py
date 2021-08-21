import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QDesktopWidget
from PyQt5.QtGui import QIcon

class CentreForm(QMainWindow):
    def __init__(self,parent=None):
        super(CentreForm,self).__init__(parent)

        #设置主窗口
        self.setWindowTitle('窗口居中')
        #设置窗口尺寸
        self.resize(300,300)
        #获得状态栏
        status=self.statusBar()
        #显示状态栏信息
        status.showMessage('只显示五秒的消息',5000)
        self.center()


    def center(self):
        #获取屏幕尺寸
        screen=QDesktopWidget().screenGeometry()
        #获取窗口尺寸
        size=self.geometry()
        #计算窗口到屏幕左侧的距离，计算窗口到屏幕顶端的距离
        newLeft=(screen.width()-size.width())/2
        newTop=(screen.height()-size.height())/2
        self.move(newLeft,newTop)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = CentreForm()
    main.show()
    sys.exit(app.exec_())
