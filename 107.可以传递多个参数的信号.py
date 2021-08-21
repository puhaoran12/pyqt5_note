from PyQt5.QtCore import *
class MyTypeSignal(QObject):#定义类
    #定义一个信号
    sendmsg=pyqtSignal(object)

    #发送三个参数的信号
    sendmsg1=pyqtSignal(str,int,int)#其中确定参数个数，类型

    def run(self):
        self.sendmsg.emit('hello PyQt5')

    def run1(self):
        self.sendmsg1.emit('hello',3,4)#str，int，int

class MySlot(QObject):#槽
    def get(self,msg):
        print('信息:'+msg)
    def get1(self,msg,a,b):#用msg，a，b分别接收参数str，int，int（即’hello'，3，4）
        print(msg)
        print(a+b)

if __name__ == '__main__':
    send=MyTypeSignal()
    slot=MySlot()

    send.sendmsg.connect(slot.get)
    send.sendmsg1.connect(slot.get1)

    send.run()#调用
    send.run1()

    send.sendmsg.disconnect(slot.get)
    send.run()



