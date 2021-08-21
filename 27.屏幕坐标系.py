import sys
from PyQt5.QtWidgets import QApplication, QMainWindow  # 创建应用所需的模块
from PyQt5.QtWidgets import QPushButton  # 按钮控件


class ScreenGeometry(QMainWindow):
    def __init__(self):
        super(ScreenGeometry, self).__init__()
        self.setWindowTitle("屏幕坐标系")  # 设置窗口标题
        self.resize(500, 300)  # 主窗口大小, 工作区大小

        self.btn = QPushButton(self)  # 创建一个按钮
        self.btn.setText("按钮")  # 设置按钮显示的名称
        self.btn.clicked.connect(self.onClickButton)  # 设置点击信号的槽函数

        self.move(300, 200)  # 设置窗口的位置

    def onClickButton(self):

        print("=" * 24)
        print("窗口横坐标 = %d" % self.x())
        print("窗口纵坐标 = %d" % self.y())
        print("工作区宽度 = %d" % self.width())
        print("工作区高度 = %d" % self.height())

        print("=" * 24)
        print("工作区横坐标 = %d" % self.geometry().x())
        print("工作区纵坐标 = %d" % self.geometry().y())
        print("工作区宽度 = %d" % self.geometry().width())
        print("工作区高度 = %d" % self.geometry().height())

        print("=" * 24)
        print("窗口横坐标 = %d" % self.frameGeometry().x())
        print("窗口纵坐标 = %d" % self.frameGeometry().y())
        print("窗口宽度 = %d" % self.frameGeometry().width())
        print("窗口高度 = %d" % self.frameGeometry().height())

        print("=" * 24)


if __name__ == "__main__":
    app = QApplication(sys.argv)  # 实例化应用
    main = ScreenGeometry()  # 创建窗口
    main.show()  # 显示窗口
    sys.exit(app.exec_())  # 进入主循环, sys.exit() 保证应用完全退出
