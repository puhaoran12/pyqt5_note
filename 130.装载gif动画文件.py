'''
通过QMovie装在gif
'''
import sys
from PyQt5.QtWidgets import QApplication,QLabel,QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie
class LoadingGif(QWidget):
    def __init__(self):
        super().__init__()
        self.lable=QLabel('',self)#将gif放在lable中，所以创建一个lable
        self.setFixedSize(250,175)
        self.setWindowFlags(Qt.Dialog | Qt.CustomizeWindowHint)#设置窗口样式
        self.movie=QMovie('./play.gif')#创建
        self.lable.setMovie(self.movie)
        self.movie.start()

if __name__ == '__main__':
        app = QApplication(sys.argv)
        main = LoadingGif()
        main.show()
        sys.exit(app.exec_())