listadeafazeres = {}
listadetarefasconcluidas = []


def menulista_afazeres():
    print("\nPara incluir uma nova tarefa digite 1!")
    print("Para marcar uma tarefa como concluida digite 2!")
    print("Para remover uma tarefa digite 3!")
    print("Para ver todas as tarefas digite 4!")
    print("Para voltar ao menu principal digite 5!")


def incluir_afazer():
    while True:

        tarefa = input("\nDigite a tarefa a ser introduzida:")
        diatarefa = input("Digite o dia que essa tarefa devera ser realizada:")
        if tarefa in listadeafazeres:
            print("Essa tarefa ja foi introduzia na lista!")
        else:
            listadeafazeres[diatarefa] = tarefa
            break
    print("Tarefa armazenada com sucesso!")


def concluir_tarefa():
    palavra_chave = input("\nDigite uma palavra-chave para buscar a tarefa a ser marcada como concluída: ")
    tarefas_encontradas = []

    for dia, tarefa in listadeafazeres.items():
        if palavra_chave in tarefa:
            tarefas_encontradas.append((dia, tarefa))

    if not tarefas_encontradas:
        print("Nenhuma tarefa encontrada com essa palavra-chave.")
    else:
        print("Tarefas encontradas com a palavra-chave:")
        for i, (dia, tarefa) in enumerate(tarefas_encontradas):
            print(f"{i + 1}. Dia: {dia}, Tarefa: {tarefa}")

        escolha = int(input("Digite o número da tarefa que deseja concluir: "))

        if 0 < escolha <= len(tarefas_encontradas):
            dia, tarefa = tarefas_encontradas[escolha - 1]
            confirmacao = input(
                f"Você selecionou a seguinte tarefa para concluir: Dia: {dia}, Tarefa: {tarefa}. Confirmar (S/N)? ").strip().lower()

            if confirmacao == "s":
                listadetarefasconcluidas.extend(listadeafazeres[dia])
                print("Tarefa concluída com sucesso!")
            else:
                print("Operação cancelada.")
        else:
            print("Escolha inválida.")

def remocao_tarefa():
    palavra_chave = input("\nDigite uma palavra-chave para buscar a tarefa a ser marcada como concluída: ")
    tarefas_encontradas = []

    for dia, tarefa in listadeafazeres.items():
        if palavra_chave in tarefa:
            tarefas_encontradas.append((dia, tarefa))

    if not tarefas_encontradas:
        print("Nenhuma tarefa encontrada com essa palavra-chave.")
    else:
        print("Tarefas encontradas com a palavra-chave:")
        for i, (dia, tarefa) in enumerate(tarefas_encontradas):
            print(f"{i + 1}. Dia: {dia}, Tarefa: {tarefa}")

        escolha = int(input("Digite o número da tarefa que deseja concluir: "))

        if 0 < escolha <= len(tarefas_encontradas):
            dia, tarefa = tarefas_encontradas[escolha - 1]
            confirmacao = input(
                f"Você selecionou a seguinte tarefa para concluir: Dia: {dia}, Tarefa: {tarefa}. Confirmar (S/N)? ").strip().lower()

            if confirmacao == "s":
                del (listadeafazeres[dia])
                print("Tarefa concluída com sucesso!")
            else:
                print("Operação cancelada.")
        else:
            print("Escolha inválida.")


def visualizacao_tarefas():
    print("1 - Todas as tarefas")
    print("2 - Pendentes")
    print("3 - Concluídas")
    tipotarefa = int(input("Digite a opção desejada: "))

    if tipotarefa == 1:
        print("Todas as tarefas:")
        for dia, tarefa in listadeafazeres.items():
            print(f"Dia: {dia}, Tarefa: {tarefa}")
        for tarefa in listadetarefasconcluidas:
            print(f"Tarefa Concluída: {tarefa}")
    elif tipotarefa == 2:
        print("Tarefas Pendentes:")
        for dia, tarefa in listadeafazeres.items():
            print(f"Dia: {dia}, Tarefa: {tarefa}")
    elif tipotarefa == 3:
        print("Tarefas Concluídas:")
        for tarefa in listadetarefasconcluidas:
            print(f"Tarefa Concluída: {tarefa}")
    else:
        print("Opção inválida.")


def execucao_lista_de_afazeres():
    while True:
        menulista_afazeres()
        opcaomenu = int(input("\nDigite a funcao do menu a ser acessada:"))
        if opcaomenu == 1:
            incluir_afazer()
        elif opcaomenu == 2:
            concluir_tarefa()
        elif opcaomenu == 3:
            remocao_tarefa()
        elif opcaomenu == 5:
            break


if __name__ == '__main__':
    execucao_lista_de_afazeres()

