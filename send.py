import os
import sys
import time
import telepot
from http import cookies
from telepot.loop import MessageLoop
import pdb
import os
time.sleep(410)

chanil = sys.argv[1]
chanil = chanil.replace('@','')
with open('Scraped1/%s_Scrapped.txt'% chanil) as fl:
    content = fl.read().split('\n')

content = set([line for line in content if line != ''])

content = '\n'.join(content)
with open('Scraped1/%s_Scrapped.txt'% chanil, 'w') as fl:
    fl.writelines(content)
# replace XXXX.. with your token
TOKEN = '2082814545:AAGlfguS-XoYDHpy-aSDF8UPU_fH2NMcGWE'
bot = telepot.Bot(TOKEN)
file='Scraped1/%s_Scrapped.txt'% chanil
bot.sendDocument(chat_id=sys.argv[2], document=open(file, 'rb'))
os.system('rm Scraped1/%s_Scrapped.txt'% chanil)
    


