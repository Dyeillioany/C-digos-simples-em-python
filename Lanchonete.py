produto = int(input("Temos os seguintes produtos:\n"
                    "Codigo: 100 - Cachorro quente - R$5.00\n"
                    "Codigo: 101 - Bauru Simples - R$10.00\n"
                    "Codigo: 102 - Hamburguer - R$12.00\n"
                    "Codigo: 103 - Cheeseburguer - R$3.00\n"
                    "Codigo: 104 - Refrigerante - R$4.00\n"
                    "Caso deseje algum, apenas digite o código dele aqui: "))

print("="*60)

quant = int(input("Digite a quantidade desejável: "))

if produto == 100:
    print(f"Você irá pagar R${5.0 * quant} pelo cachorro quente")

elif produto == 101:
    print(f"Você irá pagar R${10.0 * quant} pelo Bauru Simples")

elif produto == 102:
    print(f"Você irá pagar R${12.0 * quant} pelo Hamburguer")

elif produto == 103:
    print(f"Você irá pagar R${3.0 * quant} pelo CheeseBurguer")


elif produto == 104:
    print(f"Você irá pagar R${4.0 * quant} pelo Refrigerante")