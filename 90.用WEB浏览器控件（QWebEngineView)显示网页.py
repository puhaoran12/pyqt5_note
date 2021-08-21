'''
用Web浏览器控件（QWebEngineView）显示网页

PyQt5和Web的交互技术
同时使用Python和Web开发程序，混合开发

QWebEngineView:用来显示Web页面（交互之前能显示Web页面）
'''
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
class WebEngineView(QMainWindow):
    def __init__(self):
        super(WebEngineView,self).__init__()
        self.setWindowTitle('打开外部网页例子')
        self.setGeometry(5,30,1355,730)

        self.browser=QWebEngineView()#显示Web页面（浏览器控件）
        self.browser.load(QUrl('https://baidu.com/'))
        self.setCentralWidget(self.browser)#设置成中心控件

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = WebEngineView()
    main.show()
    sys.exit(app.exec_())