print("Maquina de conversão de inteiros")
n = int(input("Digite seu numero: "))
print("""Para converter, digite:
[1] = Hexadecimal
[2] = Binario
[3] = Octal """)
opcao = int(input("Opção: "))
if opcao == 1:
    print ("{} convertido em hex vale = {}".format(n, hex(n)[2:]))
elif opcao == 2:
    print ("{} convertido em bin vale = {}".format(n, bin(n)[2:]))
elif opcao == 3:
    print ("{} convertido em oct vale = {}".format(n, oct(n)[2:]))
else:
    print ("Opção invalida! Tente Novamente")