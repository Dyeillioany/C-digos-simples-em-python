idade = int(input("Digite sua idade: "))
soma = (idade - 18)
soma2 = (18 - idade)

if idade >= 18:
    print("Sim, você já pode obter sua carteira, esse direito esta desponível a ",soma,"anos.")
elif idade < 18: 
    print("Você ainda não pode obter esse documento, esse direito estará disponível em",soma2,"anos.")