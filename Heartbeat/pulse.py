#Sends n number of Json messages to a particular endpoint. 
import requests 
import json
import pdb
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("messages", help = "Will generate x number of messages to send though our system", type = int)
parser.add_argument("env", help = "This will set the Enviroment Endpoint. Options include 'Dev', 'Stage', 'Prod', or Test", type = str, choices = ['Dev', 'Stage', 'Prod','Test'])
parser.add_argument("type", help = "This will set the type of heart beat to be run. Options include 'Load', 'End', 'Error'", type = str, choices = ['Load', 'End', 'Error'])


args = parser.parse_args()
num_messages = args.messages
env = args.env


def log_data(num_messages):

	log_data = []
	for i in range(num_messages):
		log_payload = {}
		log_payload['count'] = i 
		log_payload['env'] = env  
		log_payload['game'] = "AE"
		log_payload['platform'] = "ae"
		log_payload['session_id'] = "blah" # todo : add a number generator 
		log_payload['heart_beat_message'] = True
		# figure out how to make a dictionary inside a dictionary for events 
		event_data = {}
		event_data['utc'] = "some utc numbers"
		event_data['guid'] = 'some guid number' #another unique number generator
		log_payload['events'] = event_data
		log_data.append(log_payload)
	return log_data




def send_data(log_message):
	log_json = json.dumps(log_message)
	print log_json
	url = {}
	url['Dev'] = 'https://www.dev.com'
	url['Prod'] = 'https://www.prod.com'
	url['Stage'] = 'https://www.stage.com'
	url['Test'] = 'https://github.com/'
	headers = {'content-Type':'application/json'}
	r = requests.post(url[env], data = log_json, headers = headers)
	

	status = r.status_code
	print status 
	return status

# todo figure out what a switch statement, dictionary of functions, 

# Todo - Try catch exceptions - Look at how to do error exceptions 
# what is a doc string bpython and Ipython

def errors(status):
	# r.status_code == requests.codes.ok 
	if status == 200:
		print "It worked"
	elif status == 403:
		print "Authentication Failed"
	elif status == 413: 
		print "Request was too large"
	elif status == 400:
		print "Something is wrong in the JSON or the Required Parameters"	
	else: 
		print "Some other Error code?"



log_messages = log_data(num_messages)

for log_message in log_messages:
	status= send_data(log_message)
 	errors(status);		
