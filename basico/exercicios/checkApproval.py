#Resposta do exercicio 2.Faça um programa que receba duas notas digitadas pelo usuário.
#Se a nota for maior ou igual a seis, escreva aprovado, senão escreva reprovado. 



def calculateAverage(ratingOne = float(input("what is your first rating:")),
    ratingTwo = float(input("what is your second rating:"))):
    average = (ratingOne + ratingTwo) / 2
    if(checkMax(average)):
        if(average >= 6.0):
            return True
        else:
            return False
    else:
        return False


def checkMax(param):
    if(param > 10):
        print("Please check the entered values!")
        return False
    else:
        return True


print(calculateAverage())
    