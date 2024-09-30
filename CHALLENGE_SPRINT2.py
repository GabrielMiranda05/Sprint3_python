lista_resultados = []


def embaralhar_lista(lista):
    tamanho = len(lista)
    for i in range(tamanho - 1, 0, -1):
        j = i % (i + 1)
        lista[i], lista[j] = lista[j], lista[i]
    return lista
 
def quiz():
    global lista_resultados 
    perguntas_embaralhadas = embaralhar_lista(perguntas)
    perguntas_corretas = 0
    score = 0
    

    for i in perguntas_embaralhadas[:5]: 
        print(f"Pergunta: {i['pergunta']}")
        for num, opcao in i['opções'].items():
            print(f"{num}: {opcao}")
        
        resposta_usuario = input("Escolha a sua resposta (1 a 4): ")

        while resposta_usuario not in ['1', '2', '3', '4']:
            print("Escolha inválida. Por favor, escolha um número de 1 a 4.")
            resposta_usuario = input("Escolha a sua resposta (1 a 4): ")

        resposta_usuario = int(resposta_usuario)

        if resposta_usuario == i['resposta']: 
            print("Resposta correta!\n")
            perguntas_corretas += 1
            score += 100
        else:
            resposta_correta = i['opções'][i['resposta']]
            print(f"Resposta incorreta. A resposta correta é: {resposta_correta}\n")
    
    print(f"Você acertou {perguntas_corretas} de 5 perguntas. Seu Score total foi de {score} pontos!")
    

    lista_resultados.append(score)

