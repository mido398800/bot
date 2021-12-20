



import os
import sys
import time
import telepot
from http import cookies
from telepot.loop import MessageLoop
import pdb
def _extract_message(update):
    key = _find_first_key(update, [
                                   'message',
                                   'edited_message',
                                   'channel_post',
                                   'edited_channel_post',
                                   'callback_query',
                                   'inline_query',
                                   'chosen_inline_result',
                                   'shipping_query',
                                   'pre_checkout_query',
                                   'update_id'])
    return key, update[key]
def handle(msg):

    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text' and msg["text"] == "HZjd9H":
    	
    		bot.sendMessage(chat_id, "Done Activited ")
    		f2= open('paid.txt', 'a')
    		f2.write(str(chat_id))
    		f2.write("\n")
    paid = open('paid.txt',mode='r+')
    readpaid = paid.readlines()
    x = str(chat_id)
    for line in readpaid:
    	if x in line:
    		paid = 'paid'
    
    if paid == 'paid':
     
	    sp = open("users.txt", "r")
	    data = sp.read()
	    limit = data.count(str(chat_id))
	    
	    sp.close()
	    print(chat_id)
	    if limit < 50 or chat_id == 1136754989 or str(chat_id) == '-1001446252611' or str(chat_id) == '-1001558652150' or str(chat_id) == '-1001702455980' or str(chat_id) == '-1001171130697':
		    if content_type == 'text' and msg["text"] != "/start" and '/sc' in msg["text"]:
		        # let the human know that the pdf is on its way        
		        import requests as r
		        a=r.get("https://t.me/"+msg["text"].replace("/sc ",'').replace('@','')).text
		        b=r.get("https://sand65.ml/api/chaek.php?tu="+msg["text"].replace('/sc ',''))
		    
		 
		       
		    
		      
		        if '<meta property="og:description" content="">' not in a and msg["text"] != "/sc" and "members" in a or "subscribers" in a:
		        	bot.sendMessage(chat_id, "preparing txt of fresh CC, pls wait 400 Second..\nUsed Credit : "+str(limit))
		        	f = open('users.txt', 'a')
		        	f.write(str(chat_id))
		        	f.write("\n")
		        		
		        	import os
		        	os.system('timeout 400 python3 scrape1.py '+msg["text"].replace('/sc ','')+" "+str(chat_id)+" &")
		        	
		        	os.system('timeout 420 python3 send.py '+msg["text"].replace('/sc @','')+" "+str(chat_id)+" &")
		        	import time
		
		        	
		
		        else:
		        	bot.sendMessage(chat_id, "No Group/Channel/User With this username")
		        
		    elif content_type == 'text' and '-' not in str(chat_id):
		        bot.sendMessage(chat_id, "Hello!\nSend Group/Channel Username To Scrape CC Combolist For Free !\n\nBY • @STR_GUYS\nDwv • @S0OON")
	    else:
	    	bot.sendMessage(chat_id, "You Are Exceeded The Max Limit\n\nContact • @S0OON TO Activate New Key")
    else:
    	if content_type == 'text' and msg["text"] != "/start" and '-' not in str(chat_id):
    	
    		bot.sendMessage(chat_id, "You Are Not Activited User\n\nContact • @S0OON TO Activate Key")
    	elif content_type == 'text' and msg["text"] == "/start":
    	
    		if '-' not in chat_id:
    			bot.sendMessage(chat_id, "Welcome!\nJoin Us @STR_GUYS To Know The News\n\nBY • @S0OON ")


# replace XXXX.. with your token
TOKEN = '2082814545:AAFAFzWgO1bxtJSwBRTPu3DpcRfm3zUWWQA'
bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')
# Keep the program running.
while 1:
	time.sleep(10)

  

