使用pyinstaller打包PyQt5应用

pip3 install pyinstaller(安装所对应的包)
方法一：
1.输入pyinstaller
2.将盘转换到python文件存放的盘：输入d:
3.复制python文件路径(copy-copy path)
4.cd 路径
5.pyinstaller python文件名.py

方法二：
1.输入pyinstaller
2.将盘转换到python文件存放的盘：输入d:
3.复制python文件路径(copy-copy path)
4.cd 路径
5.python 文件名.py
6.pyinstaller -Fw 文件名.py
-w:不显示终端
-F:将所有的库打包成一个文件