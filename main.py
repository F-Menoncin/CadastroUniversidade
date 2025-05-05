# Felipe Menoncin - Análise e Desenvolvimento de Sistemas

lista_estudantes = []
lista_professores = []
lista_disciplinas = []
lista_turmas = []
lista_matriculas = []

mapeamento_geral = {
  1: {
      "lista": lista_estudantes,
      "tipo": "estudante",
      "campos": {
         "codigo": "cod_estudante",
         "nome": "nome_estudante",
         "cpf": "cpf_estudante"
      }
  },
  2: {
      "lista": lista_professores,
      "tipo": "professor",
      "campos": {
         "codigo": "cod_professor",
         "nome": "nome_professor",
         "cpf": "cpf_professor"
      }
  },
  3: {
      "lista": lista_disciplinas,
      "tipo": "disciplina",
      "campos": {
         "codigo": "cod_disciplina",
         "nome": "nome_disciplina"
      }
  },
  4: {
      "lista": lista_turmas,
      "tipo": "turma",
      "campos": {
         "codigo": "cod_turma",
         "professor": "professor_turma",
         "disciplina": "disc_turma" 
      }
  },
  5: {
      "lista": lista_matriculas,
      "tipo": "matrícula",
      "campos": {
         "codigo": "cod_matricula",
         "estudante": "estud_matricula",
      }
  },

}

#função do menu principal
def abrir_menu_principal():
  print("\nBem vindo ao menu principal!\n1. Estudantes\n2. Professores\n3. Disciplinas\n4. Turmas\n5. Matrículas\n6. Sair")

  #recebendo a resposta do usuário (int para receber a variavel no formato numero ao invés de texto)
  try:
    opcao = int(input("\nDigite o número da opção desejada: "))
  except ValueError:
    #setar o valor em -1 para que não caia em nenhum if e chegue até o else
    return -1
  return opcao

#função do menu secundário
def abrir_menu_secundario():
  print("\n===== MENU DE OPERAÇÕES =====\n1. Incluir\n2. Listar\n3. Excluir\n4. Alterar\n5. Retornar ao menu principal\n")
    #try para não receber um valor inválido e dar erro (usar o except)
  try:
    opcao_secundaria = int(input("Selecione uma das opções acima: "))
  except ValueError:
    opcao_secundaria = -1
  return opcao_secundaria

#função para incluir estudante, professor ou disciplina pois não dependem de outras listas para serem incluídas
def incluir_estudante_professor_ou_disciplina():
   while True:
      if opcao == 1:
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
      elif opcao == 2:
        print("\nVocê selecionou a opção de incluir um professor!")
        professor = input('\nDigite o nome que deseja incluir ou a palavra "sair": ')
        if professor == "sair":
          break
        else:
          try:
            codigo_professor = int(input('\nDigite o código do professor: '))
          except ValueError:
            print("O código digitado é inválido!")
            break
          cpf_professor = input('\nDigite o CPF do professor: ')
            #dicionário armazenando três variáveis sobre um estudante
          novo_professor = {
            "cod_professor" : codigo_professor,
            "nome_professor" : professor,
            "cpf_professor" : cpf_professor 
            }
          #append para que a lista possa ser flexível e tenha um número de entradas variável
          #adicionando o dicionário como uma entrada de uma lista 
          lista_professores.append(novo_professor)
          print("\nProfessor adicionado com sucesso!")
      elif opcao == 3:
        print("\nVocê selecionou a opção de incluir uma disciplina!")
        disciplina = input('\nDigite o nome da disciplina que deseja incluir ou a palavra "sair": ')
        if disciplina == "sair":
          break
        else:
          try:
            codigo_disc = int(input('\nDigite o código da disciplina: '))
          except ValueError:
            print("O código digitado é inválido!")
            break
          nova_disciplina = {
            "cod_disciplina" : codigo_disc,
            "nome_disciplina" : disciplina,
            }
          #append para que a lista possa ser flexível e tenha um número de entradas variável
          #adicionando o dicionário como uma entrada de uma lista 
          lista_disciplinas.append(nova_disciplina)
          print("\nDisciplina adicionada com sucesso!")
      else:
        break

