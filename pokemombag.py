pokebola = 0
potion = 0
fruit = 0
outros = 0

while True:
    item = input("Digite '1' para pokebola, '2' para Poções, '3' para frutas ou '4' para outros: ")
    qnt = int(input("Digite a quantidade de itens a serem inseridos: "))
    print("-"*50)
    if item == '1':
        pokebola = pokebola + qnt
        print("Pokebolas: " + str(pokebola))
        print("Poções e derivados: " + str(potion))
        print("Frutas: " + str(fruit))
        print("Outros: " + str(outros))
        print("-"*50)
    elif item == '2':
        potion = potion + qnt
        print("Pokebolas: " + str(pokebola))
        print("Poções e derivados: " + str(potion))
        print("Frutas: " + str(fruit))
        print("Outros: " + str(outros))
        print("-"*50)
    elif item == '3':
        fruit = fruit + qnt
        print("Pokebolas: " + str(pokebola))
        print("Poções e derivados: " + str(potion))
        print("Frutas: " + str(fruit))
        print("Outros: " + str(outros))
        print("-"*50)
    elif item == '4':
        outros = outros + qnt
        print("Pokebolas: " + str(pokebola))
        print("Poções e derivados: " + str(potion))
        print("Frutas: " + str(fruit))
        print("Outros: " + str(outros))
        print("-"*50)
    else:
        continue
