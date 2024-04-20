class Item:
    """
    Class that describes an item by name, weight (kg), and value ($).
    """

    def __init__(self, name: str, weight: int, value: int) -> None:
        """
        Initializes an item with name, weight, and value.
        """
        self.name = name
        self.weight = weight
        self.value = value

    def __str__(self) -> str:
        """
        Returns a string representation of the item.
        """
        return f"{self.name} ({self.weight} kg, ${self.value})"

    def __repr__(self) -> str:
        """
        Returns a string representation of the item for debugging purposes.
        """
        return self.name


class Backpack:
    """
    Class that describes a backpack and its methods.
    """

    __capacity = 10

    def __init__(self) -> None:
        """
        Initializes a backpack with an empty list of items.
        """
        self._items = []

    @property
    def items(self):
        """
        Returns the items in the backpack.
        """
        return self._items

    @items.setter
    def items(self, new_items):
        """
        Sets the items in the backpack.
        """
        for item in new_items:
            self.add_item(item)

    @items.deleter
    def items(self):
        """
        Deletes all items from the backpack.
        """
        self._items = []

    @property
    def total_value(self):
        """
        Calculates the total value of all items in the backpack.
        """
        return sum(item.value for item in self._items)

    @property
    def total_weight(self):
        """
        Calculates the total weight of all items in the backpack.
        """
        return sum(item.weight for item in self._items)

    def add_item(self, item):
        """
        Adds an item to the backpack if it does not exceed the capacity.
        """
        if isinstance(item, Item):
            if item.weight + self.total_weight <= self.__capacity:
                self._items.append(item)
                return "Object added!"
            else:
                return f"Item '{item.name}' is too heavy for the backpack."
        return 'Item is not valid'

    def remove_item(self, item):
        """
        Removes an item from the backpack.
        """
        if item in self._items:
            self._items.remove(item)
            return "Object succesfully removed."
        else:
            return "Item not found in backpack."

    def __str__(self) -> str:
        """
        Returns a string representation of the backpack.
        """
        item_count = len(self._items)
        item_plural = "items" if item_count > 1 else "item"
        return f"Backpack contains {item_count} {item_plural} with total weight {self.total_weight} kg and total value ${self.total_value}"

    @staticmethod
    def is_item_valid(item):
        """
        Checks if an item is valid.
        """
        if isinstance(item, Item):
            if item.value < 0 or item.weight < 0:
                return False
            return True
        return False

    @classmethod
    def set_capacity(cls, new_capacity):
        """
        Sets the capacity of the backpack.
        """
        cls.__capacity = new_capacity
