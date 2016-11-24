import requests
import os
import shutil
import urllib2

letters = ["03", "04", "05", "06", "07", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24"]
path_u = "/home/anusha/Downloads/MIT Algorithmic Courseware/"

for letter in letters:
    #r = requests.get("http://www.archive.org/download/MIT6.006F11/MIT6_006F11_lec{}_300k.mp4".format(str(letter)))
    #if r.status_code == 200:
    #    with open(path, 'wb') as f:
    #        r.raw.decode_content = True
    #        shutil.copyfileobj(r.raw, f)
    page = urllib2.urlopen("http://www.archive.org/download/MIT6.006F11/MIT6_006F11_lec{}_300k.mp4".format(str(letter)))
    html = page.read()
    path = "{}Lecture Video_{}.mp4".format(path_u,letter) 
    name = os.path.abspath(path)
    with open(name, 'wb') as f:
    	f.write(html)

