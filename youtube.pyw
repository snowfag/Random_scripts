import subprocess
import re
try:
    from tkinter import Tk
except:
    from Tkinter import Tk

creds = ['username', 'password']
url = Tk().clipboard_get()

def mpv():
    subprocess.Popen(['C:\Users\Yuki\mpv\mpv.exe', "-volume=100", youtube_url_validation(url)])

def mpv_vessel():
    subprocess.Popen(['C:\Users\Yuki\mpv\mpv.exe', "-volume=100", '--ytdl-raw-options=username=%s,password=%s' % (creds[0],creds[1]), vessel_url_validation(url)])

def vessel_url_validation(url):
    vessel_regex = ( r'(https?://)?(www\.)?vessel\.com/videos/([^&=%\?]{9})' )
    vessel_regex_match = re.match(vessel_regex, url)
    if vessel_regex_match:
        return vessel_regex_match.group(0)
    return vessel_regex_match

def youtube_url_validation(url):
    youtube_regex = ( r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})' )
    youtube_regex_match = re.match(youtube_regex, url)
    if youtube_regex_match:
        return youtube_regex_match.group(0)
    return youtube_regex_match

if youtube_url_validation(url):
    mpv()
elif vessel_url_validation(url):
    mpv_vessel()
else:
    print ("Not a valid url.")
    exit()
