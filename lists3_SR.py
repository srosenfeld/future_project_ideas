import webbrowser
import pyautogui as pg

videos = ["https://youtube.com","https://vimeo.com","https://netflix.com"]

mail = ["https://gmail.com","https://mail.yahoo.com"]

choice = pg.prompt(
"""
Which links would you like to open? Type one of the following:

videos
mail
"""
    )

if choice == "videos":
    for i in videos:
        webbrowser.open(i)

elif choice == "mail":
    for i in mail:
        webbrowser.open(i)

else:
    pg.prompt("Please make sure your response is formatted correctly.")
