def create_table(rows: int, columns: int) -> list:
    """
    Create a table of numbers using recursion.
    
    Args:
        rows (int): Number of rows in the table.
        columns (int): Number of columns in the table.
    
    Returns:
        list: A 2D list representing the table.
        
    Example:
        >>> create_table(4, 6)
        [[1, 1, 1, 1, 1, 1], [1, 2, 3, 4, 5, 6], [1, 3, 6, 10, 15, 21], [1, 4, 10, 20, 35, 56]]
    """
    # Initialize the table with zeros
    table = [[0] * columns for _ in range(rows)]
    
    # Fill the first row and first column with 1s
    for i in range(rows):
        table[i][0] = 1
    for j in range(columns):
        table[0][j] = 1
    
    # Define a helper function to fill the table recursively
    def fill_table(i, j):
        if i < rows and j < columns:
            if table[i][j] == 0:
                # Fill the cell using recursive calls
                table[i][j] = fill_table(i - 1, j) + fill_table(i, j - 1)
            return table[i][j]
        return 0
    
    # Start filling the table recursively from the bottom-right cell
    fill_table(rows - 1, columns - 1)
    
    return table

def flatten_list(lst: list) -> list:
    """
    Flatten a nested list to a single list of elements.
    
    Args:
        lst (list): The input list which may contain nested lists.
    
    Returns:
        list: A flattened list with no nested structure.
        
    Example:
        >>> flatten_list([1, [2]])
        [1, 2]
        >>> flatten_list([1, 2, [3, [4, 5], 6], 7])
        [1, 2, 3, 4, 5, 6, 7]
        >>> flatten_list(['wow', [2, [[]]], [True]])
        ['wow', 2, True]
        >>> flatten_list([])
        []
        >>> flatten_list([[]])
        []
        >>> flatten_list(3)
        3
    """
    # Base case: if the input is not a list, return it as is
    if not isinstance(lst, list):
        return lst
    
    flattened = []
    for item in lst:
        if isinstance(item, list):
            # Recursively flatten nested lists
            flattened.extend(flatten_list(item))
        elif item is not None:
            # Add non-None elements to the flattened list
            flattened.append(item)
    
    return flattened
if __name__ == "__main__":
    import doctest
    doctest.testmod()