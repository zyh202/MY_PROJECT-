import easygui,os,sys
from asyncio.windows_utils import Popen
a=easygui.msgbox('''PONG
                            难度:普通
                            球大小:30x30
                            球拍大小:100x20''')
if a == 'OK':
    Popen('python pong_debauft.py',shell=True)
    sys.exit()