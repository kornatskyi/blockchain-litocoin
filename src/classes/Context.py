from src.classes import Node


class Context:
    """
    Context for sharing state acros the app
    """
    def __init__(self, node=None) -> None:
        self.node: Node = node
