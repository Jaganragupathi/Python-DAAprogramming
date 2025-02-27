def subsets_recursive(items):
    if len(items) == 0:
        return [[]]
    subsets = []
    first = items[0]
    rest_subsets = subsets_recursive(items[1:])    
    for subset in rest_subsets:
        subsets.append(subset)
        subsets.append([first] + subset)
    return subsets
items = [1, 2, 3]
subsets = subsets_recursive(items)
for subset in subsets:
    print(subset)
