print("------lista de produtos------")

produtos_and_price = { "notebook": 3000, "celular": 1500, "tablet": 800, "fone de ouvido": 200, "smartwatch": 1000 }
for i, (produto, preco) in enumerate(produtos_and_price.items()):
    print(f"{i+1} - {produto} - R$ {preco:.2f}")

choise = int(input("Escolha um produto pelo número: "))

if choise < 1 or choise > len(produtos_and_price):
    print("Escolha inválida. Tente novamente.")
else:
    print(f"Você escolheu: {list(produtos_and_price.keys())[choise - 1]} o preço é R$ {list(produtos_and_price.values())[choise - 1]:.2f}")
    print("deseja adicionnar outro produto? (s/n)")
if input().lower() == "s":
    print("------lista de produtos------")
    for i, (produto, preco) in enumerate(produtos_and_price.items()):
        print(f"{i+1} - {produto} - R$ {preco:.2f}")
   
new_choise = int(input("Escolha outro produto pelo número: "))

if new_choise < 1 or new_choise > len(produtos_and_price):
    print("Escolha inválida. Tente novamente.")
    print(f"Você escolheu: {list(produtos_and_price.keys())[new_choise - 1]} o preço é R$ {list(produtos_and_price.values())[new_choise - 1]:.2f}")

    print("Deseja adicionar ao carrinho? (s/n)")
    add_to_cart = input().lower()
    if add_to_cart == "s":
        print(f"{list(produtos_and_price.keys())[choise - 1]} e {list(produtos_and_price.keys())[new_choise - 1]} adicionado ao carrinho.")
    
    print("Deseja confirmar a compra? (s/n)")
    confirm = input().lower()
    
    if confirm == "s":
        print("Obrigado pela compra!")
    else:
        print("Compra cancelada.")
