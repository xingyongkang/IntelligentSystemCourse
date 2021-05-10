import time
from pyknow import *
class Greetings(KnowledgeEngine):
    @DefFacts()
    def _initial_action(self):
        yield Fact(Ticks = 0)
        yield Fact(NSsign = 'RED')
        yield Fact(WEsign = 'GREEN')
        yield Fact(switchTime = 4)
        yield Fact(startTime = 0)
        yield Fact(period = 8)
    
    @Rule(AS.oldFact << Fact(Ticks=MATCH.times))
    def ticker(self,times,oldFact):
        time.sleep(1)
        self.retract(oldFact)
        self.declare(Fact(Ticks = times + 1))
        print('*',end='')
   

    @Rule(AS.oldFact << Fact(Ticks=MATCH.times),
          Fact(period = MATCH.period),
          TEST(lambda times,period: times == period),
          salience = 2
         )
    def exit(self,oldFact):
        choice = input('are you going to quit?')
        if 'Y' in choice.upper(): 
            self.declare(Fact(action = 'halt'))
        else:
            self.retract(oldFact)
            self.declare(Fact(Ticks = 0))
        
        
            
    @Rule(
          Fact(Ticks = MATCH.times),
          Fact(startTime = MATCH.startTime),
          TEST(lambda startTime,times:times == startTime),
          salience= 2
       )
    def firstSwitch(self):
        self.declare(Fact(switch = True))
    
    @Rule(
          Fact(Ticks = MATCH.times),
          Fact(switchTime = MATCH.switchTime),
          TEST(lambda switchTime,times:times == switchTime),
          salience= 2
       )
    def secondSwitch(self):
        self.declare(Fact(switch = True))
        
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
