#Esse programa armazena o nome e a nota dos alunos de uma sala.

#Cores:
COR_VERDE = "\033[92m"
COR_AMARELO = "\033[93m"
COR_VERMELHA = "\033[91m"
COR_ROXA = "\033[95m"
RESET_COR = "\033[0m"


alunos = {}

while True:
    print(COR_AMARELO + "------------" + RESET_COR,"Menu",COR_AMARELO +"--------------" +RESET_COR)
    print("0. Sair")
    print("1. Adicionar Aluno. ")
    print("2. Exibir nota de um aluno. ")
    print("3. Exibir o nome e a nota de todos os alunos. ")
    print("4. Atualizar nota de um aluno.")
    print("5. Excluir Aluno.")
    print(COR_AMARELO+ 30*"-" + RESET_COR)
    print()
    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        nome = input("Digite o nome do aluno: ").capitalize()
        nota = float(input("Digite a nota do aluno: "))
        alunos[nome] = nota
        print(COR_VERDE+"Aluno adicionado com sucesso!"+RESET_COR)

    elif opcao == "2":
        nome = input("Digite o nome do aluno que deseja saber a nota: ").capitalize()
        if nome in alunos:
            print(f"A nota do aluno {nome} é {alunos[nome]}.")
        else:
            print(COR_VERMELHA+"Aluno não encontrado!"+RESET_COR)

    elif opcao == "3":
        if alunos:
            print("Alunos e suas notas:")
            for aluno, nota in alunos.items():
                print(COR_ROXA + f"{aluno}: {nota}"+RESET_COR)
        else:
            print(COR_VERMELHA+"Não há alunos cadastrados."+RESET_COR)

    elif opcao == "4":
        nome = input("Digite o nome do aluno para atualizar a nota: ").capitalize()
        if nome in alunos:
            nova_nota = float(input("Digite a nova nota: "))
            alunos[nome] = nova_nota
            print(COR_VERDE+"Nota atualizada com sucesso!"+RESET_COR)
        else:
            print(COR_VERMELHA+"Aluno não encontrado!"+RESET_COR)

    elif opcao == "5":
        nome = input("Digite o nome do aluno que deseja excluir: ").capitalize()
        if nome in alunos:
            del alunos[nome]
            print(COR_VERDE + f"O aluno {nome} foi removido com sucesso!" + RESET_COR)
        else:
            print(COR_VERMELHA + "Aluno não encontrado!" + RESET_COR)

    elif opcao == "0":
        print(COR_VERDE+"Encerrando o programa..."+RESET_COR)
        break


