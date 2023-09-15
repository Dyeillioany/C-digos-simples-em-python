altura = float(input("Digite a altura em metros: "))
sexo = input("Digite o sexo (M/F): ").strip().upper()

if sexo == "M":
    peso_ideal = (72.7 * altura) - 58
    peso_arredondado = round(peso_ideal,2)
    print("O peso ideal para um homem com altura de", altura, "m é", peso_arredondado, "kg.")
elif sexo == "F":
    peso_ideal = (62.1 * altura) - 44.7
    peso_arredondado = round(peso_ideal,2)
    print("O peso ideal para uma mulher com altura de", altura, "m é", peso_arredondado, "kg.")
else:
    print("Sexo inválido. Por favor, digite M ou F.")
