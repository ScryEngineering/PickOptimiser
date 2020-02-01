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

from typing import Iterable, List

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
        self._item_locs: dict = {}
        for item, loc in item_locations:
            self._item_locs[item] = loc

    def move_item(self, *, item, quantity: int=1, old_location, new_location):
        """Move a quantity of items from one place to another"""
        raise NotImplementedError

    def get_items_near_location(self, *, location: Location, tolerance):
        """Find all items that are near the given location within the tolerance given"""
        raise NotImplementedError

    def get_locations_of_item(self, *, item) -> List:
        """Find the locations where items are currently located"""
        res = []
        for current_item, loc in self._item_locs.items():
            if current_item == item:
                res.append(loc)
        return res