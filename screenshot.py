import pyautogui
import os

dir = 'screenshots'

def randomShot():
    if not os.path.exists(dir):
        os.makedirs(dir)
    
    pyautogui.screenshot().save(dir + '/b.jpg')
    print('已保存')