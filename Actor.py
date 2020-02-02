class Actor():

    def __init__(self, fss, name, dispatcher):
        self.name = name;
        self.fss = fss;
        self.fss.start('Sova');
        self.dispatcher = dispatcher;
        
    def sendMessage(self, msg, target):
        dispatcher.send(msg, target, self.name);

    def printState(self):
        print(self.fss.CurrentState());

    def performAction(self, action):
        print(self.name + ':');
        self.fss.event(action)
        self.fss.runFunction(action)(0);

    def receiveMessage(self, msg, source):
        self.performAction(msg);
        
    
        
