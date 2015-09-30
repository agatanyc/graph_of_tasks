import json
import node
import os

class Graph():
    """Instantiate nodes and add them to a graph object."""
    def __init__(self, filename=None):
        self.graph = {}      # Key: id; value: instance of Node.
        self.paths = set()   # Each path in this set is unique tuple of ids.
        self.orphans = set() # Contains ids.
        self.populate_graph(filename)

    def populate_graph(self, filename=None):
        """Populate graph from file (JSON format)."""
        # Check for existence of file and open.
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                content = f.read()
            dictionary = json.loads(content)
        else return

        # For each item, create node.
        for item in dictionary:
            node = Node()
            node.id = item
            # Populate string attributes of node.
            attrs = ['descr', 'action', 'test']
            for attr in attrs:
                if attr in dictionary[item]:
                    setattr(node, attr, dictionary[item][attr])

            # Populate 'successors' set.
            node.successors = set(dictionary[item]['successors']

            # Populate 'parents' set.
            # This must depend on self.populate_all_paths.
            pass


        # For each node, populate parents.

    def populate_all_paths(self):
        """Conduct breadth-first search on graph."""
        pass

    def find_paths(self, start, finish):
        """Look up all paths between start and finish."""
        return [path for path in self.paths
                if path[0] == start and path[-1] == finish]

    def add_node(self, node):
        """Add node and its connections."""
        # Add node to graph.

        pass

    def delete_node(self, node):
        """Delete node and its connections."""
        # Remove node.id from the successors set in node.parents.
        for parent in node.parents:
            successors = parent.successors
            for successor in successors:
                if successor[0] == node.id:
                    self.graph[parent].successors.remove(successor)

        # Remove node.id from the parents set in node.successors.
        for successor in node.successors:
            parents = successor.parents
            for parent in parents:
                if parent == node.id:
                    self.graph[successor].parents.remove[parent

        # Find new orphans.
        self.find_orphans(node.successors)

        # Remove from self.paths any path containing node.
        # Can we index all such paths to make this process faster?

        # Last of all, delete node.id from self.graph.
        del self.graph[node.id]

    def delete_edge(self, node):
        """Delete a particular edge to a node."""
        pass

    def move_node(self, node, new_parents):
        """Move an existing node."""
        pass

    def find_orphans(self, successors):
        """Check each successor for orphanhood; add to self.orphans."""
        if isinstance(successors, str):
            # In case we have not a set but a single string, make into set.
            successors = {successors}
        else:
            # If node has no parents, add to set of orphans.
            for successor in successors:
                if not len(successor.parents):
                    self.orphans.add(successor)

