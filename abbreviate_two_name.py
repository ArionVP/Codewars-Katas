def abbrev_name(nombre_completo):
    nombre_separado = nombre_completo.split()
    
    inicial1 = nombre_separado[0][0].upper()
    inicial2 = nombre_separado[1][0].upper()
    
    resultado = f"{inicial1}.{inicial2}"
    return resultado