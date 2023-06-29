import requests

def send_message(email, matn):
	response = requests.post(
		"https://api.mailgun.net/v3/sandboxc9fedaa8cd1b408d93c89efb9895ff40.mailgun.org/messages",
		auth=("api", "d3564e02ed519bf4e5afe5ba8c564d26-30344472-11b68e52"),
		data={"from": "<mailgun@sandbox19f60e3287144aa2a88f19bc8991f7ba.mailgun.org>",
			"to": [email],
			"subject": "Your result",
			"text": matn})
	print(response.text)
	return response

