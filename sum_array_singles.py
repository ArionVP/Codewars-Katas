def repeats(arr):
    contador = 0
    
    for num in arr:
        if arr.count(num) == 1:
            contador += num
            
    return contador