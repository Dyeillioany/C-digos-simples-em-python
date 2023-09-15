cor = str(input("Digite a cor: "))
if cor == "Azul".lower(): 
    print("O CD custa R$10,00")
elif cor == "Verde".lower(): 
    print("O CD custa R$20,00")
elif cor == "Amarelo".lower():
    print("O CD custa R$30,00")
elif cor == "Vermelho".lower():
    print("O CD custa R$40,00")
else:
    print("Cor inválida! Tente novamente com as cores válidas.")
    