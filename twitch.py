import sys
import subprocess
import time
try:
    from tkinter import Tk
except:
    from Tkinter import Tk

def livestreamer():
    subprocess.Popen([r'C:\Program Files (x86)\Livestreamer\livestreamer.exe', URL, "best"])

sel = True
while sel:
    print ("""
    ...............................................
    Make your selection at any time (TOOL)
    ...............................................
    1 - Conzec
    2 - Bwana
    3 - Mia
    4 - Gemieee
    5 - djclichedarkness
    6 - Rhyaree
    0 - Get url from clipboard
    Q - Exit
    """)
    if (sys.version_info > (3, 0)):
        sel = input("#: ")
    else:
        sel = raw_input("#: ")
    if sel == "1":
        URL = "http://www.twitch.tv/conzec89"
        livestreamer()
        break
    elif sel == "2":
        URL = "http://www.twitch.tv/bawana"
        livestreamer()
        break
    elif sel == "3":
        URL = "http://www.twitch.tv/missmiarose"
        livestreamer()
        break
    elif sel == "4":
        URL = "http://www.twitch.tv/gemieee"
        livestreamer()
        break
    elif sel == "5":
        URL = "http://www.twitch.tv/djclichedarkness"
        livestreamer()
        break
    elif sel == "6":
        URL = "http://www.twitch.tv/rhyaree"
        livestreamer()
        break
    elif sel == "0":
        OURL = Tk().clipboard_get()
        if "twitch.tv/" in OURL:
            SURL = OURL.rsplit('/', 1)
            URL = "http://www.twitch.tv/" + SURL[1]
            livestreamer()
        else:
            print ("Invalid clipboard contents.")
        break
    elif sel.lower() == "q":
        exit()
    elif sel != "":
        print ("\nInvalid option please try again.")
time.sleep(1)
