"""Represent an item in the warehouse"""

from dimensions import SpatialDimensions

class Item:
    """Representation of an item in the warehouse"""
    def __init__(self, *, SKU, weight, dimensions: SpatialDimensions):
        self.SKU = SKU
        self.weight = weight
        self.dimensions = dimensions
