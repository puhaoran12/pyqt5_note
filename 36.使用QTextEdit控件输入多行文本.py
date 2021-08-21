from PyQt5.QtWidgets import *
import sys

class QTextEditDemo(QWidget):
    def __init__(self):
        super(QTextEditDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('控件演示')

        self.resize(300,320)
        self.textEdit=QTextEdit()
        self.buttonText=QPushButton('显示文本')
        self.buttonHTML=QPushButton('显示HTML')
        self.buttonToText = QPushButton('获取文本')
        self.buttonToHTML = QPushButton('获取HTML')


        layout=QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.buttonText)
        layout.addWidget(self.buttonToText)
        layout.addWidget(self.buttonHTML)
        layout.addWidget(self.buttonToHTML)


        self.setLayout(layout)

        self.buttonText.clicked.connect(self.onClick_ButtonText)
        self.buttonToText.clicked.connect(self.onClick_ButtonToText)
        self.buttonHTML.clicked.connect(self.onClick_ButtonHTML)
        self.buttonToHTML.clicked.connect(self.onClick_ButtonToHTML)

     #槽
    def onClick_ButtonText(self):
        self.textEdit.setPlainText('hello world,世界你好吗？')

    def onClick_ButtonToText(self):
        print(self.textEdit.toPlainText())

    def onClick_ButtonHTML(self):
        self.textEdit.setHtml('<font clor="blue" size="5">Hello World</font>')
    def onClick_ButtonToHTML(self):
        print(self.textEdit.toHTML())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QTextEditDemo()
    main.show()
    sys.exit(app.exec_())
