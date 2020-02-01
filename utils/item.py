"""Represent an item in the warehouse"""

from dimensions import SpatialDimensions

class Item:
    """Representation of an item in the warehouse"""
    def __init__(self, *, SKU, weight, dimensions: SpatialDimensions, max_stack: int=1):
        """Representations of an item to be stored
        SKU: stock keeping unit (TODO: is this unique?)
        weight: the weight of the item
        dimensions: the spatial dimensions of the item
        max_stack: how many of these items can be stacked on top of each other
        """
        self.SKU = SKU
        self.weight = weight
        self.dimensions = dimensions
        self.max_stack = max_stack
