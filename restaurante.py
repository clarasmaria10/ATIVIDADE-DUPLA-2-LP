import os

os.system('cls || clear')


pratos = []
precos = []


print('== SABOR DA CASA ==')
print(' 1 - Picanha ..... R$25,00\n 2 - Lasanha ..... R$20,00\n 3 - Strogonoff ..... R$18,00\n 4 - Bife Acebolado ..... R$15,00\n 5 - Pão com ovo ..... R$5,00')

while True:
    pedido = int(input('Digite o número do prato desejado: '))
    
    match pedido:
        case 1:
            prato = 'PICANHA'
            preco = 25
        
        case 2:
            prato = 'LASANHA'
            preco = 20
        
        case 3:
            prato = 'STROGONOFF'
            preco = 18
        
        case 4:
            prato = 'BIFE ACEBOLADO'
            preco = 15
        
        case 5:
            prato = 'PÃO COM OVO'
            preco = 5
        
        case _:
            print('Opção inválida. Tente novamente!')

    if pedido >= 1 and pedido <= 5:
        pratos.append(prato)
        precos.append(preco)

    deseja_continuar = True
    while True:
        resposta = (input("Deseja pedir mais algum prato? (S/N): ").strip().upper())
        if resposta == "S":
            break
        elif resposta == "N":
            deseja_continuar = False
            break
        else:
            print("Opção inválida. Tente novamente.")

    if not deseja_continuar:
        break

nome = input('Nome para retirada: ')

os.system('cls || clear')

if sum(precos) == 0:
    print('Nenhum prato foi pedido.')
else:
    print('=== PEDIDO ===')
    print(f'Nome para retirada: {nome}')
    for i in range(len(pratos)):
        print(f'{pratos[i]} ..... R${precos[i]:.2f}')
    print('---------------')
    valor_total = sum(precos)
    print(f'Valor total: R${valor_total:.2f}')
