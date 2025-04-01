#apresentando o menu inicial
print("Bem vindo ao menu!")
print("1. Estudantes")
print("2. Professores")
print("3. Disciplinas")
print("4. Turmas")
print("5. Matrículas")
print("6. Sair")

#recebendo a resposta do usuário (int para receber a variavel no formato numero ao invés de texto)
opcao = int(input("Digite o número da opção desejada: "))

  #apresentando o segundo menu
if opcao == 6 :
      print("Obrigado e volte sempre!")
elif 1 <= opcao < 6:
    print(f"MENU DE OPERAÇÕES - Opção {opcao}.")
    print("Seleciona uma ação para prosseguir: ")
    print("1. Incluir")
    print("2. Listar")
    print("3. Excluir")
    print("4. Alterar")
    print("5. Returnar ao menu inicial")
    opcao_secundaria = int(input("Selecione uma das opções acima: "))
    if 1 <= opcao_secundaria < 5 :
        print(f"Você selecionou a opção {opcao_secundaria}.")
    else :
        print("Opção inválida!")
else:
  print("Opção inválida!")