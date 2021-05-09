import time
from pyknow import *
class Greetings(KnowledgeEngine):
    @DefFacts()
    def _initial_action(self):
        yield Fact(Ticks = 0)
        yield Fact(NSsign = 'RED')
        yield Fact(WEsign = 'GREEN')
        yield Fact(switchTime = 8)
        yield Fact(startTime = 0)
        yield Fact(period = 10)
    
    # task 
    def exit(self):
        choice = input('are you going to quit?')
        if 'Y' in choice.upper(): 
            self.declare(Fact(action = 'halt'))
        
    def doTask(self,times):
        if times == switch:
            self.declare(Fact(switch = True))
            
    @Rule(AS.oldFact << Fact(Ticks=MATCH.times),
          Fact(switchTime = MATCH.switchTime),
          Fact(period = MATCH.period)
         )
    def ticker(self,oldFact,times,switchTime, period):
        time.sleep(1)
        self.retract(oldFact)
        if times == period:
            self.declare(Fact(Ticks = 0))
            self.exit()
        else:
            self.declare(Fact(Ticks = times + 1))
        print('*',end='')
   
    @Rule(
          Fact(Ticks = MATCH.times),
          Fact(startTime = MATCH.startTime),
          TEST(lambda startTime,times:times == startTime),
          salience= 2
       )
    def startSwitch0(self):
        self.declare(Fact(switch = True))
        #print(self.facts)
    
    @Rule(
          Fact(Ticks = MATCH.times),
          Fact(switchTime = MATCH.switchTime),
          TEST(lambda switchTime,times:times == switchTime),
          salience= 2
       )
    def startSwitch(self):
        self.declare(Fact(switch = True))
        #print(self.facts)
        
    @Rule(
        AS.oldSwtich << Fact(switch = True),
        AS.oldNS << Fact(NSsign = 'RED'),
        AS.oldWE << Fact(WEsign = 'GREEN'),
        salience = 2
      )
    def switch1(self,oldSwtich,oldNS,oldWE): 
        self.declare(Fact(NSsign = 'GREEN'))
        self.declare(Fact(WEsign = 'RED'))
        self.retract(oldSwtich)
        self.retract(oldWE)
        self.retract(oldNS) 
        
    @Rule(
        AS.oldSwtich << Fact(switch = True),
        AS.oldNS << Fact(NSsign = 'GREEN'),
        AS.oldWE << Fact(WEsign = 'RED'),
        salience = 2
      )
    def switch2(self,oldSwtich,oldNS,oldWE):
        self.declare(Fact(NSsign = 'RED'))
        self.declare(Fact(WEsign = 'GREEN'))
        self.retract(oldSwtich)
        self.retract(oldWE)
        self.retract(oldNS)
        
    @Rule(
        Fact(NSsign = MATCH.NScolor),
        Fact(WEsign = MATCH.WEcolor),
        salience = 2
      )
    def show(self,NScolor,WEcolor):
        print('\nNS:WE={}:{}\n'.format(NScolor,WEcolor))

        
    @Rule(
        Fact(action = 'halt'),
        salience = 2
      )
    def halts(self):
        print('bye')
        self.halt()
        
engine = Greetings()
engine.reset()  # Prepare the engine for the execution.
engine.run()  # Run it!
