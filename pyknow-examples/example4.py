from pyknow import *
class Greeting(KnowledgeEngine):
    @DefFacts()
    def init(self):
        yield Fact(action='greet')
    @Rule(
        AS.r << Fact(action = MATCH.f),
    )
    def SayHello(self,r,f):
       print("field:",f," rule:",r) 
       for i in self.facts[1].keys():
            print(i,":",self.facts[1][i])
   
engin mplee= Greeting()
engine.reset()
engine.run()
