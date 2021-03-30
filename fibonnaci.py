from pyknow import *
class FibonacciDigit(Fact):
    position = Field(int, mandatory=True)
    value = Field(int, mandatory=True)


class FibonacciCalculator(KnowledgeEngine):    
    @DefFacts()
    def set_target_position(self, target):
        yield Fact(target_position=target)

    @DefFacts()
    def init_sequence(self):
        yield FibonacciDigit(position=1, value=1)
        yield FibonacciDigit(position=2, value=1)

    @Rule(
        FibonacciDigit(
            position=MATCH.p1,
            value=MATCH.v1),
        FibonacciDigit(
            position=MATCH.p2,
            value=MATCH.v2),
        TEST(
            lambda p1, p2: p2 == p1 + 1),
        Fact(
            target_position=MATCH.t),
        TEST(
            lambda p2, t: p2 < t))
    def compute_next(self, p2, v1, v2):
        next_digit = FibonacciDigit(
            position=p2 + 1,
            value=v1 + v2)

        self.declare(next_digit)
        print(p2+1, ":",v1 + v2)
    
    @Rule(
        Fact(
            target_position=MATCH.t),
        FibonacciDigit(
            position=MATCH.t,
            value=MATCH.v))
    def print_last(self, t, v):
        print("Fibonnaci digit in position {position} is {value}".format(
            position=t, value=v))
