import matplotlib.pyplot as plt

x =[1 ,2, 5]
y =[2, 3, 7]

#TÍTULO
plt.title("My first graph with Python")

#EIXOS
plt.xlabel("EIXO X")
plt.ylabel("EIXO Y")


plt.plot(x, y)
plt.show()