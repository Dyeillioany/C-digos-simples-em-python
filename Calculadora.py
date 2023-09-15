import math

def mais(num1, num2):
    return num1 + num2

def menos(num1, num2):
    return num1 - num2

def mult(num1, num2):
    return num1 * num2

def elevado(numy, numx):
    return numy ** numx

def elev(numx, numy):
    return numx ** numy

def seno(angulo):
    ang = math.radians(angulo)
    seno_ang = math.sin(ang)
    return seno_ang

def cosseno(angulo):
    ang = math.radians(angulo)
    cos_ang = math.cos(ang)
    return cos_ang

def tangente(angulo):
    ang = math.radians(angulo)
    tang_ang = math.tan(ang)
    return tang_ang



   
def calculadora():
    while True:
        print("Oferecemos as seguintes operações em nossa calculadora científica:")
        print("A - Adição")
        print("B - Subtração")
        print("C - Multiplicação")
        print("D - Y elevado a X")
        print("E - X elevado a Y")
        print("F - Função Seno")
        print("G - Função Cosseno")
        print("H - Função Tangente")
        print("K - Para encerrar a calculadora digite -1")
        
        operacao_usuario = input("Digite a operação que deseja: ").strip().lower()
        
        if operacao_usuario == "a":
            num1 = int(input("Digite o primeiro número: "))
            num2 = int(input("Digite o segundo número: "))
            resultado = mais(num1, num2)
            print("O resultado é:", resultado)
        elif operacao_usuario == "b":
            num1 = int(input("Digite o primeiro número: "))
            num2 = int(input("Digite o segundo número: "))
            resultado = menos(num1, num2)
            print("O resultado é:", resultado)
        elif operacao_usuario == "c":
            num1 = int(input("Digite o primeiro número: "))
            num2 = int(input("Digite o segundo número: "))
            resultado = mult(num1, num2)
            print("O resultado é:", resultado)
        elif operacao_usuario == "d":
            numy = int(input("Digite o primeiro número: "))
            numx = int(input("Digite o segundo número: "))
            resultado = elevado(numy, numx)
            print("O resultado é:", resultado)
        elif operacao_usuario == "e":
            numx = int(input("Digite o primeiro número: "))
            numy = int(input("Digite o segundo número: "))
            resultado = elev(numx, numy)
            print("O resultado é:", resultado)
        elif operacao_usuario == "f":
            angulo = int(input("Digite o ângulo em graus: "))
            resultado = seno(angulo)
            print("O resultado é:", resultado)
        elif operacao_usuario == "g":
            angulo = int(input("Digite o ângulo em graus: "))
            resultado = cosseno(angulo)
            print("O resultado é:", resultado)
        elif operacao_usuario == "h":
            angulo = int(input("Digite o ângulo em graus: "))
            resultado = tangente(angulo)
            print("O resultado é:", resultado)
        elif operacao_usuario == "-1":
            break


calculadora()