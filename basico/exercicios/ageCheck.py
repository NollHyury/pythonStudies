#Resposta do exercicio 1.Faça um programa que receba a idade do usuário e diga se ele é maior ou menor de idade. 

def ageCheck(ageUser = int(input("how old are you?"))):
    if (ageUser >= 18):
        return True
    else:
        return False

print(ageCheck())
