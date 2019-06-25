adminUsuario = "ADMIN"
adminSenha = "Admin"

usuario = ""
senha = ""

print("-=-" *10)
print("Bem Vindo(a)")
print("-=-" *10)

opcaoSelecionada = ""
while opcaoSelecionada != "S":
    opcaoSelecionada = str(input("Digite [L] para Logar, [R] para Registrar ou [S] para sair. ")).strip().upper()[0]

    if opcaoSelecionada == "R":
        print("Você selecionou a opção para se registrar")
        usuario = str(input("Digite seu usuario: ")).strip().upper()
        senha = str(input("Agora, digite sua senha: "))
        print("Registrado(a) com sucesso")
        continue

    if opcaoSelecionada == "L":
        print("Você selecionou a opção para se logar")
        usuarioDigitado = str(input("Digite seu usuario: ")).strip().upper()
        senhaDigitada = str(input("Digite sua senha: "))

        if usuarioDigitado == adminUsuario and senhaDigitada == adminSenha:
            print("Logado como administrador com sucesso senhor(a) {}".format(usuarioDigitado))
            continue

        if usuario == usuarioDigitado and senha == senhaDigitada:
            print("Logado com sucesso senhor(a) {}".format(usuarioDigitado))
            continue

        print("Usuário e/ou senha invalidos, tente novamente!")
        continue

    if opcaoSelecionada == "S":
        print("Você selecionou a opção para sair")
        continue

    print("Esta opção não é valida [{}], tente novamente!".format(opcaoSelecionada))
