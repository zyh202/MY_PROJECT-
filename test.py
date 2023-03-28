import easygui,os
cho=easygui.choicebox(title='选择版本',msg='选择一个版本',choices=['简单','普通','一般','困难'])
print('[debug]:choice'+cho)
if cho == '简单':os.system('py easy//pong_easy.py')
if cho == '一般':os.system('py hhh//pong_hhh.py')
if cho == '普通':os.system('py debauft//pong_debauft.py')
if cho == '困难':os.system('py o,no//pong_o,no.py')







