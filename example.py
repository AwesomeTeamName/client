from client import StockzClient

request = ('hello', 'Jack')

client = StockzClient()

print(('Request: {0}').format((' ').join(map(str, request))))

response = client.send_request(*request)

print(('Response: {0}').format(response))