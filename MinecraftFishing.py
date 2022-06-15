# /usr/bin/env python3
import threading
import sys
import keyboard
import time
import pyautogui
from pymouse import PyMouse


def SCREEN_CHECK():
    screenWidth, screenHeight = pyautogui.size() #获取屏幕分辨率
    center_X = screenWidth / 2 - 5               #截取鱼漂一定存在的图像的左上X座标
    center_Y = screenHeight / 2 + 370            #截取鱼漂一定存在的图像的左上Y座标,*可改为+250 增大检测范围
    im = pyautogui.screenshot(region=(center_X, center_Y, 3, 70)) #根据左上X，Y座标截取宽度为3，长度为70的图像,*修改Y座标后必须修改此处，可改为+140 增大检测范围
    im.save("123.png")

    for y in range(im.size[1]):
        for x in range(im.size[0]):
            pix = im.getpixel((x, y))
            if pix[0] == 209 or pix[0] == 0:
#                print(pix)
                return False   #存在鱼漂，返回False
#    im.save("1456.png")
    return True                #不存在鱼漂，鱼上钩，返回True


def MOUSE_CLICK():
    click = SCREEN_CHECK()
    m = PyMouse()
    x, y = m.position()
    if click:
        m.click(x, y, 2)
        time.sleep(0.2)
        m.click(x, y, 2)
        time.sleep(3)



def RUN():
    global EXIT
    if not EXIT:
        a = MOUSE_CLICK()

    else:
        while True:
            sys.exit()


def START():
    while True:
        a = RUN()



def STOP():
    global EXIT
    keyboard.wait('esc')
    EXIT = True
    return True


if __name__ == '__main__':
    EXIT = False

    t2 = threading.Thread(target=STOP)
    t1 = threading.Thread(target=START)
    keyboard.wait('ctrl')
    t2.start() 
    t1.start()
