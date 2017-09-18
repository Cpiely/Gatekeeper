from app import app
from flask import Flask, request, redirect
from twilio.twiml.voice_response import VoiceResponse, Gathe, Sms
from twilio.rest import Client
import os

@app.route('/', methods=['GET', 'POST'])
def hello():
	resp = VoiceResponse()
	g = Gather(numDigits=4, action="/handle-key", method="POST")
	g.say("Enter your pin code.", voice='alice', language='es-US')
	resp.append(g)
	return str(resp)

@app.route('/handle-voice', methods=['GET', 'POST'])
def handle_voice():

	return str(resp)


@app.route('/handle-key', methods=['GET', 'POST'])
def handle_key():
	admin_name = os.environ.get("ADMIN_NAME") 
	admin_number = os.environ.get("ADMIN_NUMBER")
	"""Handles keys presses by the caller"""
	resp = VoiceResponse()
	# Get the digits pressed by the user
	digits_pressed = request.values.get('Digits', None)
	# Admin number
	if digits_pressed == '2158':
		resp.say('Hello %s, have a wonderful day!'%(ADMIN_NAME), voice='woman')
	elif digits_pressed == '8008':
		resp.sms('Your gate has been opened', to=admin_number)
		resp.say('%s will be expecting you shortly.'%(ADMIN_NAME), voice='woman')
	else:
		resp.say('Unauthorized visitor.', voice='woman')

	return str(resp)
