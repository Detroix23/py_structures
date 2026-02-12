from structures_detroix23.modules import nodes as nodes

class Graph:
    register: list[nodes.Node]
    def __init__(self, register: list[nodes.Node] | None = None) -> None: ...

class Explorer:
    graph: Graph
    current: nodes.Node
    seen: set[nodes.Node]
    def __init__(self, graph: Graph, current: nodes.Node) -> None: ...
    def move(self, destination: nodes.Node) -> bool: ...
