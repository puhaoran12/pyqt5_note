'''
让程序定时关闭
QTimer.singleShot:在指定时间以后只调用一次代码
'''
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
if __name__=='__main__':
    app=QApplication(sys.argv)
    label=QLabel('<font color=red size=140><b>hello world,窗口在5秒后关闭！</b></font>')
    label.setWindowFlags(Qt.SplashScreen | Qt.FramelessWindowHint)
    label.show()
    QTimer.singleShot(5000,app.quit)


    sys.exit(app.exec_())