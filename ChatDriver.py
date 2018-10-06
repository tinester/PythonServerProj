from ChatClient import ChatClient
from ChatServer import ChatServer

#for testing
print("we started instantiation")
#Create a Server
server = ChatServer()
#for testing
print("instantiated server")
# Create clients; must ask server to accept client connection before continuing
clientA = ChatClient("Client A")
#for testing
print("instantiated clientA")
server.acceptConnection()
#for testing
print("accepted A connection...")
clientB = ChatClient("Client B")
#for testing
print("instantiated clientB")
server.acceptConnection()
#for testing
print("accepted B connection...")

#for testing
print("instantiated everything")

clientSentStr = "just sending stuff"
#client A sends clientSentStr to server
clientA.send(clientSentStr.encode())
# Server receives string from Client A (index 0 because it connected first)
receivedStr = server.receive(0)
# Server sends string to client B (index 1 because it connected second)
server.send(receivedStr, 1)
# Client B receives the string
clientReceiveStr = clientB.receive().decode()
print(clientReceiveStr)