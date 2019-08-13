seq = "Hyury Luis Da Silva Noll " + "\n"
print(seq)

# deixa a string em letra minuscula
print(seq.lower())


# remove os caractéris especiais
print(seq.strip())


# deixa a string em letra maiuscula
seq = seq.upper()
print(seq)

# converte uma string em uma lista
x = seq.split("Y")
print(x)

# busca o indice onde esta localizado a palavra passada por parametro, e retorna o mesmo.
busca = seq.find("NOLL")
print(busca)

# altera um determinado valor dentro de uma string
busca = seq
busca  = busca.replace("HYURY","LUCAS")
print(busca)


