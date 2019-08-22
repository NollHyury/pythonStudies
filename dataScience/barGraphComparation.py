import matplotlib.pyplot as plt

x1 = [1,3,5,7,9] #ID BARRAS
y1 = [2,4,5,6,1] #Tamanho das barras

x2 = [2,4,6,8,10] #ID BARRAS
y2 = [5,1,5,3,6]

#LEGENDAS
plt.title("Bar Graph Comparation")
plt.xlabel("EIXO X")
plt.ylabel("EIXO Y")


plt.bar(x1,y1, label = "Grupo 1")
plt.bar(x2,y2, label = "Grupo 2")
plt.legend()
plt.show()