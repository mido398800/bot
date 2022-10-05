#IMPORT_LIBS
import telebot
import os
import time
import sys
import requests as r
from dotenv import load_dotenv
while True:
	try:
		
		####################################
		AUTH_TOKEN = '2082814545:AAGlfguS-XoYDHpy-aSDF8UPU_fH2NMcGWE' 
		ADMIN_ID     = '1136754989'
		CH_USER      = 'STR_GUYS'
		CH_USER2    = 'PPJKK'
		load_dotenv()
		token = os.getenv(AUTH_TOKEN)
		bot     = telebot.TeleBot(AUTH_TOKEN,parse_mode="MARKDOWN")

		def main():

			bot.polling()
			
		@bot.message_handler()

		def greet(message):
		######################################################
			print("NEW MESSAGE : " + message.text + " FROM : " + str(message.chat.id)) # LOOP_PRINT
		######################################################
			from_id    = message.chat.id
			message_id = message.id
			text       = message.text
			first_name = message.chat.first_name
			username   = message.chat.username
			type       = message.chat.type
			language   = message.from_user.language_code
			sc_user    = text.replace("/cc @",'')
			start      = "HELLO , I CAN SCRAPE CC FROM GROUPS AND CHANNELS \nJUST SEND THE COMMAND\nLIKE : /sc @USER\nAND IF I FOUND ANY CC I WILL SEND IT IN A COMBO FILE\nI CREATED BY @S0OON"
			scraping   = "يرجى الانتظار 400 ثانية ثم إذا وجدت CC فسأرسلها\n--------------------\nPLEASE WAIT 400 SECOND THEN IF I FOUND CC I WILL SEND IT \nMY COMMAND IS '/sc @TARGET'\nTHIS BOT CREATED BY @S0OON\n[TEAM STRANGERS](https://t.me/PPJKK)"
			SUBSCRIBE_FIRST = "PLEASE SUBSCRIBE TO OUR CHANNEL TO USE ME\n-----------------------------------------------\nCH » @STR\_GUYS AND @PPJKK"
			CH_SUB = r.get("https://api.telegram.org/bot" + AUTH_TOKEN + "/getChatMember?chat_id=@" + CH_USER + "&user_id=" + str(from_id)).json()
			CH_SUB2 = r.get("https://api.telegram.org/bot" + AUTH_TOKEN + "/getChatMember?chat_id=@" + CH_USER2 + "&user_id=" + str(from_id)).json()
			CH_CHECK = CH_SUB['result']["status"]
			CH_CHECK2 = CH_SUB2['result']["status"]
			print("STATUS : " + CH_CHECK + " STATUS2 : " + CH_CHECK2)

			
			if type == "private" and CH_CHECK != 'kicked' and CH_CHECK2 != 'left' :
				
			######################################################  
				if "/start" == str(text) :                       #WELCOME_MESSAGE
					bot.reply_to(message, start)     #WELCOME_MESSAGE
			######################################################


			######################################################



				if "/cc @" in str(text) and text != "/cc @" and len(sc_user) >= 5 and text.count(' ') == 1:
		
					
					is_channel = r.get("https://t.me/"+str(sc_user)).text
					key_check  = '<meta property="og:description" content="">'
					if key_check not in is_channel and text != "/cc" and "groups can hold up to 200,000 members." not in is_channel and "members" in is_channel or "subscribers" in is_channel:
						bot.reply_to(message, scraping)
						co_1   = 'timeout 400 python3 scrape1.py ' + str(sc_user) + " " + str(from_id) + " &"
						co_2   = 'timeout 420 python3 send.py ' + str(sc_user) + " " + str(from_id) + " &"
						co_3   = 'timeout 420 python3 cc.py ' + str(sc_user) + " " + str(from_id) + " &"
						os.system(co_1)
						os.system(co_2)
						os.system(co_3)
						
					
			else:
				#SUBSCRIBE_FIRST
				bot.reply_to(message,SUBSCRIBE_FIRST)
					######################################################

		if __name__ == '__main__':
			main()

		####################################

	except Exception as ex:
		print(ex)
		continue
