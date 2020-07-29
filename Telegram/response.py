from wit import Wit
from tabulate import tabulate
access_token = "ERFWG3HTOK5TRYDHCJYJAKGZCIL2JKSH"
client = Wit(access_token=access_token)

#getting intention and value from the message given
def message_response(message_text1):
		
	intent = None
	entity = None
	value = None
	
	response = client.message(message_text1)
	print(response)

	try:
		intent=response['entities']['intent'][0]['value']
	except:
		pass
	try:
		entity = list(response['entities'])[1]	
	except:
		pass
	try:
		value= response["entities"][entity][0]['value']
	except:
		pass
	
	
	return (intent,value)



#getting particular train name
def train_name(message):
	train = None
	response = client.message(message)
	try:
		train= response['entities']['train'][0]['value']
	except:
		pass

	return train

def schedule(train):
	headers = ["From","Departure","To","Arrival","Off Day"]
	if train == "Padma":
		time = [["Rajshahi","16:00","Dhaka","21:40","Tuesday"],
				["Dhaka","23:00","Rajshahi","04:30","Tuesday"]]
	if train == "Silk City":
		time = [["Rajshahi","07:40","Dhaka","13:30","Sunday"],
				["Dhaka","14:45","Rajshahi","20:35","Sunday"]]
	if train == "Dhumketu Express":
		time = [["Rajshahi","23:20","Dhaka","04:45","Wednesday"],
				["Dhaka","06:00","Rajshahi","11:40","Thurday"]]

	return tabulate(time,headers=headers,tablefmt="pretty")

def price():
	headers = ["Shovon","Snigdha","AC Seat","AC Berth"]
	price_of_ticket = [["340","570","680","1020"]]
	return tabulate(price_of_ticket,headers=headers,tablefmt="pretty")





