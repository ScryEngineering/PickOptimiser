"""Representation of a warehouse layout

    x
+-------+
|       |
|       |
|       | y
|       |
|       |
+-------+

Heights represented as z
"""

from typing import Iterable

class Location:
    """represent the location of some entity in physical coordinates"""
    def __init__(self, x, y, z):
        """TODO: force dimensionality check"""
        self.x = x
        self.y = y
        self.z = z


class Warehouse:
    """Keep track of where items are in a warehouse"""
    def __init__(self, *, item_locations: Iterable[object, Location]):
        raise NotImplementedError

    def get_items_near_location(self, *, location, tolerance):
        """Find all items that are near the given location within the tolerance given"""
        raise NotImplementedError

    def get_locations_of_item(self, *, item):
        """Find the locations where items are currently located"""
        raise NotImplementedError