import random

# Nome do jogo
NOME_DO_JOGO = "Adivinhe o Número Mágico!"

# Regras do jogo
REGRAS = [
    "Bem-vindo(a) ao " + NOME_DO_JOGO,
    "O objetivo é adivinhar o número mágico que o computador escolheu.",
    "O número mágico está entre 1 e 100.",
    "Você tem um máximo de 7 tentativas para acertar.",
    "A cada tentativa, o programa dirá se o número digitado é maior ou menor que o número mágico.",
    "Você ganhará pontos com base na tentativa em que acertar:",
    "  - 1ª tentativa: 100 pontos",
    "  - 2ª tentativa: 90 pontos",
    "  - 3ª tentativa: 80 pontos",
    "  - ... e assim por diante (diminuindo 10 pontos a cada tentativa).",
    "Boa sorte!"
]

# Número máximo de tentativas
MAX_TENTATIVAS = 7
MIN_NUMERO = 1
MAX_NUMERO = 100

ranking = {}

# Exibir regras
for regra in REGRAS:
    print(regra)
    

# Loop principal do jogo
while True:
    numero_magico = random.randint(MIN_NUMERO, MAX_NUMERO)
    nome_jogador = input("Digite seu nome: ")
    tentativa_atual = 0
    pontuacao = 0

    print(f"\nOk, {nome_jogador}! O número mágico foi escolhido. Boa sorte!")

    while tentativa_atual < MAX_TENTATIVAS:
        numero_digitado = input(f"Tentativa {tentativa_atual + 1}/{MAX_TENTATIVAS}: Digite um número: ")
        
        if not numero_digitado.isdigit():
            print("Entrada inválida! Por favor, digite um número inteiro.")
            continue

        numero_digitado = int(numero_digitado)

        if numero_digitado < MIN_NUMERO or numero_digitado > MAX_NUMERO:
            print(f"Por favor, digite um número entre {MIN_NUMERO} e {MAX_NUMERO}.")
            continue

        tentativa_atual += 1

        if numero_digitado == numero_magico:
            pontuacao = 100 - (tentativa_atual - 1) * 10
            print(f"\nParabéns, {nome_jogador}! Você acertou o número mágico ({numero_magico}) em {tentativa_atual} tentativas!")
            print(f"Sua pontuação nesta rodada é: {pontuacao} pontos.")
            ranking[nome_jogador] = ranking.get(nome_jogador, 0) + pontuacao
            break
        elif numero_digitado < numero_magico:
            print("O número que você digitou é menor que o número mágico.")
        else:
            print("O número que você digitou é maior que o número mágico.")

    else:
        print(f"\nSuas {MAX_TENTATIVAS} tentativas acabaram, {nome_jogador}. O número mágico era {numero_magico}.")
        print("Sua pontuação nesta rodada é: 0 pontos.")
        ranking[nome_jogador] = ranking.get(nome_jogador, 0)

    # Exibe ranking
    print("\n----- Ranking Atual -----")
    if ranking:
        
        # Criando uma lista de chaves ordenadas pela pontuação
        chaves_ordenadas = []
        for chave in ranking:
            inserido = False
            for i in range(len(chaves_ordenadas)):
                if ranking[chave] > chaves_ordenadas[i][0]:  # Correção aqui
                    chaves_ordenadas.insert(i, (ranking[chave], chave))
                    inserido = True
                    break
            if not inserido:
                chaves_ordenadas.append((ranking[chave], chave))

        # Exibe o ranking ordenado
        posicao = 1
        for pontos, jogador in chaves_ordenadas:
            print(f"{posicao}. {jogador}: {pontos} pontos")
            posicao += 1
    else:
        print("Ainda não há jogadores no ranking.")
    # Pergunta se quer jogar novamente
    jogar_novamente = input("\nDeseja jogar novamente? (sim/não): ").lower()
    if jogar_novamente == "s" or jogar_novamente == "sim":
        print("\nObrigado por continuar jogando!")
    else:
        print("\nObrigado por jogar o Adivinhe o Número Mágico! Até a próxima!")
        break