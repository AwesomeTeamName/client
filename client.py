import socket

class StockzClient():
	"""A client for StockzServer"""

	def __init__(self, host = '0.0.0.0', port = 1337):
		"""Create a StockzClient to connect to the provided address."""

		if not isinstance(host, basestring):
			raise TypeError('host must be a string')

		if not isinstance(port, int):
			raise TypeError('port must be an int')

		self._address = (host, port)

	def execute(self, request, timeout = 1):
		"""Execute a request and get a response from the server."""

		if not isinstance(request, basestring):
			raise TypeError('request must be a string')

		if not isinstance(timeout, int):
			raise TypeError('timeout must be an int')

		# Create the socket and connect to it
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		try:
			sock.connect(self._address)
			sock.settimeout(timeout)

			# Send the request
			sock.sendall(request)

			# Receive a response
			response = sock.recv(2048)
		finally:
			sock.close()

		# Return None if there is no response
		if response is None or len(response) == 0:
			return None

		return response

	def build_request(self, action, sender, data = None):
		"""Build a request from an action, sender and data."""

		if not isinstance(action, basestring):
			raise TypeError('action must be a string')

		if not isinstance(sender, basestring):
			raise TypeError('sender must be a string')

		if not data is None and not isinstance(data, basestring):
			raise TypeError('data must be a string or None')

		request = [action, sender]

		if data is not None:
			request.append(data)

		return (' ').join(request)

	def send_request(self, action, sender, data = None, timeout = 5):
		"""Send a request with an action, sender and data."""

		request = self.build_request(action, sender, data)
		return self.execute(request, timeout)
