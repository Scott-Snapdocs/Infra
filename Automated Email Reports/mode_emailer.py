import mandrill
MANDRILL_API_KEY = 'ygblmkZ2RChJRPFG3KPKsA'  #<=fillin!
mandrill_client = mandrill.Mandrill(MANDRILL_API_KEY)
message = {
	'from_email': 'scott@snapdocs.com',
	'from_name': 'Scott via Mandrill via Python',
	'to': [{
		'email': 'scott@breuds.com',
		'name': 'Also Scott',
		'type': 'to'
		}],
	'subject': 'Testing out Mandrill',
	'text': 'This is a message from Mandrill'
	}

result = mandrill_client.messages.send(message=message)
print(result)