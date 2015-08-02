from os import listdir
from os.path import isfile, join
from random import shuffle
import subprocess

animepath = "A:\\"
mpv = "C:\Users\Yuki\mpv\mpv.exe"

animefiles = [ f for f in listdir(animepath) if isfile(join(animepath,f)) ]
shuffle(animefiles)
a = 0
while a <= len(animefiles):
    subprocess.Popen([mpv, animepath + animefiles[a]]).wait()
    a = a + 1
