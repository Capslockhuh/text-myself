# text_myself.py - sends you a text message 

from twilio.rest import Client

# Preset values
accountSID = <your account SID>
authToken = <your auth token>
myNumber = < your phone number>
twilioNumber = <your twilio phone number>

def textmyself(message):
    twilioCLi = Client(accountSID, authToken)
    twilioCLi.messages.create(body=message, from_=twilioNumber, to=myNumber)