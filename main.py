# Felipe Menoncin - Análise e Desenvolvimento de Sistemas

cadastro_estudantes = {}
lista_estudantes = []
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
              print("\nVocê selecionou a opção de incluir um estudante!")
              estudante = input('\nDigite o nome que deseja incluir ou a palavra "sair": ')
              if estudante == "sair":
                break
              else:
                codigo = int(input('\nDigite o código do estudante: '))
                cpf = input('\nDigite o CPF do estudante: ')
                novo_estudante = {
                  "cod_estudante" : codigo,
                  "nome_estudante" : estudante,
                  "cpf_estudante" : cpf 
                }
                #append para que a lista possa ser flexível e tenha um número de entradas variável
                #cadastro_estudantes.append(estudante) 
                lista_estudantes.append(novo_estudante)
                print("\nEstudante adicionado com sucesso!")
        elif  opcao_secundaria == 2:
            #len(variavel) é uma forma de verificar se a lista esta vazia, pois se o comprimento dela (length) for zero, ela está vazia.
            print("\nVocê selecionou a opção de listar os estudantes cadastrados!")
            if len(lista_estudantes) == 0:
              print("\nNão há estudantes cadastrados!\n")
            else:
              print("\nAqui está a lista de estudantes: \n")
              #for para listar em linhas diferentes
              for estudante in lista_estudantes:
                cod = estudante["cod_estudante"]
                nome = estudante["nome_estudante"]
                cpf = estudante["cpf_estudante"]
                print(f"Estudante: {nome}, CPF: {cpf}, código: {cod}.")
        elif opcao_secundaria == 3:
            print("\nVocê selecionou a opção de excluir o cadastro um estudante!\n")
            #print("\n===== EM DESENVOLVIMENTO =====")
            excluir_estudante = input("\nInsira o nome do estudante que deseja excluir: ")
            encontrado = False

            for estudante in lista_estudantes:
              if estudante["nome_estudante"] == excluir_estudante:
                  lista_estudantes.remove(estudante)
                  print("Estudante removido com sucesso!")
                  encontrado =  True
                  break
            if encontrado == False:
                  print("Estudante não encontrado!")
        elif opcao_secundaria == 4:
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