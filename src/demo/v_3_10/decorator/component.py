class Component:
    """
    The base Component interface defines operations that can be altered by
    decorators.
    """
    def run(self):
        pass


class ConcreteComponent(Component):
    """
    Concrete Components provide default implementations of the operations. There
    might be several variations of these classes.
    """
    def run(self):
        return "ConcreteComponent"
