class Node():
    def __init__(self):
        self.id = None          # str.
        self.descr = None       # str.
        self.successors = set() # contains tuples: (id, edge).
        self.parents = set()    # contains ids.
        self.action = None      # str or function. The step to be taken.
        self.test = None        # str or function. Test of step's outcome.

