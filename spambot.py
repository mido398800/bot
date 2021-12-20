



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
    if "-1001558652150" == str(chat_id) or msg['from']['id']==1136754989 or str(chat_id) == "-1001513318163" or chat_id == 1767396893 or chat_id == 1153806633:
    
    
	    if content_type == 'text' and "/spam 012" in msg["text"]:
	    
	    	data = msg['text'].replace('/spam ','')
	    	data2 = data.split(' ')
	    	print(len(data2))
	    	if len(data2) == 2:
	    		#result = bot.invoke(DeleteMessagesRequest(msg['message_id']))
	    		bot.deleteMessage(telepot.message_identifier(msg))
	    		
	    		bot.sendMessage(chat_id, "Iam Starting Now ...\nNumber : "+data2[0].replace(data2[0][-4:],"xxxx")+"\nCount : "+data2[1])
	    		os.system('timeout 900 python3 spam012.py '+str(data2[0])+" "+str(data2[1])+' '+str(chat_id)+' &')
	    	else:
	    		bot.sendMessage(chat_id, "Error \nthe correct syntax like : /spam 012xxxxxxxx 12")
	    	
    else:
    	bot.sendMessage(chat_id, "Sorry The Bot Available in our group only @STR_GUYS\nTo Activate The Bot In Your Group => Dm @S0OON")
    	
    	


# replace XXXX.. with your token
TOKEN = '2105905758:AAFgUW13XjTzO2tTRBalBIj9MrrVYNnNlH0'
bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')
# Keep the program running.
while 1:
	time.sleep(10)

  
