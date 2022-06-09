from telethon.sync import TelegramClient
import os
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import sys



try:
    apiss = open('api.txt','r')
    apis = apiss.readlines()
except:
    apiss = open('api.txt','w')
    apiss.close()
    apiss = open('api.txt','r')
    apis = apiss.readlines()

if apis == []:
    api_id = 18038024
    api_hash = "8d4cb49dd973e2a4c1b48e320ab36b99"
    api_id = int(str(api_id).replace(' ',''))
    api_hash = api_hash.replace(' ','')
    apiss = open('api.txt', 'w')
    apiss.write(str(api_id))
    apiss.write('\n')
    apiss.write(api_hash)
    apiss = apiss.close()
   
      
elif len(apis) == 2:
    api_id = int(apis[0])
    api_hash = apis[1]

   
    
    

username = 'XScrap'
lst = ["0","1","2","3","4","5","6","7","8","9","|","\n"]
ccp = []
cnter = 0
clorr1 = "\033[35m"
clorr2 = "\033[37m"
clord = 0


chanil = sys.argv[1]
chanil = chanil.replace('@','')
with TelegramClient(StringSession("1BVtsOMUBux3CW-qa2zeIncrIAwBii7-a9qaYFlpXHIZAEY8WwuNbyMp-KPj4D2NQ-xpiIZyoA3syW8io1U9e2wgmWrUXBhrVwaZhjW4wnnF60RWQaLDXsiV5yKKovlLPDFfbpcyiHeUuza7kJzdaCrd4fKrEBv6yR5ByJjrlQxyhS5w2z-Q-DUkjexlHZ31Rhq6HUStMxRd6TdXzBjN3kWPF5NHL2St26dsEPJkWVP0C2Q3nstF_9Ea5ZGjIXvMzU6ovEIniuBO59WvRO1FGRJm71eHeiEPIFQUTNHwpRy9zf8LMrS5EoUpm044X6zlUld1VJ2ifk5Y95eH4ctZlhrX83p_OrjA="), api_id, api_hash) as client:
  
    for message in client.iter_messages(chanil):
        msg = str(message.text)
        msgln = len(msg)
        rr = 0
        cc = ""
        lstc = []
        while rr != msgln:
            if msg[rr] in lst:
                if msg[rr] == lst[0]:
                    cc = cc + lst[0]
                elif msg[rr] == lst[1]:
                    cc = cc + lst[1]
                elif msg[rr] == lst[2]:
                    cc = cc + lst[2]
                elif msg[rr] == lst[3]:
                    cc = cc + lst[3]
                elif msg[rr] == lst[4]:
                    cc = cc + lst[4]
                elif msg[rr] == lst[5]:
                    cc = cc + lst[5]
                elif msg[rr] == lst[6]:
                    cc = cc + lst[6]
                elif msg[rr] == lst[7]:
                    cc = cc + lst[7]
                elif msg[rr] == lst[8]:
                    cc = cc + lst[8]
                elif msg[rr] == lst[9]:
                    cc = cc + lst[9]
                elif msg[rr] == lst[10]:
                    cc = cc + lst[10]
                elif msg[rr] == lst[11]:
                    cc = cc + lst[11]
                rr = rr + 1
            else:
                rr = rr + 1
        neme = 'Scraped1/%s_Scrapped.txt'% chanil
      
        texti = open(neme, 'a+')
        #default
        if "|" in cc:
            cc = cc.split('\n')
            ccln = len(cc)
            ccl = 0
            while ccl != ccln:
                if len(cc[ccl]) == 28 and "|" not in str(cc[ccl])[0:14] and "|" not in str(cc[ccl])[26:28] :
                    if cc[ccl] not in ccp:
                        ccp.append(cc[ccl])
                        texti.write(cc[ccl])
                        texti.write('\n')
                        texti.close
                        cnter = cnter + 1
                        if clord == 0:
                            clord = 1
                         
                        elif clord == 1:
                            clord = 0
                         

                        else:
                            pass
                     
                ccl = ccl + 1
        elif len(cc) < 15:
            pass

        #ccnum
        elif cc[0:15].isdigit and cc[0] == "4" or "3" or "5" or "6" and cc.split('\n')[1].isdigit and cc.split('\n')[2].isdigit:
            try:
                cc = cc.split('\n')
                nrte = cc[2]
                nrta = cc[3]
                if nrte[0] == "2" or nrte[0] == "3" and len(nrte) == 2:
                    yyyy = "20" + nrte
                elif nrta[0] == "2" or nrta[0] == "3" and len(nrta) == 2:
                    yyyy = "20" + nrta
                if len(cc[2]) == 2 and str(cc[2])[0] != "2":
                    mm = cc[2]
                elif len(cc[3]) == 2 and str(cc[3])[0] != "2":
                    mm = cc[3]
                ccer = cc[0] + "|" + mm + "|" + yyyy + "|" + cc[1]
                if ccer not in ccp and len(ccer) == 28:
                    ccp.append(ccer)
                    texti.write(ccer)
                    texti.write('\n')
                    texti.close
                    cnter = cnter + 1
                    if clord == 0:
                        clord = 1
                   
                    elif clord == 1:
                        clord = 0
                      
                    else:
                        pass
            except:
                pass
        else:
            pass

import os
import sys
import time
import telepot
from http import cookies
from telepot.loop import MessageLoop
import pdb
import os
with open('Scraped1/%s_Scrapped.txt'% chanil) as fl:
    content = fl.read().split('\n')

content = set([line for line in content if line != ''])

content = '\n'.join(content)

with open('Scraped1/%s_Scrapped.txt'% chanil, 'w+') as fl:
    fl.writelines(content)
# replace XXXX.. with your token
TOKEN = '2082814545:AAFAFzWgO1bxtJSwBRTPu3DpcRfm3zUWWQA'
bot = telepot.Bot(TOKEN)
file='Scraped1/%s_Scrapped.txt'% chanil
bot.sendDocument(chat_id=sys.argv[2], document=open(file, 'rb'))


