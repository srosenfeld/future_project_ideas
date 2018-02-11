import webbrowser
import pyautogui as pg

sites = {
'https://yahoo.com':'mail',
'https://gmail.com':'mail',
'https://youtube.com':'video',
'https://vimeo.com':'video',
'https://netflix.com':'video'
    }

site_type = pg.prompt(
"""
What type of site would you like to open?
mail
video
"""
    )

for k,v in sites.items():
    if v == site_type:
        print(k)
        webbrowser.open(k)
