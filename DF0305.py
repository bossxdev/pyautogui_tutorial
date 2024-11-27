import pyautogui as pg
import pyautogui
import time

pg =  pg.position(746,134)

time.sleep(2)
pg = pyautogui.click(744, 134, button="left")

time.sleep(3)
pg = pyautogui.keyDown('shift')
pg = pyautogui.press('\\')
pg = pyautogui.keyUp('shift')
pg = pyautogui.write("0993000177967")

time.sleep(2)
pg = pyautogui.click(479, 456, button="left")

time.sleep(20)
pg = pyautogui.click(377, 559, button="left")
pg = pyautogui.write("3500")

time.sleep(3)
pg = pyautogui.click(679, 641, button="left")

time.sleep(5)
pg = pyautogui.click(729, 646, button="left")

time.sleep(5)
pg = pyautogui.click(671, 644, button="left")

time.sleep(5)
pg = pyautogui.click(560, 639, button="left")

time.sleep(5)
pg = pyautogui.click(486, 427, button="left")