num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
opcao = int(input("Digite a operação desejada (1 para média, 2 para diferença, 3 para produto ou 4 para divisão): "))

if opcao == 1:
    media = (num1 + num2) / 2
    print("A média entre", num1, "e", num2, "é", media)
elif opcao == 2:
    diferenca = num1 - num2
    print("A diferença entre", num1, "e", num2, "é", diferenca)
elif opcao == 3:
    produto = num1 * num2
    print("O produto entre", num1, "e", num2, "é", produto)
elif opcao == 4:
    if num2 != 0:
        divisao = num1 / num2
        print("A divisão de", num1, "por", num2, "é", divisao)
    else:
        print("Não é possível dividir por zero")
else:
    print("Opção inválida. Por favor, escolha uma opção válida (1, 2, 3 ou 4).")