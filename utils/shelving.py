class Shelving:
    def __init__(self, *, width, depth, max_weight=None):
        """Represent rectangular shelving
        width: the length from which items are accessible
        depth: the length that represents how far the shelving goes back.
        max_weight: the maximum weight a shelve can take as load"""
        self.width = width
        self.depth = depth
        self.max_weight = max_weight