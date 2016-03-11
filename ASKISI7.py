#APARAITHTES VIVLIOTHIKES GIA TO PROGRAMMA
import urllib2,json


#ORISMOS SYNARTHSHS ME TIS SUNTETAGMENES KATHE XWRAS
def fetchHTML(x,y):
    URL = "http://api.openweathermap.org/data/2.5/weather?lat="+y+"&lon="+x+"&appid=390f40f8ee6f923bba8b8b6726443618&units=metric"
    req = urllib2.Request(URL)
    response=urllib2.urlopen (req)
    return response.read()


#EISAGWGH SYNTETAGMENWN APTO XRHSTH
lon=(raw_input ("DWSTE THN TETMHMENH X : "))
lat=(raw_input ("DWSTE THN TETAGMENH Y : "))



output=fetchHTML(lon,lat)
data=json.loads(output)
temp = float (str(data['main']['temp']))


#EKTYPWSH KAIROY
print ("")
print "XWRA:  "+str(data['sys']['country'])
print "POLH:  "+str(data['name'])
print "KAIROS:  "+str(data['weather'][0]['main'])
print "THERMOKRASIA:  "+str(data['main']['temp'])
print "YGRASIA:  "+str(data['main']['humidity'])
print "PIESH: "+str(data['main']['pressure']) 
print "TAXYTHTA ANEMOY:  "+str(data['wind']['speed'])
print "EPIPEDO THALASSAS:  "+str(data['main']['sea_level'])
print "EPIPEDO EDAFOUS:  "+str(data['main']['grnd_level'])
print "ANATOLH HLIOU:  "+str(data['sys']['sunrise'])
print "DYSH HLIOY:  "+str(data['sys']['sunset'])


#SYNTHIKH IF GIA VROXH KAI YGRASIA
if str(data['weather'][0]['main']) == "Rain" :
     print "I'm singing in the rain!"

if temp > 20:
    print "Nice..."

if temp < 5:
    print "brrrrr"
