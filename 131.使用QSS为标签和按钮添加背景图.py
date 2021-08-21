from PyQt5.QtWidgets import *
import sys
class LabelButtonBackground(QWidget):
    def __init__(self):
        super().__init__()
        label1=QLabel(self)
        label1.setObjectName('name')
        label1.setToolTip('这是一个文本标签')#将鼠标放在标签上将会出现“这是一个文本标签”
        label1.setStyleSheet('#name{border-image:url(./lgz.jpg);}')

        label1.setFixedWidth(500)#设置标签尺寸
        label1.setFixedHeight(500)

        btn1=QPushButton(self)
        btn1.setObjectName('btn1')#设置按钮名字，选择器将会通过改名字定位到这个btn1
        btn1.setMaximumSize(100,100)
        btn1.setMinimumSize(100,100)

        style='''
          #btn1{
            border-radius:20px;
            background-image:url('./xiaotubiao.png');
          }
          #btn1:pressed{
             background-image:url('')
          }
        '''#（#btn1中#充当选择器）     pressed表示按下状态//即为按下和未按下两个状态
        #border-radius:20px;设置按键圆角
        btn1.setStyleSheet(style)

        layout=QVBoxLayout()
        layout.addWidget(label1)
        layout.addStretch()#添加拉伸
        layout.addWidget(btn1)

        self.setLayout(layout)
        self.setWindowTitle('使用QSS为标签和按钮添加背景图')

if __name__ == '__main__':
        app = QApplication(sys.argv)
        main = LabelButtonBackground()
        main.show()
        sys.exit(app.exec_())