# Felipe Menoncin - Análise e Desenvolvimento de Sistemas

lista_nomes = []
#while True para que o loop seja infinito (tem que por um break no meio senão fica infinito) 
while True:
    #apresentando o menu inicial
  print("\nBem vindo ao menu principal!\n")
  print("1. Estudantes")
  print("2. Professores")
  print("3. Disciplinas")
  print("4. Turmas")
  print("5. Matrículas")
  print("6. Sair\n")

  #recebendo a resposta do usuário (int para receber a variavel no formato numero ao invés de texto)
  try:
    opcao = int(input("Digite o número da opção desejada: "))
  except ValueError:
    #setar o valor em -1 para que não caia em nenhum if e chegue até o else
    opcao = -1
      #apresentando o segundo menu
  if opcao == 6:
      break
  elif  opcao == 1: 
      while True:
        print("\n===== MENU DE OPERAÇÕES =====\n")
        print("Menu de Estudantes\n")
        print("1. Incluir")
        print("2. Listar")
        print("3. Excluir")
        print("4. Alterar")
        print("5. Retornar ao menu principal\n")
        #try para não receber um valor inválido e dar erro (usar o except)
        try:
          opcao_secundaria = int(input("Selecione uma das opções acima: "))
        except ValueError:
          opcao_secundaria = -1
        if  opcao_secundaria == 1:
          while True:
              nome = input('\nDigite o nome que deseja incluir ou a palavra "sair": ')
              if nome == "sair":
                break
              else:
                #append para que a lista possa ser flexível e tenha um número de entradas variável
                lista_nomes.append(nome) 
                print("\nEstudante adicionado com sucesso!")
        elif  opcao_secundaria == 2:
            #len(variavel) é uma forma de verificar se a lista esta vazia, pois se o comprimento dela (length) for zero, ela está vazia.
            if len(lista_nomes) == 0:
              print("\nNão há estudantes cadastrados!\n")
            else:
              print("\nAqui está a lista de estudantes: \n")
              #for para listar em linhas diferentes
              for nome in lista_nomes:
                print("- " + nome)
        elif opcao_secundaria == 3 or opcao_secundaria == 4:
            print("\n===== EM DESENVOLVIMENTO =====")
        elif opcao_secundaria == 5:
           break
        else :
          print("\nOpção inválida!\n")
  elif 2 <= opcao < 6:
     print("\n===== EM DESENVOLVIMENTO =====\n")
  else:
     print("Opção inválida!")
print("\nObrigado e volte sempre!\n")