from browsermobproxy import Server, Client

server = Server(r"/Users/m.kodina/Documents/browsermob-proxy-2.1.4/bin/browsermob-proxy", options={'port': 9090})
server.start()
client = Client("localhost:8080")
client.new_har()
