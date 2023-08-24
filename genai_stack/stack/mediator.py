from genai_stack.stack.stack import Stack


class Mediator:
    """This is the mediator class which handles all the intercomponent communication within a Stack.

    This is design pattern which allows for bidirectional communication between different components in the stack.
    Further reference: https://refactoring.guru/design-patterns/mediator/python/example
    """

    def __init__(self, stack: Stack):
        self._stack = stack

    # Add more methods for inter component communication as we build the components
