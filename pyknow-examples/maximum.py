from pyknow import *
class Maximum(KnowledgeEngine):
    @Rule(NOT(Fact(max=W())))
    def init(self):
        self.declare(Fact(max=0))
    
    @Rule(Fact(val=MATCH.val),
          AS.m << Fact(max=MATCH.max),
          TEST(lambda max, val: val > max))
    def compute_max(self, m, val,max):
        self.modify(m, max=val)
        #print(max,"->",val)
    
    @Rule(AS.v << Fact(val=MATCH.val),
          Fact(max=MATCH.max),
          TEST(lambda max, val: val <= max))
    def remove_val(self, v):
        self.retract(v)
            
    @Rule(AS.v << Fact(max=W()),
          NOT(Fact(val=W())))
    def print_max(self, v):
        print("Max:", v['max'])

engine = Maximum()
engine.reset()
engine.declare(*[Fact(val= i) for i in [30,58,12,20,35,8,58]])
engine.run()
