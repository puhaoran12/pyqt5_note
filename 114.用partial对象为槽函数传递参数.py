from PyQt5.QtWidgets import *
import sys
from functools import partial

class PartialSlotArg(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('使用Partial表达式为槽函数传递参数')

        button1=QPushButton('按钮1')
        button2=QPushButton('按钮2')

        button1.clicked.connect(partial(self.onButtonClick,10,20))
        button2.clicked.connect(partial(self.onButtonClick, 112, 20))

        layout = QHBoxLayout()
        layout.addWidget(button1)
        layout.addWidget(button2)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

    def onButtonClick(self, m, n):
        print('m+n=', m + n)
        QMessageBox.information(self, '结果：', str(m + n), )  # 弹出对话框，标题为  结果：  显示：str（m+n）

if __name__ == '__main__':
        app = QApplication(sys.argv)
        main = PartialSlotArg()
        main.show()
        sys.exit(app.exec_())