usuarios={
    "Marta": {"idade":25,"cidade":"Palhoça", "profissão":"Engenheira"},
    "João": {"idade":30,"cidade":"Florianópolis", "profissão":"Disigner"},
    "Maria": {"idade":28,"cidade":"São Paulo", "profissão":"Analista"}
}
nome_busca= input("Digite o nome do Usúario para Buscar: ")
usuario=usuarios.get(nome_busca)
if usuario: 
    print(f"\nInformações de {nome_busca}")
    for chave, valor in usuario.items():
        print(f"{chave.capitalize()}:{valor}")
else: 
    print("Usúario não encontado") 
