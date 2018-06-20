import pyautogui as pg, webbrowser as wb

subject = pg.confirm("Which subject do you need to work on?","Choose subject below",['English', 'Math', 'Spanish', 'Science', 'History', 'Chorus'])

if subject == "English":
    pg.confirm("Now opening English websites.")
    wb.open("www.thesaurus.com")
    wb.open("www.dictionary.com")

elif subject == "Math":
    topic = pg.confirm("What topic in Math?","Choose topic below", ['Algebra','Geometry','Variables','Graphing'])

    if topic == "Algebra":
        pg.confirm("Now opening Algebra websites.")

    elif topic == "Geometry":
        pg.confirm("Now opening Geometry websites.")
