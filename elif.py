c = str(input("Qual seu nome? ")) #pergunta o nome e atribui este valor a C
if c == "Kayk": #Caso o nome seja Kayk atribui uma função
    print("Olá senhor todo poderoso!") #Coloca na tela este texto

elif c == "Ana" or c == "Pedro" or c == "Paulo":
    print("Olá pessoa de nome comum!")

print("Olá {}!".format(c))