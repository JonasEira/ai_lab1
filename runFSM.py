from FSM import FSM;
from MyTransitions import MyTransitions;
from Actor import Actor;
import Dispatcher;

print("__name__ value: ", __name__)

actors = dict();
actions = ['tjäna', 'köpa', 'törstig', 'glad', 'trött'];
dispatcher = Dispatcher.Dispatcher();

def main():

    trans = MyTransitions();
    fsm = {};
    for n in range(0,4):
        fsm[n] = FSM( [ ("Sova","Äta", 'hungrig', lambda x: x == trans.sova('hungrig')),
                    ("Sova","Umgås",'glad', lambda x: x == trans.sova('glad')),
                    ("Sova","Jobba",'tjäna', lambda x: x == trans.sova('tjäna')),
                    ("Sova","Dricka",'törstig', lambda x: x == trans.sova('törstig')),

                    ("Äta","Sova",'trött', lambda x: x == trans.ata('trött')),
                    ("Äta","Jobba",'tjäna', lambda x: x == trans.ata('tjäna')),
                    ("Äta","Umgås", 'glad', lambda x: x == trans.ata('glad')),

                    ("Umgås","Äta",'hungrig',lambda x: x == trans.umgas('hungrig')),
                    ("Umgås","Dricka",'törstig',lambda x: x == trans.umgas('törstig')),
                    ("Umgås","Sova",'trött',lambda x: x == trans.umgas('trött')),

                    ("Jobba","Sova",'trött',lambda x: x == trans.jobba('trött')),
                    ("Jobba","Äta",'hungrig',lambda x: x == trans.jobba('hungrig')),
                    ("Jobba","Dricka",'törstig',lambda x: x == trans.jobba('törstig')),
                    ("Jobba","Jobba",'tjäna',lambda x: x == trans.jobba('tjäna')),
                    ("Jobba","Handla",'köpa',lambda x: x == trans.jobba('köpa')),

                    ("Handla","Äta",'hungrig',lambda x: x == trans.handla('hungrig')),
                    ("Handla","Umgås",'glad',lambda x: x == trans.handla('glad')),
                    ("Handla","Jobba",'tjäna',lambda x: x == trans.handla('tjäna')),
                       
                    ("Dricka","Sova",'trött',lambda x: x == trans.dricka('trött')),
                    ("Dricka","Jobba",'tjäna',lambda x: x == trans.dricka('tjäna')),
                    ("Dricka","Umgås",'glad',lambda x: x == trans.dricka('glad')),
                    ("Dricka","Handla",'köpa',lambda x: x == trans.dricka('köpa')),
                    ("Dricka","Äta",'hungrig',lambda x: x == trans.dricka('hungrig'))])

        name = 'actor' + str(n);
        actors[name] = Actor(fsm[n], name, dispatcher);
        
    dispatcher.addClients(actors);
    printCommands();
    cmd = input()
    while(not cmd == 'quit'):
        doCommand(cmd);
        cmd = input();

def doCommand(cmd):
    cmds = cmd.split()
    try:
        if(len(cmds) == 0 or len(cmds) > 2):
            print('Wrong number of commands');
            printCommands();
        if(len(cmds) == 2):
            actor = actors[cmds[0]];
            if(cmds[1] == 'state'):
                actor.printState();
            else:
                actor = actors[cmds[0]];
                actor.receiveMessage(cmds[1], 'me');
        if(len(cmds) == 1):
            if(cmds[0] == 'listactors'):
                printActors();
        
    except ValueError as e:
        print('Error ' + str(e));
    
def printCommands():
    print('Commands: actor<n> <action>, actor<n> state, listactors');
    print('Actions:');
    acts = "";
    for act in actions:
        acts += act + ' ';
    print(acts);

def printActors():
    actorList = actors.keys();
    acts = "";
    for act in actorList:
        acts += act + ' ';
    print('Actors:');
    print(acts);

def runActors():
    while(running):

def TestFSM():
    fs[1].start('Sova');
    newState = fs[1].CurrentState();
    wasLast = True;
    fs[1].event(event);
    fs[1].RunFunction(event)(0);
        
    

if __name__ == '__main__':
    main()
