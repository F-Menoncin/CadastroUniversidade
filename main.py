while True:
    #apresentando o menu inicial
  print("Bem vindo ao menu principal!")
  print("1. Estudantes")
  print("2. Professores")
  print("3. Disciplinas")
  print("4. Turmas")
  print("5. Matrículas")
  print("6. Sair")

  #recebendo a resposta do usuário (int para receber a variavel no formato numero ao invés de texto)
  try:
    opcao = int(input("Digite o número da opção desejada: "))
  except ValueError:
    opcao = -1
      #apresentando o segundo menu
  if opcao == 6:
      break
  elif  opcao == 1: 
      while True:
        print(f"MENU DE OPERAÇÕES - Opção {opcao}.")
        print("Seleciona uma ação para prosseguir: ")
        print("1. Incluir")
        print("2. Listar")
        print("3. Excluir")
        print("4. Alterar")
        print("5. Returnar ao menu principal")
        try:
          opcao_secundaria = int(input("Selecione uma das opções acima: "))
        except ValueError:
          opcao_secundaria = -1
        if  opcao_secundaria == 1 or opcao_secundaria == 2:
            print(f"Você selecionou a opção {opcao_secundaria}.")
        elif opcao_secundaria == 3 or opcao_secundaria == 4:
            print("EM DESENVOLVIMENTO")
        elif opcao_secundaria == 5:
           break
        else :
          print("Opção inválida!")
  elif 2 <= opcao < 6:
     print("EM DESENVOLVIMENTO")
  else:
     print("Opção inválida!")
print("Obrigado e volte sempre!")