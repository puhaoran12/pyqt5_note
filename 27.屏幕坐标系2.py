import sys
from PyQt5.QtWidgets import QHBoxLayout, QMainWindow, QApplication, QPushButton, QWidget

def onClick_button():
    print('1')
    print("widget.x()=%d"%widget.x())
    print("widget.y()=%d" % widget.y())
    print("widget.width()=%d" % widget.wigth())
    print("widget.height()=%d" % widget.heihgt())
    print('2')
    print("widget.geometry.x()=%d" % widget.geometry.x())
    print("widget.geometry.y()=%d" % widget.geometry.y())
    print("widget.geometry.width()=%d" % widget.geometry.wigth())
    print("widget.geometry.height()=%d" % widget.geometry.heihgt())


app=QApplication(sys.argv)
widget=QWidget()
btn=QPushButton(widget)
btn.setText("按钮")
btn.clicked.connect(onClick_button)
btn.move(100,52)
widget.resize(600,240)
widget.move(500,200)
widget.setWindowTitle('屏幕坐标系')
widget.show()
sys.exit(app.exec_())