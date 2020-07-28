import requests
import json 
import configparser as cfg
class telegram_chatbot():
	def __init__(self,config):
		self.token = self.read_token_from_config_file(config)
		self.base = "https://api.telegram.org/bot{}/".format(self.token)


	#get updates about incoming messagesd
	def get_updates(self,offset=None): 
		url = self.base + "getUpdates?timeout=100"
		if offset:
			url = url + "&offset={}".format(offset +1)
		print(url)

		r = requests.get(url)
		return json.loads(r.content)

	#send message
	def send_message(self,msg,chat_id):
		url = self.base + "sendMessage?chat_id={}&text={}".format(chat_id,msg)
		if msg is not None:
			requests.get(url)
		
	#read token from congig file
	def read_token_from_config_file(self,config):
		parser = cfg.ConfigParser()
		parser.read(config)
		return parser.get('creds','token')
