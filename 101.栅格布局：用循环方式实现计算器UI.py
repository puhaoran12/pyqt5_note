import sys,math
from PyQt5.QtWidgets import *
class calc(QWidget):
    def __init__(self):
        super(calc,self).__init__()
        self.setWindowTitle('栅格布局')

        grid=QGridLayout()#创建栅格布局
        self.setLayout(grid)

        names=['cls','back','','close',
               '7','8','9','/',
               '4','5','6','*',
               '1','2','3','-',
               '0','.','=','+']#创建元组
        positions=[(i,j) for i in range(4) for j in range(5)]
        print(positions)
        i=0
        for position,name in zip(positions,names):
            if name=='':
                continue#跳过，忽略
            button=QPushButton(name)
            #print(position)
            #i+=1
           # print(i)#用来验证22，26两行是否为循环内的
            grid.addWidget(button,*position)#position是一个元组，而grid不接受元组。在元组前面加*则可以将元组拆成两个数

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = calc()
    main.show()
    sys.exit(app.exec_())