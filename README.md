The heartbeat project is something I'm working on at work in 
order to test our Analytics System end to end.

Pulse.py will take in the number of messages we want to
generate and send to our url event logging point. 

It will convert my dictionary into a Json string then 
do a post request to our URL. 

I will then check the Database to make sure that the logs 
generated will end up in the right database. 

In the future I will write something that will check 
my database for if heart_beat_message is set to true
(which means something was logged) then it will check the
number of rows and then do a database clean up. 



