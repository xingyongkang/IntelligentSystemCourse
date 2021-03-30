from pyknow import *
class Greeting(KnowledgeEngine):
    @DefFacts()
    def init(self):
        yield Fact(action='greet')
        yield Fact(name='zhangsan')
        
    @Rule(
        Fact(action = 'greet')
    )
    def SayHello(self):
        print('hello world')
        
    @Rule(
        Fact(action = 'greet'),
        Fact(name = "zhangsan")
    )
    def SayHelloZS(self):
        print('hello world! zhangsan')


engine = Greeting()
engine.reset()
engine.run()
    
