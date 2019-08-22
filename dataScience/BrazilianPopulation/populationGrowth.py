#Crescimento da população brasileira 1980 - 2016
#DataSus database do governo

import matplotlib.pyplot as plt

dados = open("dataScience\BrazilianPopulation\populacao_brasileira.csv", "r").readlines()

years = []
population = []

for i in range(len(dados)):
    if i != 0 :
        linha = dados[i].split(";")
        years.append(int(linha[0]))
        population.append(int(linha[1]))

plt.title("Brazilian Population Growth from 1980 to 2016 ")
plt.xlabel("Year")
plt.ylabel("Population ^100MM")
plt.bar(years,population)
plt.show()