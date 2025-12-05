import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode
import pyautogui

TOGGLE_KEY = KeyCode(char='*')  # 開始/暫停自動點擊器
EXIT_KEY = KeyCode(char='~')    # 退出程式

clicking_event = threading.Event()
running = True
mouse = Controller()
xaxis = 0 #設定點擊位置的X座標
yaxis = 0 #設定點擊位置的Y座標

def clicker():
    while running:
        if clicking_event.is_set():
            pyautogui.moveTo(xaxis, yaxis, duration=1)
            time.sleep(1)
            pyautogui.mouseDown(button='left')
            pyautogui.moveTo(xaxis, yaxis-50, duration=1)
            pyautogui.mouseUp(button='left')
            pyautogui.moveTo(xaxis, yaxis, duration=1)
            time.sleep(4)
            mouse.click(Button.left, 1)
            time.sleep(4)
            mouse.click(Button.left, 1)
            time.sleep(30)
        else:
            time.sleep(0.1)

def on_press(key):
    global running
    if key == TOGGLE_KEY:
        if clicking_event.is_set():
            clicking_event.clear()
            print("Auto-clicker paused")
        else:
            clicking_event.set()
            print("Auto-clicker started")
    elif key == EXIT_KEY:
        print("Exiting...")
        clicking_event.clear()
        running = False
        return False
    
click_thread = threading.Thread(target=clicker)
click_thread.daemon = True
click_thread.start()

with Listener(on_press=on_press) as listener:
    listener.join()
