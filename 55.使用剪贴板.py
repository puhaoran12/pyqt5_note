import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
class ClipBoard(QDialog):
    def __init__(self):
        super(ClipBoard,self).__init__()
        textCopyButton=QPushButton('复制文本')
        textPasteButton=QPushButton('粘贴文本')

        htmlCopyButton = QPushButton('复制HTML')
        htmlPasteButton = QPushButton('粘贴HTML')

        imageCopyButton = QPushButton('复制图像')
        imagePasteButton = QPushButton('粘贴图像')

        self.textLabel=QLabel('默认文本')
        self.imageLabel=QLabel()
        self.imageLabel.setPixmap(QPixmap('book1.png'))

        layout=QGridLayout()
        layout.addWidget(textCopyButton,0,0)
        layout.addWidget(imageCopyButton,0,1)
        layout.addWidget(htmlCopyButton,0,2)
        layout.addWidget(textPasteButton,1,0)
        layout.addWidget(imagePasteButton,1,1)
        layout.addWidget(htmlPasteButton,1,2)

        layout.addWidget(self.textLabel,2,0,1,2)
        layout.addWidget(self.imageLabel,2,2)

        self.setLayout(layout)
        #关联
        textCopyButton.clicked.connect(self.copyText)
        textPasteButton.clicked.connect(self.pasteText)
        htmlCopyButton.clicked.connect(self.copyHtml)
        htmlPasteButton.clicked.connect(self.pasteHtml)
        imageCopyButton.clicked.connect(self.copyImage)
        imagePasteButton.clicked.connect(self.pasteImage)

        self.setWindowTitle('演示剪贴板')

    def copyText(self):
        clipboard=QApplication.clipboard()
        clipboard.setText('hello world')
    def pasteText(self):
        clipboard = QApplication.clipboard()
        self.textLabel.setText(clipboard.text())
    def copyImage(self):
        clipboard = QApplication.clipboard()
        clipboard.setPixmap(QPixmap('book1.png'))
    def pasteImage(self):
        clipboard = QApplication.clipboard()
        self.imageLabel.setPixmap(clipboard.pixmap())
    def copyHtml(self):
        mimData=QMimeData()
        mimData.setHtml('<b>Bold and <font color=red>Red</font></b>')
        clipboard = QApplication.clipboard()
        clipboard.setMimeData(mimData)

    def pasteHtml(self):
        clipboard = QApplication.clipboard()
        mimData=clipboard.mimeData()
        if mimData.hasHtml():
            self.textLabel.setText(mimData.html())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ClipBoard()
    main.show()
    sys.exit(app.exec_())