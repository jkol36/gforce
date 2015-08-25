from django.core.management.base import BaseCommand, CommandError
from socketio.namespace import BaseNamespace

class Command(BaseCommand):
	help = "Starts to listen for data from kinises"

	def handle(self, *args, **kwargs):
		print "starting"
		with SocketIO('localhost', 8000, LoggingNamespace) as socketIO:
			socketIO.emit("wohhoo")
			socketIO.wait(seconds=1)

	