import time
import random
import threading
from datetime import datetime
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, Key
import pyautogui

TOGGLE_KEY = Key.tab
EXIT_KEY = Key.home

clicking_event = threading.Event()
running = True
mouse = Controller()
xaxis, yaxis = 1295, 655
count = 0
last_run_date = None
pyautogui.FAILSAFE = False

def log_terminal(message):
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] {message}")

def quest42():
    rng = random.uniform(-0.5, 0.5)
    pyautogui.moveTo(890, 590, duration=1+rng) 
    time.sleep(5+rng)
    mouse.click(Button.left, 1)
    time.sleep(3+rng)
    pyautogui.moveTo(xaxis+ 10*rng, yaxis+ 10*rng, duration=1+rng)
    mouse.click(Button.left, 1)
    time.sleep(5+rng)
    pyautogui.moveTo(900, 600, duration=1+rng)
    mouse.click(Button.left, 1)
    time.sleep(3+rng)
    pyautogui.moveTo(xaxis+ 10*rng, yaxis+ 10*rng, duration=1+rng)
    mouse.click(Button.left, 1)
    time.sleep(5+rng)
    mouse.click(Button.left, 1)
    time.sleep(3+rng)
    mouse.click(Button.left, 1)
    time.sleep(5+rng)


def quest43():
    rng = random.uniform(-0.5, 0.5)
    pyautogui.moveTo(890, 590, duration=1+rng)  
    mouse.click(Button.left, 1)
    time.sleep(3+rng)
    pyautogui.moveTo(xaxis+ 10*rng, yaxis+ 10*rng, duration=1+rng)
    mouse.click(Button.left, 1)
    time.sleep(5+rng)
    pyautogui.moveTo(1100, 600, duration=1+rng)
    mouse.click(Button.left, 1)
    time.sleep(3+rng)
    pyautogui.moveTo(xaxis+ 10*rng, yaxis+ 10*rng, duration=1+rng)
    mouse.click(Button.left, 1)
    time.sleep(5+rng)
    mouse.click(Button.left, 1)
    time.sleep(3+rng)
    mouse.click(Button.left, 1)
    time.sleep(5+rng)


def quest54():
    rng = random.uniform(-0.5, 0.5)
    pyautogui.moveTo(960, 500, duration=1+rng)  
    mouse.click(Button.left, 1)
    time.sleep(5+rng)
    pyautogui.moveTo(xaxis+ 10*rng, yaxis+ 10*rng, duration=1+rng)
    mouse.click(Button.left, 1)
    time.sleep(5+rng)
    pyautogui.moveTo(1300, 600, duration=1+rng)
    mouse.click(Button.left, 1)
    time.sleep(5+rng)
    pyautogui.moveTo(xaxis+ 10*rng, yaxis+ 10*rng, duration=1+rng)
    mouse.click(Button.left, 1)
    time.sleep(5+rng)
    mouse.click(Button.left, 1)
    time.sleep(5+rng)
    mouse.click(Button.left, 1)
    time.sleep(5+rng)


def quest71():
    rng = random.uniform(-0.5, 0.5)
    pyautogui.moveTo(1100, 500, duration=1+rng)
    time.sleep(5+rng)   
    mouse.click(Button.left, 1)
    time.sleep(5+rng)
    pyautogui.moveTo(xaxis+ 10*rng, yaxis+ 10*rng, duration=1+rng)
    mouse.click(Button.left, 1)
    time.sleep(5+rng)
    mouse.click(Button.left, 1)
    time.sleep(5+rng)
    mouse.click(Button.left, 1)
    time.sleep(5+rng)


def quest83():
    rng = random.uniform(-0.5, 0.5)
    pyautogui.moveTo(1150, 580, duration=1+rng)  
    mouse.click(Button.left, 1)
    time.sleep(3+rng)
    pyautogui.moveTo(xaxis+ 10*rng, yaxis+ 10*rng, duration=1+rng)
    mouse.click(Button.left, 1)
    time.sleep(5+rng)
    pyautogui.moveTo(1100, 600, duration=1+rng)
    mouse.click(Button.left, 1)
    time.sleep(3+rng)
    pyautogui.moveTo(xaxis+ 10*rng, yaxis+ 10*rng, duration=1+rng)
    mouse.click(Button.left, 1)
    time.sleep(5+rng)
    mouse.click(Button.left, 1)
    time.sleep(3+rng)
    mouse.click(Button.left, 1)
    time.sleep(3+rng)
    pyautogui.moveTo(1050, 600, duration=1+rng)
    mouse.click(Button.left, 1)
    heal()


