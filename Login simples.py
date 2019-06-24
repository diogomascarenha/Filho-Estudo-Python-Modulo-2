Usr = "ADMIN"
Pass = "Admin"
Reg = ""
Log = ""
Log2 = ""
Usri = ""
Passi = ""
print("-=-" *10)
print("Bem Vindo(a)")
print("-=-" *10)
regolog = str(input("Deseja logar ou se cadastrar? -[L/R]- ")).strip().upper()[0]
if regolog == "R":
    while Reg != "R":
        Reg = str(input("Você deseja cadastrar? -[S/N]- ")).strip().upper()[0]
        if Reg == "S":
            print("Você selecionou se cadastrar")
            Usr = str(input("Digite seu usuario: ")).strip().upper()
            Pass = str(input("Agora, digite sua senha: "))
            Reg = "R"
            print("Registrado(a) com sucesso")
        elif Reg == "N":
            print("Você selecionou não se cadastrar")
            Reg = "R"
        elif Reg != "S" or "N":
            print("Você selecionou uma opção invalida, por favor tente novamente!")
            Reg = str(input("Você deseja cadastrar? -[S/N]- ")).strip().upper()[0]
if Reg == "R":
    Log2 = str(input("Agora resgistrado(a) deseja logar? -[S/N]-")).strip().upper()[0]
    if Log2 == "S":
        Usri = str(input("Digite seu usuario: ")).strip().upper()
        Passi = str(input("Digite sua senha: "))
        if Usri != Usr or Passi != Pass:
            while Usri != Usr or Passi != Pass:
                print("Usuário ou senha invalidos, Tente novamente!")
                Usri = str(input("Digite seu usuario: ")).strip().upper()
                Passi = str(input("Digite sua senha: "))
        else:
            print("Logado com sucessor senhor(a) {}".format(Usri))
    else:
        print("Muito obrigado pela preferencia, volte sempre")
elif regolog == "L":
    Usri = str(input("Digite seu usuario: ")).strip().upper()
    Passi = str(input("Digite sua senha: "))
    if Usri != Usr or Passi != Pass:
        while Usri != Usr or Passi != Pass:
            print("Usuário ou senha invalidos, Tente novamente!")
            Usri = str(input("Digite seu usuario: ")).strip().upper()
            Passi = str(input("Digite sua senha: "))
    else:
        print("Logado com sucesso senhor(a) {}".format(Usri))
elif regolog != "R" or "L":
    print("Esta opção não é valida")