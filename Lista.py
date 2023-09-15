lista = []
valor_final = 0 

while True: 
    item = str(input("Digite o item que deseja adicionar a lista, caso deseje encerrar a lista, digite 'sair' : "))
    if item.lower() == "sair":
        break 
    valor = float(input("Digite o valor do item: "))

    lista.append(item + str(valor))
    valor_final += valor 
lista.sort()

for item in lista:
    print( item )
print( valor_final)