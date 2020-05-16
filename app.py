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
							

						if intent == "schedule":
							if value == "Silk City":
								response = "The Silkcity Express departs from Dhaka Komlapur station at 14:45 and arrives in Rajshahi Chapainababganj station at 08:35. In the return trip, Its leaves from Chapainababganj station at 07:40  and after 6-7 hours reaches Komlapur station at13:30. It works 6 days a week. Sunday is the weekly holiday of SIlkcity Express."
							if value == "Dhumketu Express":
								response = "The Dhumketu Express departs from Dhaka to Kamalapur railway station at 06:00 AM and arrives at Rajshahi at 11:40PM. This time it holds 769 number and Dhumketu Express doesn’t run Dhaka to Rajshahi route on Saturday. In the return trip, Dhumketu Express starts the journey from Rajshahi at 23:20 and ends the journey in Kamalapur station at 04:45. This time it holds the 770 number. Friday is the holiday of Rajshahi to Dhaka route."
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
	