try:
    from tkinter import Tk
except:
    from Tkinter import Tk
t = Tk()
t.withdraw()
url = t.clipboard_get()
def cba():
    t.clipboard_clear()
    t.clipboard_append(cleanurl)

if "www.ebay.com" in url:
    cleanurl = "http://www.ebay.com/itm/" + url.rsplit('/',1)[1].split('?')[0]
    cba()
elif "www.amazon.co" in url:
    site = url.split('/',3)[2]
    cleanurl = "http://" + site + "/dp/" + url.rsplit('/',2)[1]
    cba()
elif "youtube.com/watch" in url:
    cleanurl = "https://youtu.be/" + url.split('?',1)[1].split('&',1)[0].split('=',1)[1]
    cba()
elif "https://youtu.be/" in url:
    cleanurl = "https://youtu.be/" + url.split('/')[3].split('?')[0]
    cba()
else:
    exit()
