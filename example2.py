from pyknow import *
class Greeting(KnowledgeEngine):
    @DefFacts()
    def init(self):
        yield Fact(action='greet')
        
    @Rule(
        Fact(action = 'greet'),
        NOT(Fact(Name = W()))
    )
    def SayHello(self):
        getname = input('what is your name?')
        self.declare(Fact(name = getname))
        
    @Rule(
        Fact(action = 'greet'),
        Fact(name = MATCH.userName)
    )
    def SayHelloZS(self,userName):
        print('hello world',userName)


engine = Greeting()
engine.reset()
engine.run()
