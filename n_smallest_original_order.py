def first_n_smallest(listaNum, NumDevolver):
    numSeleccionados = []
    copia_de_lista = listaNum.copy()
    cantidadNum = min(NumDevolver, len(listaNum))

    for repeticion in range(cantidadNum):
        numMenor = min(copia_de_lista)
        numSeleccionados.append(numMenor)
        copia_de_lista.remove(numMenor)

    resultado = []

    for numero in listaNum:
        if numero in numSeleccionados:
            resultado.append(numero)
            numSeleccionados.remove(numero)

    return resultado

assert(first_n_smallest([1,2,3,4,5],1) == [1])
assert(first_n_smallest([1,2,3,4,5],3) == [1,2,3])
assert(first_n_smallest([5,4,3,2,1],3) == [3,2,1])
assert(first_n_smallest([1,2,3,1,2],3) == [1,2,1])
assert(first_n_smallest([1,2,3,-4,0],3) == [1,-4,0]) 
assert(first_n_smallest([1,2,3,4,5],0) == [])
assert(first_n_smallest([1,2,3,4,5],5) == [1,2,3,4,5])
assert(first_n_smallest([1,2,3,4,2],4) == [1,2,3,2])
assert(first_n_smallest([2,1,2,3,4,2],2) == [2,1])
assert(first_n_smallest([2,1,2,3,4,2],3) == [2,1,2])
assert(first_n_smallest([2,1,2,3,4,2],4) == [2,1,2,2])