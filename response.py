from wit import Wit

access_token = "OQJZGVBYC3YC2753FZXQAEIKQWIFBE7S"

client = Wit(access_token=access_token)


def message_response(message_text):
	intent=None
	entity = None
	value = None
	response = client.message(message_text)

	try:
		intent=response['entities']['intent'][0]['value']
		entity = list(response['entities'])[1]
		value= response["entities"][entity][0]['value']
	except:
		pass
	print(intent,entity,value)
	return (intent,entity,value)
