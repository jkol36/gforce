from django.conf import settings
from pusher import Pusher


def Setup():
	app_id = settings.PUSHER_APP_ID
	ssl = True
	port = 443
	key = settings.PUSHER_KEY
	secret = settings.PUSHER_SECRET
	return Pusher(app_id=app_id, 
		key=key, 
		secret=secret, 
		ssl=ssl,
		port=port)




