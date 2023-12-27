import time
import keyboard
from pywinauto.application import Application
from pymouse import PyMouse  # 模拟鼠标

if __name__ == '__main__':
    m = PyMouse()

    # 点击学习按钮
    # x为水平位置 小左 大右
    # y为竖直位置 小上 大小

    t = 15
    while t != 0:
        t -= 1

        m.move(890, 250)
        m.click(890, 250, 1)
        time.sleep(0.5)

        m.move(320, 530)
        m.click(320, 530, 1)
        time.sleep(0.5)
