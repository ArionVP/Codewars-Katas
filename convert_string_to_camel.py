def to_camel_case(texto_base):
    if not texto_base:
        return ""
    
    texto_normal = texto_base.replace("_","-")
    lista_de_palabras = texto_normal.split("-")
    texto_final = lista_de_palabras[0]
    
    for palabra in lista_de_palabras[1:]:
        texto_final += palabra.capitalize()
    
    return texto_final

    resultado_1 = to_camel_case("mi_variable_ejemplo")
    
    print(resultado_1)