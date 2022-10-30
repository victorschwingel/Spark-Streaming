import socket
import tweepy

host = 'localhost'
port = 9009

s = socket.socket()
s.bind((host, port))
print(f'Aguardando conexão na porta: {port}')

s.listen(5)
connection, address = s.accept()
print(f'Recebendo solicitação de: {address}')

token = 'AAAAAAAAAAAAAAAAAAAAAHGuigEAAAAAJkLOXrKCWiRreW7zZPEam80erWw%3D7iultrYbVPkzlZ3YuWiKkB7PTNhWqYqOqZcIPNCZpURSac1lTl'
keyword = 'domingo'

class GetTweets(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        print(tweet.text)
        print('='*50)
        connection.send(tweet.text.encode('utf-8', 'ignore'))

printer = GetTweets(token)
printer.add_rules(tweepy.StreamRule(keyword))
printer.filter()

connection.close()