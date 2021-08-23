#!/usr/bin/env python
# coding=utf-8

import pyautogui

print(pyautogui.size())
print(pyautogui.position())  # 鼠标当前坐标
pyautogui.moveTo(24, 882, duration=1)  # 移动到指定位置
pyautogui.click(24, 882, duration=1)  # 移动到开始菜单位置
pyautogui.click(24, 830, duration=1)  # 点击电源键
pyautogui.click(24, 750, duration=1)  # 移动到关机键
pyautogui.click(24, 750)  # 点击关机
