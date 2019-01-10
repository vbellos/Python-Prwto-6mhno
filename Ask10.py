#!/usr/bin/python
import urllib2

n = raw_input("dwse syndesmo .html: \n")

response = urllib2.urlopen(n) 
html = response.read()
 
syndesmoi = html.count("href")
par= html.count("<p>") + html.count("<br>")

print("Arithmos syndesmwnn: ",syndesmoi)
print("Arithmos allagwn grammhs: ",par)
