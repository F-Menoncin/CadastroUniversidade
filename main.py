# Felipe Menoncin - Análise e Desenvolvimento de Sistemas

cadastro_estudantes = {}
lista_estudantes = []
#while True para que o loop seja infinito (tem que por um break no meio senão fica infinito) 
while True:
    #apresentando o menu inicial
  print("\nBem vindo ao menu principal!\n1. Estudantes\n2. Professores\n3. Disciplinas\n4. Turmas\n5. Matrículas\n6. Sair\n")

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
        print("\n===== MENU DE OPERAÇÕES =====\nMenu de Estudantes\n1. Incluir\n2. Listar\n3. Excluir\n4. Alterar\n5. Retornar ao menu principal\n")
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
                try:
                  codigo = int(input('\nDigite o código do estudante: '))
                except ValueError:
                   print("O código digitado é inválido!")
                   break
                cpf = input('\nDigite o CPF do estudante: ')
                #dicionário armazenando três variáveis sobre um estudante
                novo_estudante = {
                  "cod_estudante" : codigo,
                  "nome_estudante" : estudante,
                  "cpf_estudante" : cpf 
                }
                #append para que a lista possa ser flexível e tenha um número de entradas variável
                #adicionando o dicionário como uma entrada de uma lista 
                lista_estudantes.append(novo_estudante)
                print("\nEstudante adicionado com sucesso!")

        elif  opcao_secundaria == 2:
            #len(variavel) é uma forma de verificar se a lista esta vazia, pois se o comprimento dela (length) for zero, ela está vazia.
            print("\nVocê selecionou a opção de listar os estudantes cadastrados!")
            if len(lista_estudantes) == 0:
              print("\nNão há estudantes cadastrados!")
            else:
              print("\nAqui está a lista de estudantes: \n")
              #for para listar em linhas diferentes
              for estudante in lista_estudantes:
                #percorre a lista e printa o nome, codigo e cpf de cada estudante
                cod = estudante["cod_estudante"]
                nome = estudante["nome_estudante"]
                cpf = estudante["cpf_estudante"]
                print(f"Estudante: {nome}, CPF: {cpf}, código: {cod}.")

        elif opcao_secundaria == 3:
            if len(lista_estudantes) == 0:
                print("\nNão há estudantes cadastrados!")
                #print("\n===== EM DESENVOLVIMENTO =====")
            else:
              print("\nVocê selecionou a opção de excluir o cadastro de um estudante!")
              try:
                #print("\n===== EM DESENVOLVIMENTO =====")
                excluir_estudante = int(input("\nInsira o código do estudante que deseja excluir: "))
                encontrado = False

                for estudante in lista_estudantes:
                  if estudante["cod_estudante"] == excluir_estudante:
                      lista_estudantes.remove(estudante)
                      print("Estudante removido com sucesso!")
                      encontrado =  True
                      break
                if encontrado == False:
                    print("Estudante não encontrado!")
              except ValueError:
               print("Erro: O código digitado é inválido.")

        elif opcao_secundaria == 4:
            if len(lista_estudantes) == 0:
              print("\nNão há estudantes cadastrados!")
             #print("\n===== EM DESENVOLVIMENTO =====")
            else:
              print("\nVocê selecionou a opção de alterar o cadastro de um estudante!")
              try:
                alt_estudante = int(input("\nInsira o código do estudante que deseja alterar: "))
                encontrado = False

                for estudante in lista_estudantes:
                  if estudante["cod_estudante"] == alt_estudante:
                      print("\n1. Nome\n2. CPF\n3. Código")
                      try:
                        o_que_alterar = int(input("\nSelecione o que deseja alterar: "))
                      except ValueError:
                         print("Opção inválida")
                      if o_que_alterar == 1:
                          estudante["nome_estudante"] = input("Digite o novo nome: ")
                          encontrado =  True
                          print("Nome alterado com sucesso!")
                          break
                      elif o_que_alterar == 2:
                          estudante["cpf_estudante"] = input("Digite o novo CPF: ")
                          encontrado =  True
                          print("CPF alterado com sucesso!")
                          break
                      elif o_que_alterar == 3:
                          try:
                            estudante["cod_estudante"] = int(input("Digite o novo código: "))
                          except ValueError:
                             print("Valor inválido.")
                             break
                          encontrado =  True
                          print("Código alterado com sucesso!")
                          break
                      else:
                         print("Opção inválida.")
                      break
                if encontrado == False:
                      print("Estudante não encontrado!")
              except ValueError:
                print("Erro: O código digitado é inválido.") 


        elif opcao_secundaria == 5:
           break
        else :
          print("\nOpção inválida!\n")

  elif 2 <= opcao < 6:
     print("\n===== EM DESENVOLVIMENTO =====\n")
  else:
     print("Opção inválida!")
print("\nObrigado e volte sempre!\n")