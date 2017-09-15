from app import app
from twilio.twiml.voice_response import VoiceResponse

@app.route("/", methods=['GET', 'POST'])
def hello():
	resp = VoiceResponse()
	resp.say("You will die in seven days!",voice='woman')
	return str(resp)

