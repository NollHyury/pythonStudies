myList = ['abacaxi','melancia','tomate']
myList2 = [1,2,3,4,5]
myList3 = [1,4.3,'Laranja',False]

print(myList)
print(myList2)
print(myList3[3])

#varrer uma lista
for item in myList:
    print(item)

#descobrir o tamanho de uma lista
print(len(myList2))

# adiciona um item a lista
myList.append("limao")

#remove um item da lista comparando o item passado como parametro
myList.remove("melancia")
print(myList)

# deleta itens da lista
del myList[1:2]
print(myList)

#verifica so parametro existe em uma lista
if "Laranja" in myList3:
    print("Laranja existe nesta lista")