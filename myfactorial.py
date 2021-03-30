from pyknow import *
class Engine(KnowledgeEngine):
    @DefFacts()
    def first(self):
        yield Fact(n = 0, res = 1)
        yield Fact(goal = 4)
        
    @Rule(
        AS.r << Fact(n = MATCH.n,res = MATCH.res),
        Fact(goal = MATCH.g),
        TEST(lambda n,g: n<g)
    )
    def Factorial(self, r, n, res):
        self.declare(
            Fact(n = n+1, res = (n + 1) * res)
        )
        self.retract(r)
