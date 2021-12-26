from collections import namedtuple

Player = namedtuple("Player", "name age rating")

player_Car = Player("Carlsen", 1990, 2842)
player_Caru = Player("Caruana", 1992, 2822)
player_Mamed = Player("Mamedyarov", 1985, 2801)

while True:

    # Menu
    print("1 - Carlsen \n"
          "2 - Caruana \n"
          "3 - Mamedyarov")

    escolha = input("Escolha um dos seguintes jogadores: ")

    if escolha == "1":
        print("1 - Nome \n"
              "2 - Ano \n"
              "3 - Pontos \n"
              "4 - Toda a informação")

        escolha_Car = input("Escolha o que deseja saber sobre o jogador: ")
        if escolha_Car == "1":
            print(player_Car.name)

        elif escolha_Car == "2":
            print(player_Car.age)

        elif escolha_Car == "3":
            print(player_Car.rating)

        elif escolha_Car == "4":
            print(player_Car)

        else:
            print("Ocorreu um erro!!")

    if escolha == "2":
        print("1 - Nome \n"
              "2 - Ano \n"
              "3 - Pontos \n"
              "4 - Toda a informação")

        escolha_Caru = input("Escolha o que deseja saber sobre o jogador: ")
        if escolha_Caru == "1":
            print(player_Caru.name)

        elif escolha_Caru == "2":
            print(player_Caru.age)

        elif escolha_Caru == "3":
            print(player_Caru.rating)

        elif escolha_Caru == "4":
            print(player_Caru)

        else:
            print("Ocorreu um erro!!")

    if escolha == "3":
        print("1 - Nome \n"
              "2 - Ano \n"
              "3 - Pontos \n"
              "4 - Toda a informação")

        escolha_Mamed = input("Escolha o que deseja saber sobre o jogador: ")
        if escolha_Mamed == "1":
            print(player_Mamed.name)

        elif escolha_Mamed == "2":
            print(player_Mamed.age)

        elif escolha_Mamed == "3":
            print(player_Mamed.rating)

        elif escolha_Mamed == "4":
            print(player_Mamed)

        else:
            print("Ocorreu um erro!!")

    escolha_exit = input("Deseja continuar? (s,n): ")

    if escolha_exit == "n":
        break
