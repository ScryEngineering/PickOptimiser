"""Representation of dimensional data,
using pint to ensure dimensional data is correct across the codebase, always import the unit registry from here"""
import pint

ureg = pint.UnitRegistry()

class SpatialDimensions:
    """Represent spatial dimensions"""
    def __init__(self, *, length, width, height):
        """Spatial dimensions
        TODO: force dimensionality check using Pint"""
        self.length = length
        self.width = width
        self.height = height