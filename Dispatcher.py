from Actor import Actor;
class Dispatcher():
    def __init__(self):
        pass;
    
    def addClients(self, clients):
        clients = clients;
        
    def sendToClient(self, msg, name, source):
        client = clients[name];
        if(isinstance(client, Actor)):
            client.receiveMessage(msg, source);
