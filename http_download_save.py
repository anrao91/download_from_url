import os
import urllib2

numbers = []

for number in range(0,10):
    numbers.append(number)
path_u = "/home/your_directory/"

for number in numbers:
    page = urllib2.urlopen("url_continuation_number{}".format(str(number)))
    html = page.read()
    path = "{}Lecture Video_{}.mp4".format(path_u,number) 
    name = os.path.abspath(path)
    with open(name, 'wb') as f:
    	f.write(html)

