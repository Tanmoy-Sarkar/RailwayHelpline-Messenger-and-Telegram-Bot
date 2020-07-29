from bot import telegram_chatbot
from response import message_response,train_name,schedule,price


bot = telegram_chatbot("config.cfg")

#making reply based on intention of the given message

def make_reply(msg,name,sticker,sticker_name):

	global update_id
	
	

	if msg is not None:
		intent,value = message_response(msg)
		
		response = None

		if intent == "buying":
			response = "you can buy tickets from here \n"
			response += "https://www.esheba.cnsbd.com/#/"

		elif intent == "schedule" and value != "schedule":

			if value == "Silk City":
				response = schedule(value)
			if value == "Dhumketu Express":
				response = schedule(value)
			if value == "Padma":
				response = schedule(value)
			else:
				response = "Sorry Can't Understand You. Did you reallly meant " + value + "?"

			return response

		elif intent == "schedule" and value == "schedule":
			reply = "Which train you need schedule of Padma/Silk City/Dhumketu"
			bot.send_message(reply,from_)
			updates = bot.get_updates(offset=update_id)
			updates = updates['result']
			for item in updates:
				update_id = item['update_id']
				message = str(item['message']['text'])
						
			train= train_name(message)

			if train == "Silk City":
				response = schedule(train)

			if train == "Dhumketu Express":
				response = schedule(train)

			if train == "Padma":
				response = schedule(train)

			return response
			
		elif intent == "location_finding" and value != "location":

			if value == "Silk City":
				response = "Silk City is currently in Ullapara Station.It is late by 20 minutes off schedule.(This is completely random and static info for showing purpose.I really hope Bangladesh Railway provides location API for all their trains then it will be so much easier for us developers."
			if value == "Dhumketu Express":
				response = "Dhumketu Express is currently in Sirajgong Station.It is on time to schedule.(This is completely random and static info for showing purpose.I really hope Bangladesh Railway provides location API for all their trains then it will be so much easier for us developers."
			if value == "Padma":
				response = "Padma is currently in Tongi Station.It is late by 10 minutes.(This is completely random and static info for showing purpose.I really hope Bangladesh Railway provides location API for all their trains then it will be so much easier for us developers."

		elif intent == "location_finding" and (value == "location" or value == None):
			reply = "Which train you need location of Padma/Silk City/Dhumketu"
			bot.send_message(reply,from_)
			updates = bot.get_updates(offset=update_id)
			updates = updates['result']
			for item in updates:
				update_id = item['update_id']
				message = str(item['message']['text'])
						
			train= train_name(message)
			if train == "Silk City":
				response = "Silk City is currently in Ullapara Station.It is late by 20 minutes off schedule.(This is completely random and static info for showing purpose.I really hope Bangladesh Railway provides location API for all their trains then it will be so much easier for us developers."
			if train == "Dhumketu Express":
				response = "Dhumketu Express is currently in Sirajgong Station.It is on time to schedule.(This is completely random and static info for showing purpose.I really hope Bangladesh Railway provides location API for all their trains then it will be so much easier for us developers."
			if train == "Padma":
				response = "Padma is currently in Tongi Station.It is late by 10 minutes.(This is completely random and static info for showing purpose.I really hope Bangladesh Railway provides location API for all their trains then it will be so much easier for us developers."
			return response

		elif intent == "price":
			response = price()

		elif intent == None:
				response = "Sorry \U0001f614 I don't understand. \nYou can only ask me about \n\U0001f449Buying tickets \n\U0001f449Schedule of train(Padma,Silk City,Dhumketu) \n\U0001f449Location of train(Padma,Silk City,Dhumketu) \nThank You"
		
		elif intent == "Greetings":
			response = "Hi " + name + "\U0001f60A"+ " \n I am a rail bot \U0001f916 at your service\U0001f689\nYou can ask me about \n\U0001f449Buying tickets \n\U0001f449Schedule of train(Padma,Silk City,Dhumketu) \n\U0001f449Location of train(Padma,Silk City,Dhumketu) \n\U0001f449Ticket Price \nThank You"
	elif sticker == True:
		response = "That was a nice " + sticker_name + " sticker." + "Or not? \U0001f602 I don't know I can't read stickers \U0001f643."
	else:
		response = "Sorry \U0001f614 I don't understand. \nYou can only ask me about \n\U0001f449Buying tickets \n\U0001f449Schedule of train(Padma,Silk City,Dhumketu) \n\U0001f449Location of train(Padma,Silk City,Dhumketu) \n\U0001f449Ticket Price \nThank You"


	return response

update_id = None
sticker = False
sticker_name = None
while True:
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]


        	

    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = str(item["message"]["text"])

            except:
                message = None
            
            try:
            	if str(item["message"]["sticker"]):
            		sticker_name = str(item["message"]["sticker"]["set_name"])
            		sticker = True
            except:
            	sticker = False

       

            from_ = item["message"]["from"]["id"]
            name = item["message"]["from"]["first_name"]
            print(message)
            reply = make_reply(message,name,sticker,sticker_name)
            bot.send_message(reply, from_)




