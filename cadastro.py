produto = {
    'codigo': 0,
    'descricao': "",
    'preco': 00.0,
    'qtde': 000
}

produto['codigo'] = int(input("Digite o código do produto: "))
produto['descricao'] = (input("Digite a descrição do produto: "))
produto['preco'] = float(input("Digite o preço do produto: "))
produto['qtde'] = float(input("Digite a quantidade em estoque do produto: "))

print("Código: ", produto['codigo'])
print("Descrição: ", produto['descricao'])
print("Preço: ", produto['preco'])
print("Quantidade estoque: ", produto['qtde'])