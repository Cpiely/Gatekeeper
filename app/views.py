from app import app
from twilio.twiml.voice_response import VoiceResponse, Gather

@app.route('/', methods=['GET', 'POST'])
def hello():
	resp = VoiceResponse()
	g = Gather(numDigits=4, action="/handle-key", method="POST")
	g.say("Please enter your assinged pin code.", voice='woman')
	resp.append(g)
	return str(resp)

@app.route('/handle-key', methods=['GET', 'POST'])
def handle_key():
	"""Handles keys presses by the caller"""
	resp = VoiceResponse()
	# Get the digits pressed by the user
	digits_pressed = request.values.get('Digits', None)
	# Admin number
	if digits_pressed == '2158':
		resp.say('Hello Cameron, have a wonderful day!', voice='woman')
	elif digits_pressed == '8008':
		resp.say('Cameron will be expecting you shortly.', voice='woman')
	else:
		resp.say('Unauthorized visitor.', voice='woman')

	return str(resp)
