genero = str(input("Caso você seja homem, escreva a letra M. Caso você seja mulher, escreva a letra F"
                   "\nDigite aqui: ")).strip().upper()

idade = float(input("Digite sua idade aqui: "))

tempo_contri = float(input("Digite o seu tempo de contribuição com o INSS aqui: "))

if idade >= 65 and genero == "M":
    print("Você pode se aposentar.")

elif idade >= 60 and genero == "F":
    print("Você pode se aposentar.")

elif idade >= 55 and genero == "F" and tempo_contri >= 30:
    print("Você pode se aposentar.")

else:
    print("Você não pode se aposentar.")