nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print("Aprovado.")

elif media < 7 and media >= 5:
    print("Recuperação.")

elif media < 5:
    print("Reprovado.")