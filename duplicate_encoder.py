def duplicate_encode(palabra):
    texto_minuscula = palabra.lower()
    resultado = ""
    
    for letra in texto_minuscula:
        if texto_minuscula.count(letra) == 1:
            resultado = resultado + "("
        else: 
            resultado = resultado + ")"
            
    return resultado
    