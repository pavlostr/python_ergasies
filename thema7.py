#!/usr/bin/env python
# -*- coding: iso-8859-7 -*-

#����������� ����������� ��� �� ���������
import urllib2,json


#������� ���������� �� ��� ������������� ���� ����� 
def fetchHTML(x,y):
    URL = "http://api.openweathermap.org/data/2.5/weather?lat="+y+"&lon="+x+"&appid=390f40f8ee6f923bba8b8b6726443618&units=metric"
    req = urllib2.Request(URL)
    response=urllib2.urlopen (req)
    return response.read()


#�������� ������������� ���� ������
lon=(raw_input ("����� ��� ��������� X : "))
lat=(raw_input ("����� ��� ��������� Y : "))



output=fetchHTML(lon,lat)
data=json.loads(output)
temp = float (str(data['main']['temp']))


#�������� ������
print ("")
print "����:  "+str(data['sys']['country'])
print "����:  "+str(data['name'])
print "������:  "+str(data['weather'][0]['main'])
print "�����������:  "+str(data['main']['temp'])
print "�������:  "+str(data['main']['humidity'])
print "�����: "+str(data['main']['pressure']) 
print "�������� ������:  "+str(data['wind']['speed'])
print "������� ��������:  "+str(data['main']['sea_level'])
print "������� �������:  "+str(data['main']['grnd_level'])
print "������� �����:  "+str(data['sys']['sunrise'])
print "���� H����:  "+str(data['sys']['sunset'])


#������� IF ��� ����� ��� �����������
if str(data['weather'][0]['main']) == "Rain" :
     print "I'm singing in the rain!"

if temp > 20:
    print "Nice..."

if temp < 5:
    print "brrrrr"




    
   
