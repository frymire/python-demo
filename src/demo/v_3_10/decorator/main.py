from src.demo.v_3_10.decorator.component import ConcreteComponent
from src.demo.v_3_10.decorator.decorator import ConcreteDecoratorA, ConcreteDecoratorB

simple = ConcreteComponent()
decorated1 = ConcreteDecoratorA(simple)
decorated2 = ConcreteDecoratorB(decorated1)

print("Simple component:", simple.run())
print("Decorated component #1:", decorated1.run())
print("Decorated component #2:", decorated2.run())
