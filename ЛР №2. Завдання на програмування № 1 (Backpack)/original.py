class Item:
    """Class that describe item by name:str, weight:int(kg), value:int($)"""
    def __init__(self,name:str,weight:int,value:int) -> None:
        """Method that takes main parametrs for item
        >>> bread = Item("Bread", 1, 2)
        >>> bread.weight == 1
        True
        """
        self.name=name
        self.weight=weight
        self.value=value
    def __str__(self) -> str:
        """Method that print main item information
        >>> bread = Item("Bread", 1, 2)
        >>> print(bread)
        Bread (1 kg, $2)
        """
        return f"{self.name} ({self.weight} kg, ${self.value})"
    def __repr__(self) -> str:
        return self.name
class Backpack:
    """Class that describe main backpack parametrs and methods"""
    _Backpack__capacity=10
    def __init__(self) -> None:
        """Function that create backpack
        >>> backpack=Backpack()
        >>> backpack.items==[]
        True
        """
        self._items=[]
    def total_value(self):
        """Function that calculate total value of all items 
        in backpack
        >>> bread = Item("Bread", 1, 2)
        >>> backpack = Backpack()
        >>> backpack.add_item(bread)
        'Object added!'
        >>> backpack.total_value
        2
        """
        tota=0
        for i in self._items:
            tota+=i.value
        return tota
    def total_weight(self):
        """Function that calculate total value of all items 
        in backpack
        >>> bread = Item("Bread", 1, 2)
        >>> backpack = Backpack()
        >>> backpack.add_item(bread)
        'Object added!'
        >>> backpack.total_weight
        1
        """
        total=0
        for i in self._items:
            total+=i.weight
        return total
    @property
    def items(self):
        """method that set items in backpack
        >>> bread = Item("Bread", 1, 2)
        >>> backpack = Backpack()
        >>> backpack.add_item(bread)
        'Object added!'
        >>> print(backpack.items)
        ['Bread']
        """
        return self._items
    @items.setter
    def items(self,new):    
        """ 
        method that setter items 
        >>> backpack4 = Backpack()
        >>> backpack4.items = [Item("Watermelon", 200, 200), book, "Watermelon", 5, water]
        >>> len(backpack4.items) == 2
        """
        for i in new:
            self.add_item(i)
    @items.deleter
    def items(self):
        """
        method that deleted all items from backpack
        >>> backpack4 = Backpack()
        >>> backpack4.items = [Item("Watermelon", 200, 200), book, "Watermelon", 5, water]
        >>> len(backpack4.items) == 2
        >>> del backpack4.items
        >>> print(backpack4.items)
        []
        """
        self._items=[]
    total_value=property(total_value)
    total_weight=property(total_weight)
    def add_item(self,item):
        """
        method that add items to backpack
        >>> bread = Item("Bread", 1, 2)
        >>> backpack = Backpack()
        >>> backpack.add_item(bread)
        'Object added!'
        """
        if isinstance(item,Item):
            if item.weight+self.total_weight<=self._Backpack__capacity:
                self._items.append(item)
                return "Object added!"
            else:
                return f"Item '{item.name}' is too heavy for the backpack."
        return 'Item is not valid'
    def remove_item(self,item):
        """method taht remove items one items from backpack
        >>> bread = Item("Bread", 1, 2)
        >>> backpack = Backpack()
        >>> backpack.add_item(bread)
        'Object added!'
        >>> backpack.remove_item(bread)
        'Object succesfully removed.'
        """
        if item in self.items:
            self._items.remove(item)
            return "Object succesfully removed."
        else:
            return "False"
    def __str__(self) -> str:
        """method that print main information about backpack
        >>> bread = Item("Bread", 1, 2)
        >>> backpack = Backpack()
        >>> backpack.add_item(bread)
        'Object added!'
        >>> print(backpack)
        Backpack contains 1 item with total weight 1 kg and total value $2
        """
        if len(self._items)<2:
            return f"Backpack contains {len(self._items)} item with total \
weight {self.total_weight} kg and total value ${self.total_value}"
        else:
            return f"Backpack contains {len(self._items)} items with total \
weight {self.total_weight} kg and total value ${self.total_value}"
    @staticmethod
    def is_item_valid(item):
        """method that check if item is valid to backpack
        >>> backpack=Backpack()
        >>> backpack.is_item_valid(1)
        False
        """
        if isinstance(item,Item):
            if item.value<0 or item.weight<0:
                return False    
            return True
        return False
    @classmethod
    def set_capacity(cls,new):
        """method that change general backpacks capacity
        >>> backpack=Backpack()
        >>> Backpack.set_capacity(20)
        >>> backpack._Backpack__capacity
        20
        """
        cls._Backpack__capacity=new
