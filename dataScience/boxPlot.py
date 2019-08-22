#BoxPlot = diagrama de caixa
import matplotlib.pyplot as plt
import random


vetor = []

for i in range(13):
    vetor.append(random.randint(0,2500))


plt.title("BoxPlot")
plt.boxplot(vetor)
plt.show()