def main():
    while True:
        print("""
        =============================================================================================================================
        
        Bem-vindo ao Quiz do Racing Coders!\n    Você sabe tudo sobre Formula E? Responda as perguntas escolhendo o número correspondente à sua resposta!!.

        ===============================================================================================================================
        """)
        menu = int(input("Pressione as teclas \n 1 - Iniciar Quiz \n 2 - Ver Pontuações anteriores \n 3 - Sair\n"))

        if menu == 1:
            comeca_jogo = input("Deseja começar a jogar? (y/n)").lower()
            if comeca_jogo == "y":
                quiz()
                joga_de_novo = input("Deseja jogar novamente? (y/n): ").lower()
                if joga_de_novo == 'y':
                    quiz()
                else:
                    continue

        elif menu == 2:
            ver_ranking = input("Deseja visualizar suas pontuações anteriores? (y/n)").lower()
            if ver_ranking == 'y':
                if lista_resultados:
                    print(f"Suas pontuações anteriores foram: {sorted(lista_resultados, reverse=True)}") 
                    for i, score in enumerate(sorted(lista_resultados, reverse=True), 1):
                        print(f"{i}º - {score} pontos")
                        voltar_menu = input("Voltar ao menu? (y/n)").lower()
                        if voltar_menu == 'y':
                            continue
                else:
                    print("Ainda não há pontuações anteriores.")
            else:
                continue

        elif menu == 3:
            print("Muito obrigado! Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

perguntas = [
    {
        "pergunta": "Qual equipe tem mais títulos na Fórmula E?",
        "opções": {
            1: "DS Techeetah",
            2: "Audi Sport ABT Schaeffler",
            3: "Nissan e.dams",
            4: "Mercedes-EQ Formula E Team"
        },
        "resposta": 1
    },
    {
        "pergunta": "Quem é o atual campeão da Fórmula E na temporada 2023?",
        "opções": {
            1: "Stoffel Vandoorne",
            2: "Lucas di Grassi",
            3: "Robin Frijns",
            4: "Nyck de Vries"
        },
        "resposta": 4
    },
    {
        "pergunta": "Qual piloto possui o recorde de vitórias na Fórmula E?",
        "opções": {
            1: "Jean-Éric Vergne",
            2: "Lucas di Grassi",
            3: "Sebastien Buemi",
            4: "Sam Bird"
        },
        "resposta": 3
    },
    {
        "pergunta": "Qual cidade sediou a primeira corrida de Fórmula E na história?",
        "opções": {
            1: "Berlim",
            2: "Londres",
            3: "Pequim",
            4: "Nova York"
        },
        "resposta": 3
    },
    {
        "pergunta": "Qual é o fabricante de pneus exclusivo da Fórmula E?",
        "opções": {
            1: "Michelin",
            2: "Pirelli",
            3: "Bridgestone",
            4: "Goodyear"
        },
        "resposta": 1
    },
    {
        "pergunta": "Qual foi a primeira temporada da Fórmula E?",
        "opções": {
            1: "2012-2013",
            2: "2013-2014",
            3: "2014-2015",
            4: "2015-2016"
        },
        "resposta": 3
    },
    {
        "pergunta": "Qual o nome oficial do carro da Fórmula E utilizado na 5ª temporada?",
        "opções": {
            1: "Gen1",
            2: "Gen2",
            3: "Spark SRT_01E",
            4: "Gen3"
        },
        "resposta": 2
    },
    {
        "pergunta": "Qual piloto venceu o ePrix de Berlim em 2021?",
        "opções": {
            1: "Lucas di Grassi",
            2: "António Félix da Costa",
            3: "Stoffel Vandoorne",
            4: "Mitch Evans"
        },
        "resposta": 1
    },
    {
        "pergunta": "Qual equipe entrou na Fórmula E em 2020?",
        "opções": {
            1: "Jaguar Racing",
            2: "Mercedes-EQ Formula E Team",
            3: "Dragon Racing",
            4: "Mahindra Racing"
        },
        "resposta": 2
    },
    {
        "pergunta": "Qual é a duração de uma corrida da Fórmula E?",
        "opções": {
            1: "45 minutos + 1 volta",
            2: "30 minutos + 1 volta",
            3: "60 minutos",
            4: "90 minutos"
        },
        "resposta": 1
    },
    {
        "pergunta": "Quem foi o primeiro campeão da Fórmula E?",
        "opções": {
            1: "Nelson Piquet Jr.",
            2: "Sébastien Buemi",
            3: "Lucas di Grassi",
            4: "Jean-Éric Vergne"
        },
        "resposta": 1
    },
    {
        "pergunta": "Em qual cidade ocorre o ePrix de Mônaco?",
        "opções": {
            1: "Londres",
            2: "Roma",
            3: "Mônaco",
            4: "Berlim"
        },
        "resposta": 3
    },
    {
        "pergunta": "Quem é o maior rival de Lucas di Grassi na Fórmula E?",
        "opções": {
            1: "Sebastien Buemi",
            2: "Sam Bird",
            3: "António Félix da Costa",
            4: "Stoffel Vandoorne"
        },
        "resposta": 1
    },
    {
        "pergunta": "Qual é a capacidade máxima de energia permitida durante a corrida na Fórmula E?",
        "opções": {
            1: "50 kWh",
            2: "54 kWh",
            3: "28 kWh",
            4: "52 kWh"
        },
        "resposta": 4
    },
    {
        "pergunta": "Quem foi o primeiro piloto brasileiro a vencer uma corrida de Fórmula E?",
        "opções": {
            1: "Nelson Piquet Jr.",
            2: "Felipe Massa",
            3: "Lucas di Grassi",
            4: "Bruno Senna"
        },
        "resposta": 1
    },
    {
        "pergunta": "Em qual país aconteceu a primeira corrida de Fórmula E?",
        "opções": {
            1: "Alemanha",
            2: "China",
            3: "Brasil",
            4: "Itália"
        },
        "resposta": 2
    },
    {
        "pergunta": "Qual equipe se tornou campeã da temporada 2020-2021 da Fórmula E?",
        "opções": {
            1: "Mercedes-EQ Formula E Team",
            2: "Jaguar Racing",
            3: "DS Techeetah",
            4: "Mahindra Racing"
        },
        "resposta": 1
    },
    {
        "pergunta": "Quem foi o primeiro piloto a alcançar 10 vitórias na Fórmula E?",
        "opções": {
            1: "Jean-Éric Vergne",
            2: "Lucas di Grassi",
            3: "Sébastien Buemi",
            4: "Mitch Evans"
        },
        "resposta": 3
    },
    {
        "pergunta": "Qual é a característica única dos circuitos da Fórmula E?",
        "opções": {
            1: "São todos em ruas de cidades",
            2: "São feitos apenas em pistas de corrida",
            3: "Tem uma extensão mínima de 10 km",
            4: "Todos têm trechos de alta velocidade"
        },
        "resposta": 1
    },
    {
        "pergunta": "Qual é a distância mínima que um carro de Fórmula E pode percorrer antes de precisar reabastecer?",
        "opções": {
            1: "Não há reabastecimento, são totalmente elétricos",
            2: "150 km",
            3: "200 km",
            4: "100 km"
        },
        "resposta": 1
    }
]

main()