def test_backpack_module():
    # Let us set up items that you can put in the backpack.
    # There are two special ones: clothing and food.
    # Items have 3: name, weight in kg, value in $.
    bread = Item("Bread", 1, 2)
    water = Item("Water", 2, 1)
    jacket = Item("Jacket", 2, 10)
    book = Item("Book", 3, 5)

    assert bread.weight == 1
    assert jacket.value == 10
    assert jacket.name == 'Jacket'

    assert str(bread) == "Bread (1 kg, $2)"
    assert str(jacket) == "Jacket (2 kg, $10)"

    # Now create object Backpack where we will put the items
    backpack = Backpack()

    # All backpacks have limit for total weight of items
    assert backpack._Backpack__capacity == 10

    assert backpack.items == []
    assert str(backpack) == "Backpack contains 0 item with total weight 0 kg and total value $0"

    assert backpack.add_item(bread) == "Object added!"
    assert len(backpack.items) == 1

    assert backpack.add_item(water) == "Object added!"

    backpack.add_item(jacket)
    backpack.add_item(book)
    assert str(backpack.items) == '[Bread, Water, Jacket, Book]'
    # Also backpack has two another attributes
    # which depend on the backpack's content.
    assert backpack.total_value == 18
    assert backpack.total_weight == 8

    # You should care about maximum capacity
    # of the backpack
    assert backpack.add_item(Item('Magazine', 5, 7)) == "Item 'Magazine' is too heavy for the backpack."

    assert backpack.is_item_valid('Magazine') == False
    assert Backpack.is_item_valid('Magazine') == False
    assert backpack.is_item_valid(Item('Magazine', -5, 7)) == False
    assert backpack.is_item_valid(Item('Magazine', 5, -7)) == False

    assert backpack.add_item('Magazine') == 'Item is not valid'
    # You can also remove items from backpack
    assert backpack.remove_item(book) == "Object succesfully removed."

    assert str(backpack) == "Backpack contains 3 items with total weight 5 kg and total value $13"
    assert backpack.add_item(Item('Magazine', 5, 7)) == "Object added!"
    assert str(backpack) == "Backpack contains 4 items with total weight 10 kg and total value $20"
    assert backpack.total_value == 20
    assert backpack.total_weight == 10

    backpack2 = Backpack()

    assert backpack2._Backpack__capacity == 10
    Backpack.set_capacity(20)
    assert backpack._Backpack__capacity == 20
    assert backpack2._Backpack__capacity == 20
    assert backpack2.total_value == 0
    assert backpack2.total_weight == 0

    # Class Backpack has method pack_backpach
    # which can create Backpack objects with already added items
    backpack3 = Backpack()
    backpack3.items = [water, water, water, Item('Apple', 2, 0.5)]

    assert len(backpack3.items) == 4
    assert backpack3.total_value == 3.5
    # But if the weight of added items will be heavier than capacity
    # it will return message
    backpack4 = Backpack()
    backpack4.items = [Item("Watermelon", 200, 200), book, "Watermelon", 5, water]
    assert len(backpack4.items) == 2
    assert backpack4.total_value == 6
    del backpack4.items
    assert backpack4.items == []
    assert str(backpack4) == "Backpack contains 0 item with total weight 0 kg and total value $0"
    print('Well done!')
test_backpack_module()
