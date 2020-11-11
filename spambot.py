import pyautogui, time

time.sleep(5)

f = open("spam.txt", "r")
sla = f.readlines()
while True:
	for word in sla:
		pyautogui.typewrite(word)
		pyautogui.press('enter')