def heal():
    rng = random.uniform(-0.5, 0.5)
    time.sleep(300)
    pyautogui.moveTo(xaxis+ 10*rng, yaxis+ 10*rng, duration=1+rng)
    time.sleep(3)
    pyautogui.mouseDown(button='left')
    pyautogui.moveTo(xaxis-50+ 10*rng, yaxis+ 10*rng, duration=1+rng)
    pyautogui.mouseUp(button='left')
    pyautogui.moveTo(xaxis+ 10*rng, yaxis+ 10*rng, duration=1+rng)
    time.sleep(5+rng)
    for i in range(6):
        if i % 2 == 0:
            c = 0
        else:
            c = 100    
        pyautogui.moveTo(1000, 390+c, duration=1+rng)
        mouse.click(Button.left, 1)
        time.sleep(3+rng)
        pyautogui.moveTo(1240, 355, duration=1+rng)
        mouse.click(Button.left, 1)
        time.sleep(3+rng)
        pyautogui.moveTo(xaxis+ 10*rng, yaxis+ 10*rng, duration=1+rng)
        mouse.click(Button.left, 1)
        time.sleep(3+rng)
    pyautogui.moveTo(616, 310, duration=1+rng)
    mouse.click(Button.left, 1)
    time.sleep(3+rng)
    pyautogui.moveTo(xaxis+ 10*rng, yaxis+ 10*rng, duration=1+rng)


def refresh_four_am_function():
    log_terminal(">>> 4 AM TRIGGER: Starting special task...")
    
    rng = random.uniform(-0.5, 0.5)
    time.sleep(4000)
    pyautogui.moveTo(1448, 179, duration=1)
    mouse.click(Button.left, 1)
    time.sleep(40)
    pyautogui.moveTo(950, 590, duration=1)
    mouse.click(Button.left, 1)
    time.sleep(20)
    mouse.click(Button.left, 1)
    time.sleep(10)
    pyautogui.moveTo(1270, 670, duration=1)
    for _ in range(10):
        mouse.click(Button.left, 1)
        time.sleep(5)
    pyautogui.moveTo(xaxis+ 10*rng, yaxis+ 10*rng, duration=1+rng)
    time.sleep(5)
    pyautogui.mouseDown(button='left')
    pyautogui.moveTo(xaxis+ 10*rng, yaxis-50+ 10*rng, duration=1+rng)
    pyautogui.mouseUp(button='left')
    time.sleep(10+rng)
    quest54()

    log_terminal(">>> 4 AM TRIGGER: Task finished.")    


def normal_clicking_routine():
    rng = random.uniform(-0.5, 0.5) 
    count += 1
    pyautogui.moveTo(xaxis+ 10*rng, yaxis+ 10*rng, duration=1+rng)
    time.sleep(1)
    pyautogui.mouseDown(button='left')
    pyautogui.moveTo(xaxis+ 10*rng, yaxis-50+ 10*rng, duration=1+rng)
    pyautogui.mouseUp(button='left')
    pyautogui.moveTo(xaxis+ 10*rng, yaxis+ 10*rng, duration=1+rng)
    time.sleep(5+rng)
    mouse.click(Button.left, 1)
    time.sleep(3+rng)
    mouse.click(Button.left, 1)
    time.sleep(3+rng)

def osaka():
    pyautogui.moveTo(xaxis+ 10, yaxis+ 10, duration=1)
    mouse.click(Button.left, 1)

def clicker():
    global count, last_run_date
    log_terminal("System initialized. Waiting for input...")
    
    while running:
        now = datetime.now()
        current_date = now.date()
        if clicking_event.is_set():
            if now.hour == 3 and last_run_date != current_date:
                # Stop clicking while the special function runs
                was_clicking = clicking_event.is_set()
                if was_clicking:
                    clicking_event.clear()        
                refresh_four_am_function()
                last_run_date = current_date
                log_terminal(f"Daily task marked done for {current_date}")              
                if was_clicking:
                    clicking_event.set()
            else:
                osaka()
        else:
            time.sleep(0.5)


def on_press(key):
    global running 
    if key == TOGGLE_KEY:
        if clicking_event.is_set():
            clicking_event.clear()
            log_terminal("Status: PAUSED")
        else:
            clicking_event.set()
            log_terminal("Status: RUNNING")
    elif key == EXIT_KEY:
        log_terminal("Exiting program...")
        running = False
        return False


click_thread = threading.Thread(target=clicker, daemon=True)
click_thread.start()


print("-" * 30)
print(f"TOGGLE: {TOGGLE_KEY}")
print(f"EXIT:   {EXIT_KEY}")
print("-" * 30)


with Listener(on_press=on_press) as listener:
    listener.join()
