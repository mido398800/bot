#IMPORT_LIBS
import telebot
import os
import time
import sys
from dotenv import load_dotenv
while True:
	try:
		
		####################################
		AUTH_TOKEN = '2082814545:AAFAFzWgO1bxtJSwBRTPu3DpcRfm3zUWWQA' 
		ADMIN_ID   = '1136754989'
		load_dotenv()
		token = os.getenv(AUTH_TOKEN)
		bot = telebot.TeleBot(AUTH_TOKEN,parse_mode="MARKDOWN")

		def main():

			bot.polling()
			
		@bot.message_handler()

		def greet(message):
		######################################################
			print(message.text + "|" + str(message.chat.id)) # LOOP_PRINT
		######################################################
			from_id    = message.chat.id
			message_id = message.id
			text       = message.text
			first_name = message.chat.first_name
			username   = message.chat.username
			type       = message.chat.type
			language   = message.from_user.language_code
			start      = "NAME : " + first_name + "\nUSERNAME : " + username + "\nSTATUS : " + type + "\nLANGUAGE : " + str(language)
			scraping   = "PLEASE WAIT 400 SECOND THEN IF I FOUND CC I WILL SEND IT \nTHIS BOT CREATED BY @S0OON\n[TEAM STRANGERS](https://t.me/PPJKK)"
			
			if type == "private" :
				
			######################################################  
				if "/start" == str(text) :                       #WELCOME_MESSAGE
					bot.send_message(message.chat.id, start)     #WELCOME_MESSAGE
			######################################################


			######################################################



				if "/sc @" in str(text) and text != "/sc @":
					import requests as r
					sc_user    = text.replace("/sc @",'')
					is_channel = r.get("https://t.me/"+str(sc_user)).text
					key_check  = '<meta property="og:description" content="">'
					if key_check not in is_channel and text != "/sc" and "members" in is_channel or "subscribers" in is_channel:
						bot.send_message(message.chat.id, scraping)
						co_1   = 'timeout 400 python3 scrape1.py ' + str(sc_user) + " " + str(from_id) + " &"
						co_2   = 'timeout 420 python3 send.py ' + str(sc_user) + " " + str(from_id) + " &"
						os.system(co_1)
						os.system(co_2)
						
					
		######################################################

		if __name__ == '__main__':
			main()

		####################################

	except:
		continue
