import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import os
class WebEngineView(QMainWindow):
    def __init__(self):
        super(WebEngineView,self).__init__()
        self.setWindowTitle('装载本地Web页面')
        self.setGeometry(5,30,1355,730)
        url=os.getcwd()+'/1.html'
        self.browser=QWebEngineView()#创建显示Web页面（浏览器控件）
        self.browser.load(QUrl.fromLocalFile(url))
        self.setCentralWidget(self.browser)#设置成中心控件

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = WebEngineView()
    main.show()
    sys.exit(app.exec_())