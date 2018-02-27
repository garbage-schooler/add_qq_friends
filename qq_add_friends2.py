# -*- coding: utf-8 -*-

import pyautogui
import pyperclip

from qqlist import qq_list

p1 = pyautogui.locateCenterOnScreen('rect1.png')    # “QQ号码”输入框坐标
p2 = pyautogui.locateCenterOnScreen('rect2.png')    # “查找” 按钮坐标
p3 = pyautogui.locateCenterOnScreen('rect3.png')    # “+好友” 按钮坐标
p4 = pyautogui.locateCenterOnScreen('rect4.png')    # “下一步” 按钮坐标

pause = 2.0                                         # 根据系统反应时间调整

if None in (p1, p2, p3, p4):
    print('无法定位控件坐标，请手工截屏生成 rect*.png ')
    print([p1, p2, p3, p4])
    raise SystemExit(0)

p5 = (p4[0]+50, p4[1])

def paste(utext):
    pyperclip.copy(utext)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'v')

for qq in qq_list:
    pyautogui.PAUSE = 0.2
    pyautogui.click(*p5)                # 点击 “完成/关闭” 按钮
    pyautogui.click(*p1)                # 点击 “QQ号码” 输入框
    paste(qq)                           # 粘贴 QQ 号码

    pyautogui.PAUSE = pause
    pyautogui.click(*p2)                # 点击 “查找” 按钮
    pyautogui.click(*p3)                # 点击 “+好友” 按钮
    pyautogui.click(*p4)                # 点击 “下一步” 按钮
    pyautogui.click(*p4)                # 点击 “下一步” 按钮

pyautogui.PAUSE = 0.2
pyautogui.click(*p5)                    # 点击 “完成/关闭” 按钮

print('OK')
