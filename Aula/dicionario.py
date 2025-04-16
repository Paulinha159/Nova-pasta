# Criando um dicionário para armazenar as informações do usuário
usuario = {}
# coletando dados via entrada de usuario 
usuario["nome"]= input("Digite seu nome: ")
usuario["idade"]= input("Digite sua idade: ")
usuario["cidade"]= input("Digite sua cidade: ")
usuario["profissão"]= input("Digite sua profissão: ")

# Exibindo os dados formatados
print(f"\nInformações do usuário")
for chave, valor in usuario.items():
    print(f"{chave.capitalize()}:{valor}")