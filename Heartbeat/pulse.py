#Sends n number of Json messages to a particular endpoint. 
import requests 
import json
import pdb
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("messages", help="Will generate x number of messages to send though our system", type = int)
args = parser.parse_args()
num_messages = args.messages


def log_data(num_messages):

	log_data = []
	for i in range(num_messages):
		log_payload = {}
		log_payload['count'] = i 
		log_payload['game'] = "AE"
		log_payload['env'] = "Dev" 
		log_payload['heart_beat_message'] = True
		log_data.append(log_payload)
	return log_data


def send_data(log_message):
	log_json = json.dumps(log_message)
	url = "https://github.com/"
	headers = {'content-Type':'application/json'}
	r = requests.post(url, data = log_json, headers = headers)

	status = r.status_code
	print status 
	return status

# Todo - Try catch exceptions - Look at how to do error exceptions 

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

# print r 
# r = requests.post(url, data=json.dumps(payload), headers=headers)

# if constructing the URL query string by hand you can pass it in as a dictionary with a key value pair
# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.get("https://github.com/timeline.json", stream = True)
# r = requests.get("http://bi-logging.sjc.kixeye.com/log")
 

