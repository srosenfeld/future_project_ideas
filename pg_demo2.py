import pyautogui as pg
import time

pg.hotkey('ctrl','winleft','d')
pg.hotkey('winleft')
pg.typewrite('chrome\n',0.5)
pg.hotkey('winleft','up')

pg.typewrite('netflix.com\n',0.5)
time.sleep(4)

pg.hotkey('tab')
time.sleep(.2)
pg.hotkey('tab')
time.sleep(.2)
pg.hotkey('enter')

time.sleep(4)

pg.hotkey('tab')
time.sleep(.2)

#How can we mimic the "pw" usage below to prompt the user to enter their email?
pg.typewrite('USERNAME GOES HERE\n',0.5)
pw = pg.password('Enter your password','Password box','','*')

pg.hotkey('tab')
time.sleep(.2)
pg.typewrite(pw,0.2)

pw=""

pg.hotkey('enter')
