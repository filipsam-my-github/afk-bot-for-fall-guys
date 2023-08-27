
import keyboard,random
import win32api
import win32con
import time
import threading
import sys,pyautogui

click_info = {"afk in smal area":False,"auto afk":False,"afk in unlimited area":False}

movment_keys={"up":"w","down":"s","left":"d","right":"a"}

directions=["up","down","left","right"]

def message():
    print(f"""
      afk in unlimited area-j ({click_info["afk in unlimited area"]})
      auto afk"-k ({click_info["auto afk"]})
      afk in smal area-l ({click_info["afk in smal area"]})
      """)
message()


def on_press(key):
    try:
        if key.name == "j":
            click_info["afk in unlimited area"] = not click_info["afk in unlimited area"]
            message()
        elif key.name == "k":
            click_info["auto afk"] = not click_info["auto afk"]
            message()
        elif key.name == "l":
            click_info["afk in smal area"] = not click_info["afk in smal area"]
            message()
        elif key.name == "i":
            message()
            
    except:
        pass

good_q=0

def leaving_and_joining():
    time.sleep(0.5)
    pyautogui.keyDown("esc")
    time.sleep(1)
    pyautogui.keyUp("esc")
    time.sleep(0.5)
    pyautogui.keyDown("enter")
    time.sleep(1)
    pyautogui.keyUp("enter")
    time.sleep(6.5)
    pyautogui.keyDown("space")
    time.sleep(0.5)
    pyautogui.keyUp("space")
    time.sleep(3)
    pyautogui.keyDown("space")
    time.sleep(0.5)
    pyautogui.keyUp("space")
    time.sleep(3)
    pyautogui.keyDown("space")
    time.sleep(0.5)
    pyautogui.keyUp("space")
    time.sleep(3)
    pyautogui.keyDown("space")
    time.sleep(0.5)
    pyautogui.keyUp("space")

def clicking():
    global good_q
    while True:
        
        if click_info["afk in unlimited area"]:
            time.sleep(0.04)
            pyautogui.keyDown(movment_keys[random.choice(directions)])
            time.sleep(random.randint(15,35)/10)
            pyautogui.keyUp(movment_keys[random.choice(directions)])
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        elif click_info["auto afk"]:
            if pyautogui.locateOnScreen("fwrst.png",region = (0,0,50,50), grayscale = False, confidence = 0.7)!=None:
                leaving_and_joining()
            time.sleep(0.04)
            pyautogui.keyDown(movment_keys[directions[good_q%4]])
            time.sleep(0.5)
            pyautogui.keyUp(movment_keys[directions[good_q%4]])
            good_q+=1
        elif click_info["afk in smal area"]:
            time.sleep(0.04)
            pyautogui.keyDown(movment_keys[directions[good_q%4]])
            time.sleep(0.5)
            pyautogui.keyUp(movment_keys[directions[good_q%4]])
            good_q+=1
        else:
            time.sleep(0.01)

keyboard.on_press(on_press)

threading.Thread(target=clicking).start()