#função para incluir turma
def incluir_turma():
      while True:
        print("\nVocê selecionou a opção de incluir uma turma!")
        try:
           codigo_turma = int(input('\nDigite o código da turma que deseja incluir ou o número "0" para sair: '))
        except ValueError:
           print("Código inválido!")
           break
        if codigo_turma == 0:
          break
        else:
          for turma in lista_turmas:
             if turma["cod_turma"] == codigo_turma:
                print("Código de turma já cadastrado!")
                return
          try:
              cod_prof_turma = int(input("\nDigite o código do professor da turma: "))
              encontrado = False
              for professor in lista_professores:
                if professor["cod_professor"] == cod_prof_turma:
                    prof_turma = professor["nome_professor"]
                    encontrado =  True
                    break
              if encontrado == False:                    
                print("Professor não encontrado!")
                break
          except ValueError:
            print("Erro: O código digitado é inválido.")

          try:
              cod_disc_turma = int(input("\nDigite o código da disciplina da turma: "))
              encontrado1 = False
              for disciplina in lista_disciplinas:
                if disciplina["cod_disciplina"] == cod_disc_turma:
                    disc_turma = disciplina["nome_disciplina"]
                    encontrado1 =  True
                    break
              if encontrado1 == False:                    
                print("Disciplina não encontrada!")
                break
          except ValueError:
            print("Erro: O código digitado é inválido.")
            #dicionário armazenando três variáveis sobre um estudante
          nova_turma = {
            "cod_turma" : codigo_turma,
            "professor_turma" : prof_turma,
            "disc_turma" : disc_turma 
            }
          #append para que a lista possa ser flexível e tenha um número de entradas variável
          #adicionando o dicionário como uma entrada de uma lista 
          lista_turmas.append(nova_turma)
          print("\nTurma adicionada com sucesso!")

#função para incluir matrícula
def incluir_matriculas():
   while True:
        print("\nVocê selecionou a opção de incluir uma matrícula!")
        try:
          codigo_matricula = int(input('\nDigite o código da turma em que o estudante será inserido ou o número "0" para sair: '))
          encontrado1 = False
          for turma in lista_turmas:
              if turma["cod_turma"] == codigo_matricula:
                encontrado1 =  True
          if encontrado1 == False or codigo_matricula == 0:                    
                print("Turma não encontrada!")
                break
        except ValueError:
           print("Código inválido!")
           break
        else:
          try:
              cod_matricula_estudante = int(input("\nDigite o código do estudante da turma: "))
              encontrado = False
              for estudante in lista_estudantes:
                if estudante["cod_estudante"] == cod_matricula_estudante:
                    matricula_estud = estudante["nome_estudante"]
                    encontrado =  True
                    break
              if encontrado == False:                    
                print("Estudante não encontrado!")
                break
          except ValueError:
            print("Erro: O código digitado é inválido.")

          #dicionário armazenando duas variáveis sobre uma matrícula
          nova_matricula = {
            "cod_matricula" : codigo_matricula,
            "estud_matricula" : matricula_estud, 
            }
          #append para que a lista possa ser flexível e tenha um número de entradas variável
          #adicionando o dicionário como uma entrada de uma lista 
          lista_turmas.append(nova_matricula)
          print("\nMatrícula adicionada com sucesso!")

