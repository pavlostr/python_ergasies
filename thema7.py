#!/usr/bin/env python
# -*- coding: iso-8859-7 -*-

#ΑΠΑΡΑΙΤΗΤΕΣ ΒΙΒΛΙΟΘΗΚΕΣ ΓΙΑ ΤΟ ΠΡΟΓΡΑΜΜΑ
import urllib2,json


#ΟΡΙΣΜΟΣ ΣΥΝΑΡΤΗΣΗΣ ΜΕ ΤΙΣ ΣΥΝΤΕΤΑΓΜΕΝΕΣ ΚΑΘΕ ΧΩΡΑΣ 
def fetchHTML(x,y):
    URL = "http://api.openweathermap.org/data/2.5/weather?lat="+y+"&lon="+x+"&appid=390f40f8ee6f923bba8b8b6726443618&units=metric"
    req = urllib2.Request(URL)
    response=urllib2.urlopen (req)
    return response.read()


#ΕΙΣΑΓΩΓΗ ΣΥΝΤΕΤΑΓΜΕΝΩΝ ΑΠΤΟ ΧΡΗΣΤΗ
lon=(raw_input ("ΔΩΣΤΕ ΤΗΝ ΤΕΤΜΗΜΕΝΗ X : "))
lat=(raw_input ("ΔΩΣΤΕ ΤΗΝ ΤΕΤΑΓΜΕΝΗ Y : "))



output=fetchHTML(lon,lat)
data=json.loads(output)
temp = float (str(data['main']['temp']))


#ΕΚΤΥΠΩΣΗ ΚΑΙΡΟΥ
print ("")
print "ΧΩΡΑ:  "+str(data['sys']['country'])
print "ΠΟΛΗ:  "+str(data['name'])
print "ΚΑΙΡΟΣ:  "+str(data['weather'][0]['main'])
print "ΘΕΡΜΟΚΡΑΣΙΑ:  "+str(data['main']['temp'])
print "ΥΓΡΑΣΙΑ:  "+str(data['main']['humidity'])
print "ΠΙΕΣΗ: "+str(data['main']['pressure']) 
print "ΤΑΧΥΤΗΤΑ ΑΝΕΜΟΥ:  "+str(data['wind']['speed'])
print "ΕΠΙΠΕΔΟ ΘΑΛΑΣΣΑΣ:  "+str(data['main']['sea_level'])
print "ΕΠΙΠΕΔΟ ΕΔΑΦΟΥΣ:  "+str(data['main']['grnd_level'])
print "ΑΝΑΤΟΛΗ ΗΛΙΟΥ:  "+str(data['sys']['sunrise'])
print "ΔΥΣΗ HΛΙΟΥ:  "+str(data['sys']['sunset'])


#ΣΥΝΘΗΚΗ IF ΓΙΑ ΒΡΟΧΗ ΚΑΙ ΘΕΡΜΟΚΡΑΣΙΑ
if str(data['weather'][0]['main']) == "Rain" :
     print "I'm singing in the rain!"

if temp > 20:
    print "Nice..."

if temp < 5:
    print "brrrrr"




    
   
