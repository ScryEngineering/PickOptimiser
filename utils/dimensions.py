"""Representation of dimensional data,
using pint to ensure dimensional data is correct across"""
import pint

ureg = pint.UnitRegistry()

class SpatialDimensions:
    """Represent spatial dimensions"""
    def __init__(self, *, length, width, height):
        self.length = length
        self.width = width
        self.height = height