from wit import Wit




def message_response(message_text1):
	access_token = "ERFWG3HTOK5TRYDHCJYJAKGZCIL2JKSH"
	client = Wit(access_token=access_token)

	
	
	intent = None
	entity = None
	value = None
	response = client.message(message_text1)
	print(response)
	

	try:
		intent=response['entities']['intent'][0]['value']
		entity = list(response['entities'])[1]
		value= response["entities"][entity][0]['value']
	except:
		pass
	
	return (intent,value)

message_response("Give me schedule of padma train")