#função para listar
def listar_registros():
    if opcao == 1:
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
    elif opcao == 2:
      #len(variavel) é uma forma de verificar se a lista esta vazia, pois se o comprimento dela (length) for zero, ela está vazia.
      print("\nVocê selecionou a opção de listar os professores cadastrados!")
      if len(lista_professores) == 0:
        print("\nNão há professores cadastrados!")
      else:
        print("\nAqui está a lista de professores: \n")
        #for para listar em linhas diferentes
        for professor in lista_professores:
          #percorre a lista e printa o nome, codigo e cpf de cada professor
          cod = professor["cod_professor"]
          nome = professor["nome_professor"]
          cpf = professor["cpf_professor"]
          print(f"Professor: {nome}, CPF: {cpf}, código: {cod}.")
    elif opcao == 3:
      print("\nVocê selecionou a opção de listar as disciplinas cadastradas!")
      if len(lista_disciplinas) == 0:
        print("\nNão há disciplinas cadastradas!")
      else:
        print("\nAqui está a lista de disciplinas: \n")
        #for para listar em linhas diferentes
        for disciplina in lista_disciplinas:
          #percorre a lista e printa o nome, codigo e cpf de cada professor
          cod = disciplina["cod_disciplina"]
          nome = disciplina["nome_disciplina"]
          print(f"Disciplina: {nome}, código: {cod}.")
    elif opcao == 4:
      print("\nVocê selecionou a opção de listar as turmas cadastradas!")
      if len(lista_turmas) == 0:
        print("\nNão há turmas cadastradas!")
      else:
        print("\nAqui está a lista de turmas: \n")
        #for para listar em linhas diferentes
        for turma in lista_turmas:
          #percorre a lista e printa o nome, codigo e cpf de cada professor
          cod = turma["cod_turma"]
          prof = turma["professor_turma"]
          disc = turma["disc_turma"]
          print(f"Código: {cod}, professor: {prof}, disciplina: {disc}.")      
    else:
      print("===========EM DESENVOLVIMENTO===============")

#função para excluir     
def excluir_registro():       
  dados = mapeamento_geral.get(opcao)
  if not dados: #Se não existir a opção
     print("Opção inválida!")
     return
  
  lista = dados["lista"]
  tipo = dados["tipo"]
  codigo_solicitado = dados["campos"]["codigo"]

  if len(lista) == 0:
    print(f"Não há {tipo}s cadastrados!")
    return
  
  print(f"\nVocê selecionou a opção de excluir um(a) {tipo}!")

  try:
     codigo = int(input(f"\nInsira o código do(a) {tipo} que deseja excluir: "))
  except ValueError:
     print("Código inválido!")
     return
  encontrado = False
  for item in lista:
    if item[codigo_solicitado] == codigo:
       lista.remove(item)
       print(f"{tipo.capitalize()} removido(a) com sucesso!")
       encontrado = True
       break
  if encontrado == False:
     print(f"{tipo.capitalize()} não encontrado(a)!")

