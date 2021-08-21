'''
自定义信号
pyqtSignal()信号对象
'''
from PyQt5.QtCore import *
class MyTypeSignal(QObject):#定义类
    #定义一个信号
    sendmsg=pyqtSignal(object)#object表示参数类型，也表示python中所有类，可用str，int等代替

    def run(self):#定义方法
        self.sendmsg.emit('hello PyQt5')#触发信号

class MySlot(QObject):
    def get(self,msg):#接收信息：hello PyQt5
        print('信息：'+msg)

if __name__ == '__main__':
    send=MyTypeSignal()#创建信号和槽的对象
    slot=MySlot()

    send.sendmsg.connect(slot.get)
    send.run()

    send.sendmsg.disconnect(slot.get)
    send.run()
