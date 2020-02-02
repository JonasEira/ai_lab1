class MyTransitions(object):
    def __init__(self):
        pass

    def ata(self, value):
        #print("value=" + value);
        result = False;
        if value=='tjäna':
            print("Mätt! Dags att jobba.");
            result = True;
        if value=='trött':
            print("Mätt! Dags att sova.");
            result = True;
        if value=='glad':
            print("Mätt! Dags att umgås.");
            result = True
        
        return value;

    def sova(self, value):
        #print("value=" + value);
        result = False;
        if value=='hungrig':
            print("Vaken! Dags att käka!");
            result = True;
        if value=='glad':
            print("Vaken! Dags att umgås!");
            result = True;
        if value=='tjäna':
            print("Vaken! Dags att jobba!");
            result = True;
        if value=='törstig':
            print("Vaken! Dags att Dricka!");
            result = True;
        return value;

    def umgas(self, value):
        #print("value=" + value);
        result = False;
        if value=='hungrig':
            print("Umgåtts, dags att käka!");
            result = True;
        if value=='törstig':
            print("Umgåtts, dags att dricka!");
            result = True;
        if value=='trött':
            print("Umgåtts, dags att sova!");
            result = True;
            
        return value;

    def jobba(self, value):
        #print("value=" + value);
        result = False;
        if value=='hungrig':
            print("Jobbat, dags att äta lunch!");
            result = True;
        if value=='törstig':
            print("Jobbat, dags att dricka vatten!");
            result = True;
        if value=='trött':
            print("Jobbat, dags att sova.");
            result = True;
        if value=='tjäna':
            print("Jobbat, fortsätter att jobba.");
            result = True;
        if value=='köpa':
            print("Jobbat, dags att handla!");
            result = True;
            
        return value;

    def handla(self, value):
        #print("value=" + value);
        result = False;
        if value=='hungrig':
            print("Handlat, dags att äta!");
            result = True;
        if value=='glad':
            print("Handlat, dags att umgås!");
            result = True;
        if value=='tjäna':
            print("Handlat, dags att jobba!");
            result = True;
        return value;

    def dricka(self, value):
        #print("value=" + value);
        result = False;
        if value=='trött':
            print("Druckit, dags att sova!");
            result = True;
        if value=='tjäna':
            print("Druckit, dags att jobba!");
            result = True;
        if value=='glad':
            print("Druckit, dags att umgås!");
            result = True;
        if value=='köpa':
            print("Druckit, dags att handla!");
            result = True;
        if value=='hungrig':
            print("Druckit, dags att äta!");
            result = True;    
        return value;