#função para alterar
def alterar_registro():
  dados = mapeamento_geral.get(opcao)
  if not dados: #Se não existir a opção
     print("Opção inválida!")
     return
  
  lista = dados["lista"]
  tipo = dados["tipo"]
  campos = dados["campos"]

  if len(lista) == 0:
    print(f"Não há {tipo}s cadastrados!")
    return
  
  print(f"\nVocê selecionou a opção de alterar o cadastro de {tipo}!")

  try:
     codigo = int(input(f"\nInsira o código do(a) {tipo} que deseja alterar: "))
  except ValueError:
    print("Código inválido!")
    return
  
  encontrado = False
  for item in lista:
    if item[campos["codigo"]] == codigo:
        print("\nItens para alteração:")
        opcoes = {}
        i = 1
        for campo, nome_campo in campos.items():
           print(f"{i}. {campo.capitalize()}")
           opcoes[i] = campo
           i += 1

        try:
          opcao_alterar = int(input("\nSelecione uma opção para alterar: "))
        except ValueError:
          print("Opção inválida!")
          return
        
        if opcao_alterar in opcoes:
            campo_alterar = opcoes[opcao_alterar]
        
            #Verificação especial para código
            if campo_alterar == "codigo":
              try:
                  novo_valor = int(input("Digite o novo código: "))
              except ValueError:
                  print("Novo código inválido!")
                  return

            #Verificação se o novo professor está cadastrado antes de alterar na turma
            elif campo_alterar == "professor" and tipo == "turma":
              try:
                cod_professor = int(input("Digite o código do novo professor: "))
                professor_encontrado = False
                for professor in lista_professores:
                    if professor["cod_professor"] ==  cod_professor:
                      novo_valor = professor["nome_professor"]
                      professor_encontrado = True
                      break
                if professor_encontrado == False:
                  print("Professor não encontrado!")
                  return
              except ValueError:
                print("Código inválido!")
                return

            #Verificação se a nova disciplina está cadastrada antes de alterar na turma
            elif campo_alterar == "disciplina" and tipo == "turma":
              try:
                cod_disciplina = int(input("Digite o código da nova disciplina: "))
                disciplina_encontrada = False
                for disciplina in lista_disciplinas:
                    if disciplina["cod_disciplina"] ==  cod_disciplina:
                      novo_valor = disciplina["nome_disciplina"]
                      disciplina_encontrada = True
                      break
                if disciplina_encontrada == False:
                  print("Disciplina não encontrada!")
                  return
              except ValueError:
                print("Código inválido!")
                return

            #Verificação se a nova turma está cadastrada antes de alterar na matrícula 
            elif campo_alterar == "codigo" and tipo == "matricula":
              try:
                cod_turma = int(input("Digite o código da nova turma: "))
                turma_encontrada = False
                for turma in lista_turmas:
                    if turma["cod_turma"] ==  cod_turma:
                      novo_valor = turma["cod_turma"]
                      turma_encontrada = True
                      break
                if turma_encontrada == False:
                  print("Turma não encontrada!")
                  return
              except ValueError:
                print("Código inválido!")
                return


            #Verificação se o novo estudante está cadastrado antes de alterar na turma
            elif campo_alterar == "estudante" and tipo == "turma":
              try:
                cod_estudante = int(input("Digite o código do novo estudante: "))
                estudante_encontrado = False
                for estudante in lista_estudantes:
                    if estudante["cod_estudante"] == cod_estudante:
                      novo_valor = estudante["nome_estudante"]
                      estudante_encontrado = True
                      break
                if estudante_encontrado == False:
                  print("Estudante não encontrado!")
                  return
              except ValueError:
                print("Código inválido!")
                return
            else:
              novo_valor = input(f"Digite o novo {campo_alterar}: ")

            item[campos[campo_alterar]] = novo_valor
            print(f"{campo_alterar.capitalize()} alterado(a) com sucesso!")
            encontrado = True      

        else:
          print("Opção inválida!")

        break 
  if encontrado == False:
     print(f"{tipo.capitalize()} não encontrado(a)!")

#while True para que o loop seja infinito (tem que por um break no meio senão fica infinito) 
while True:
  #apresentando o menu inicial
  opcao = abrir_menu_principal()

    
  if opcao == 6:
    break
  #apresentando o segundo menu
  elif  1 <= opcao < 6:
      while True:
        opcao_secundaria = abrir_menu_secundario() 

        if  opcao_secundaria == 1:
          if 1 <= opcao <= 3:
            incluir_estudante_professor_ou_disciplina()  
          elif opcao == 4:
            incluir_turma()
          elif opcao == 5:
            incluir_matriculas()

        elif  opcao_secundaria == 2:
            listar_registros()
        
        elif opcao_secundaria == 3:
            excluir_registro()

        elif opcao_secundaria == 4:
            alterar_registro()

        elif opcao_secundaria == 5:
           break
        
        else :
          print("\nOpção inválida!\n")

  #elif 2 <= opcao < 6:
     #print("\n===== EM DESENVOLVIMENTO =====\n")
  else:
     print("Opção inválida! Digite um número de 1 a 6.")
print("\nObrigado e volte sempre!\n")