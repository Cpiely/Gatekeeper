from app import app
from twilio.twiml.voice_response import VoiceResponse, Gather

@app.route('/', methods=['GET', 'POST'])
def hello():
	resp = VoiceResponse()
	g = Gather(numDigits=4, action="/handle-key", method="POST")
	g.say(voice='woman', "Please enter your assinged pin code.")
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
		resp.say(voice='woman', 'Hello Cameron, have a wonderful day!')
	elif digits_pressed == '8008':
		resp.say(voice='woman', 'Cameron will be expecting you shortly.')
	else:
		resp.say(voice='woman', 'Unauthorized visitor.')

	return str(resp)
