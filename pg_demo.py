import pyautogui as pg
import time

pg.hotkey('winleft','ctrl','d')
pg.hotkey('winleft')
pg.typewrite('chrome\n',0.2)
pg.hotkey('winleft','up')
pg.typewrite('espn.com\n',0.2)

time.sleep(3)

pg.hotkey('ctrl','t')
pg.typewrite('netflix.com\n',0.2)
time.sleep(3)
pg.hotkey('tab')
time.sleep(1)
pg.hotkey('tab')
time.sleep(1)
pg.hotkey('enter')
