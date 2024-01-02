from .component import Component


class Decorator(Component):
    """
    The base Decorator class follows the same interface as the other components.
    The primary purpose of this class is to define the wrapping interface for
    all concrete decorators. The default implementation of the wrapping code
    might include a field for storing a wrapped component and the means to
    initialize it.
    """
    _component: Component = None

    def __init__(self, component: Component):
        self._component = component

    @property
    def component(self):
        """
        The Decorator delegates all work to the wrapped component.
        """
        return self._component

    def run(self):
        return self._component.run()


class ConcreteDecoratorA(Decorator):
    """
    Concrete Decorators call the wrapped object and alter its result in some way.
    """
    def run(self):
        """
        Decorators may call parent implementation of the operation, instead of
        calling the wrapped object directly. This approach simplifies extension
        of decorator classes.
        """
        return f"ConcreteDecoratorA({self.component.run()})"


class ConcreteDecoratorB(Decorator):
    """
    Decorators can execute their behavior either before or after the call to a
    wrapped object.
    """
    def run(self):
        return f"ConcreteDecoratorB({self.component.run()})"
