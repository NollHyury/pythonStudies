#5.Escreva um programa que receba dois números e um sinal, e faça a operação matemática definida pelo sinal.

valueOne = float(input("enter first value: "))
valueTwo = float(input("enter second value: "))

def additionOperation():
    return valueOne + valueTwo

def subtractionOperation():
    return valueOne - valueTwo

def multiplicationOperation():
    return valueOne * valueTwo

def divisionOperation():
    return valueOne / valueTwo

def defineOperator(valueOperator = str(input("enter with math operator"))):
    if(valueOperator == "+"):
        return additionOperation()
    elif(valueOperator == "-"):
        return subtractionOperation()
    elif(valueOperator == "*"):
        return multiplicationOperation()
    elif(valueOperator == "/"):
        return divisionOperation()
    else :
        return "operador nao eh valido!"

print(defineOperator())
    