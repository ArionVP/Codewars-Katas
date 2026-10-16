def alphabet_position(text):
    resultado = ""
    
    for letra in text:
        if letra.isalpha():
            posicion = ord(letra.lower()) - ord("a") + 1
            resultado = resultado + str(posicion) + " "
            
    resultado = resultado.strip()
    
    return resultado

