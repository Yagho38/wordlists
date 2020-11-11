import pyautogui, time
from threading import Thread

time.sleep(5)

f = open("spam.txt", "r")
sla = f.readlines()
def mandar1():
	while True:
		pyautogui.press('shift')
def mandar2():
	while True:
		pyautogui.press('enter')

t_mandar1 = Thread(target=mandar1)
t_mandar1.start()

t_mandar2 = Thread(target=mandar2)
t_mandar2.start()
