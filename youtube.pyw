import subprocess
import re
try:
    from tkinter import Tk
except:
    from Tkinter import Tk

cb = Tk()
cb.withdraw()
url = cb.clipboard_get()

def mpv():
    subprocess.Popen(['C:\Users\Yuki\mpv\mpv.exe', "-volume=100", '{}'.format(url)])

def youtube_url_validation(url):
    youtube_regex = (
        r'(https?://)?(www\.)?'
        '(youtube|youtu|youtube-nocookie)\.(com|be)/'
        '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')

    youtube_regex_match = re.match(youtube_regex, url)
    if youtube_regex_match:
        return youtube_regex_match.group(6)

    return youtube_regex_match


if youtube_url_validation(url):
    mpv()
else:
    print "Not a valid youtube url."
    exit()
