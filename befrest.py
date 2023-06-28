import requests

def send_message(email, matn):
	response = requests.post(
		"https://api.mailgun.net/v3/sandbox19f60e3287144aa2a88f19bc8991f7ba.mailgun.org/messages",
		auth=("api", "ca7f61dce9747cf8031064bbf82a323e-d51642fa-0b10cb81"),
		data={"from": "<mailgun@sandbox19f60e3287144aa2a88f19bc8991f7ba.mailgun.org>",
			"to": [email],
			"subject": "Yor result",
			"text": matn})
	print(response.text)
	return response
