import matplotlib.pyplot as plt

x =[1 ,2, 3,4,5] #ID BARRAS
y =[2, 3, 7,1,0] #TAMANHO BARRAS

#LEGENDAS
plt.title("Bar Graph")
plt.xlabel("EIXO X")
plt.ylabel("EIXO Y")


plt.bar(x, y)
plt.show()