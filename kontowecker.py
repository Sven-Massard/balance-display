from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import re

def getKontostand():
	# Setup the Gmail API
	SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'
	store = file.Storage('/home/pi/lcd/kontostand_lcd/credentials.json')
	creds = store.get()
	if not creds or creds.invalid:
	    flow = client.flow_from_clientsecrets('/home/pi/lcd/kontostand_lcd/client_secret.json', SCOPES)
	    creds = tools.run_flow(flow, store)
	service = build('gmail', 'v1', http=creds.authorize(Http()))

	messages = service.users().messages().list(userId='me',q='from:noreply@kontowecker.de').execute()
	x = 0
	numberMessages = messages['resultSizeEstimate']
	kontostand = 'Error: No matching email found'
	while x<numberMessages:
		msg_id=messages['messages'][x]['id']
		msg=service.users().messages().get(userId='me',id=str(msg_id)).execute()['snippet']
		msg = msg.encode('ascii', 'ignore')
		x += 1
		if 'Kontostand' in msg:
			kontostand = re.search('Saldo: (.+?)EUR', msg).group(1)
			break
	return kontostand

