def comp(array1, array2):
    
    if array1 is None or array2 is None:
        return False
    
    if len(array1) != len(array2):
        return False
    
    squared = []
    
    for number in array1:
        squared.append(number ** 2)
        
    return sorted(squared) == sorted(array2)


array1 = [121, 144, 19, 161, 19, 144, 19, 11]
array2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
assert comp(array1, array2)
assert comp([], [])
assert comp([2], [4])
# assert comp([1, 2, 3], [1, 4])   /// False 