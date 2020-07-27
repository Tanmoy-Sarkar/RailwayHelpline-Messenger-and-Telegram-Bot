from wit import Wit
access_token = "ERFWG3HTOK5TRYDHCJYJAKGZCIL2JKSH"
client = Wit(access_token=access_token)

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
	# 	entity = list(response['entities'])[1]
	# 	value= response["entities"][entity][0]['value']
	# except:
	# 	pass
	
	return (intent,value)

print(message_response("Where is padma"))

def train_name(message):
	train = None
	response = client.message(message)
	try:
		train= response['entities']['train'][0]['value']
	except:
		pass

	return train

print(train_name("dhumketu express"))
