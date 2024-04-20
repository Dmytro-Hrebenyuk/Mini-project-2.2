import tracemalloc
import time
def create_table(n: int, m: int) -> list:
    """
    (int,int)->list
    Creates a table of nums using dynamic programming
    >>> create_table(4,6)
    [[1, 1, 1, 1, 1, 1], [1, 2, 3, 4, 5, 6], [1, 3, 6, 10, 15, 21], [1, 4, 10, 20, 35, 56]]
    """
    table = [[1] * m for _ in range(n)]
    for i in range(1, n):
        for j in range(1, m):
            table[i][j] = table[i - 1][j] + table[i][j - 1]
    return table

def flatten(lst: list) -> list:
    """
    Takes away all list to have only one list of numbers
    list->list
    >>> flatten([1,[2]])
    [1, 2]
    >>> flatten([1,2,[3,[4,5],6],7])
    [1, 2, 3, 4, 5, 6, 7]
    >>> flatten(['wow', [2,[[]]], [True]])
    ['wow', 2, True]
    >>> flatten([])
    []
    >>> flatten([[]])
    []
    >>> flatten(3)
    3
    """
    if not isinstance(lst, list):
        return lst  # Return single element list if input is not a list
    flattened = []
    stack = [lst]  # Wrap the input in a list to ensure consistency in handling
    while stack:
        item = stack.pop()
        if isinstance(item, list):
            stack.extend(reversed(item))  # Reverse and extend inner lists
        elif item is not None:
            flattened.append(item)
    return flattened

tracemalloc.start()
start1=time.time()
create_table(300,600)
end1=time.time()
memory_stats1 = tracemalloc.get_traced_memory()
tracemalloc.stop()

tracemalloc.start()
start2=time.time()
flatten(
    [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7], [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7]], [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7], [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7]]], [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7], [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7]], [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7], [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7]]]], [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7], [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7]], [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7], [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7]]], [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7], [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7]], [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7], [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7]]]]], [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7], [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7]], [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7], [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7]]], [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7], [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7]], [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7], [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7]]]], [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7], [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7]], [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7], [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7]]], [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7], [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7]], [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7], [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7]]]]]], [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7], [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7]], [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7], [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7]]], [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7], [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7]], [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7], [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7]]]], [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7], [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7]], [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7], [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7]]], [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7], [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7]], [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7], [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7]]]]], [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7], [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7]], [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7], [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7]]], [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7], [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7]], [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7], [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7]]]], [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7], [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7]], [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7], [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7]]], [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7], [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7]], [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7], [1, 2, [3, [4, 5], 6], 7, [1, 2, [3, [4, 5], 6], 7]]]]]]]]
)
end2=time.time()
memory_stats2 = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Crating a table took {end1-start1}")
print("Memory usage:", memory_stats1)
print()
print(f"Flatening took {end2-end1}")
print("Memory usage:", memory_stats2)