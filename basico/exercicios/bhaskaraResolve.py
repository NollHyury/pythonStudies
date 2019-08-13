#3.Escreva um programa que resolva uma equação de segundo grau.   

a = -2
b = 3
c = 5

#determina o valor de delta
delta = b**2 -4*a*c

# efetua o calculo da raiz quadrada
deltaRoot = delta ** (0.5)

#efetua o calculo com o operador de adição
xBig = (-b + deltaRoot) / (2*a)

#efetua o calculo com o operador de subtração
xSmall = (-b - deltaRoot) / (2*a)

print("Big value: "+str(xBig))
print("Small value: "+str(xSmall))
