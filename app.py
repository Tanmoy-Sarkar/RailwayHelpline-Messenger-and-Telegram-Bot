import os,sys
import schedule
from flask import Flask, request
from response import message_response 
from pymessenger import Bot

app = Flask("My echo bot")

FB_ACCESS_TOKEN = "EAAIyAxz4GsIBAPEhtpCau6adcNfjyJLyyaYTaTTnYjn7f2dGBbQWOZBGriO4F2rZCraBxmyRnweFElCJspRi53bFNZBQ2hMXXrQF8fP2ZCUQ6d2OZACpLsOMvp7hMS0ZAZC94bqCDeVBg2NlUBW12k91MbKr0uctutBZB3h7dxBfV5jK8CHJgXZBO"
bot = Bot(FB_ACCESS_TOKEN)

VERIFICATION_TOKEN = "hello"


@app.route('/', methods=['GET'])
def verify():
	if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
		if not request.args.get("hub.verify_token") == VERIFICATION_TOKEN:
			return "Verification token mismatch", 403
		return request.args["hub.challenge"], 200
	return "Hello world", 200


@app.route('/', methods=['POST'])
def webhook():
	print(request.data)
	data = request.get_json()
	log(data)

	if data['object'] == "page":
		entries = data['entry']

		for entry in entries:
			messaging = entry['messaging']

			for messaging_event in messaging:

				sender_id = messaging_event['sender']['id']
				recipient_id = messaging_event['recipient']['id']

				if messaging_event.get('message'):
					# HANDLE NORMAL MESSAGES HERE
					if messaging_event['message'].get('text'):
						# HANDLE TEXT MESSAGES
						query = messaging_event['message']['text']
						# ECHO THE RECEIVED MESSAGE
						
						intent,entity,value, = message_response(query)
						response = ""

						if intent == "buying":
							response = "you can buy tickets from here" +"/n"
							response += "https://www.esheba.cnsbd.com/#/"
							print(response)

						if intent == "schedule":
							if value == "Silk City":
								response = silk_city
							if value == "Dhumketu Express":
								response = dhumketu_express
							if value == "Padma":
								response = "The Padma Express departs from Dhaka Kamalapur station at 23:00 and after 5-6 hours its arrives in Rajshahi at 04:30. This time it holds the 759 number. In the return trip, Padma Express (760) starts the journey from Rajshahi station at 16:00 and ends the journey at 21:40. About 5-6 hours of time needed on this journey."

						if intent == "location_finding":
							if value == "Silk City":
								response = "Silk City is currently in Ullapara Station.It is late by 20 minutes off schedule"
							if value == "Dhumketu Express":
								response = "Dhumketu Express is currently in Sirajgong Station.It is on time to schedule"
							if value == "Padma":
								response = "Padma is currently in Tongi Station.It is late by 10 minutes"
						
						if intent == None:
							response = "Please I don't understand. You can only ask me about buying tickets/schedule/location of value.Thank You"
						
					bot.send_text_message(sender_id,response)
	return "ok", 200
def log(message):
	print(message)
	sys.stdout.flush()

	


if __name__ == "__main__":
	app.run(port=8000, use_reloader = True)
	print(silk_city)