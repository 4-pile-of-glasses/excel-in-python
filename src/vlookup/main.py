sample_data = [
    ['Employee ID',	'Employee Name', 'Department ID'],
    ['101', 'Alice', '1'],
    ['102', 'Bob', '2'],
    ['103', 'Charlie', '3'],
    ['104', 'David', '1'],
    ['105', 'Eve', '2']
]

def VLOOKUP(lookup_value: any, lookup_table: list[list], column_index: int, approximate_match=False):
    column_index -= 1  # Adjust for 0-based indexing

    if not approximate_match:
        for row in lookup_table:
            if row and row[0] == lookup_value:  # Check if row exists and compare the first element
                try:
                    return row[column_index]
                except IndexError:
                    return None # Return None if column_index is out of range
        return None  # Return None if lookup_value is not found

    else:  # Approximate match
        # Assuming the first column is sorted for approximate match
        for i in range(len(lookup_table)):
            row = lookup_table[i]
            if row and row[0] == lookup_value:
                try:
                    return row[column_index]
                except IndexError:
                    return None
            elif row and isinstance(row[0], (int, float)) and isinstance(lookup_value, (int, float)) and row[0] > lookup_value: #Handles numeric comparison
                if i > 0:  # Check the previous row
                    try:
                        return lookup_table[i - 1][column_index]
                    except IndexError:
                        return None
                else:
                    return None  # No smaller value exists
        if lookup_table and isinstance(lookup_table[-1][0], (int, float)) and isinstance(lookup_value, (int, float)) and lookup_table[-1][0] <= lookup_value: #Handles numeric comparison for last element.
            try:
                return lookup_table[-1][column_index]
            except IndexError:
                return None
        return None  # No suitable match found

# Test cases
print(VLOOKUP('105', sample_data, 3))  # Exact match: 2
print(VLOOKUP('106', sample_data, 3))  # Not found: None
print(VLOOKUP('102', sample_data, 2))  # Exact match, different column: Bob
print(VLOOKUP('102', sample_data, 5)) #Column index out of range: None

#Example with approximate match
sample_data_approx = [
    ['Value', 'Result'],
    [1, 'A'],
    [3, 'C'],
    [5, 'E'],
    [7, 'G']
]

print(VLOOKUP(4, sample_data_approx, 2, approximate_match=True)) # Output: C
print(VLOOKUP(2, sample_data_approx, 2, approximate_match=True)) # Output: A
print(VLOOKUP(8, sample_data_approx, 2, approximate_match=True)) # Output: G
print(VLOOKUP(0, sample_data_approx, 2, approximate_match=True)) # Output: None
print(VLOOKUP(5, sample_data_approx, 2, approximate_match=True)) # Output: E