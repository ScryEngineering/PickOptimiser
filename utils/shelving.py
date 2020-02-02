class Shelving:
    def __init__(self, *, width, depth, label:str, max_weight=None) -> None:
        """Represent rectangular shelving
        width: the length from which items are accessible
        depth: the length that represents how far the shelving goes back.
        max_weight: the maximum weight a shelve can take as load"""
        self.width = width
        self.depth = depth
        self.max_weight = max_weight
        self.label = label

    def __repr__(self) -> str:
        if self.max_weight:
            return f"Shelving(label={self.label}, width={self.width}, depth={self.depth}, max_weight={self.max_weight})"
        else:
            return f"Shelving(label={self.label}, width={self.width}, depth={self.depth})"