def remove(texto_base):
    if texto_base.endswith("!"):
         return texto_base[:-1]
    else:
        return texto_base