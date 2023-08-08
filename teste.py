import time

lista_telefonica = {}
lista_de_afazeres = {}
lista_de_compromissos = {}


def escolhaagenda():
    print("Para acessar a lista telefônica digite 1!")
    print("Para acessar a lista de afazeres digite 2!")
    print("Para acessar a lista de compromissos digite 3!")


def incluir(nome, telefone):
    lista_telefonica[nome] = telefone
    sucesso = "\nO contato foi armazenado com sucesso!!"
    return sucesso


def excluir(nome):
    if nome in lista_telefonica:
        lista_telefonica.pop(nome)
        return "O contato foi excluído com sucesso!!"
    else:
        return "O contato informado não foi encontrado!!"


def pesquisar(nome):
    if len(lista_telefonica) > 0:
        if nome in lista_telefonica:
            print("\nO contato de", nome, "é:")
            return lista_telefonica[nome]
        else:
            return "O contato informado não foi encontrado!!"
    else:
        print("\nA lista telefônica ainda não possui nenhum contato salvo!")


def todas():
    if len(lista_telefonica) > 0:
        print("\nContatos salvos na lista telefônica:")

        print(f"{nome}: {lista_telefonica[nome]}")
    else:
        print("\nA lista telefônica ainda não possui nenhum contato salvo!")


def todasordenadas():
    if len(lista_telefonica) > 0:
        print("\nContatos salvos na lista telefônica:")
        for nome in sorted(lista_telefonica.keys()):
            print(f"{nome}: {lista_telefonica[nome]}")
    else:
        print("\nA lista telefônica ainda não possui nenhum contato salvo!")


def perguntas():
    print("\nPara incluir um contato na lista digite 1! ")
    print("Para excluir um contato na lista digite 2! ")
    print("Para pesquisar um contato na lista digite 3! ")
    print("Para visualizar todos os contatos armazenados na lista digite 4!")
    print("Para voltar ao menu principal digite 5! ")


if __name__ == '__main__':
    while True:

        escolhaagenda()
        escolha = int(input("Digite o número correspondente à função da agenda a ser acessada:"))

        if escolha == 1 or escolha == 2 or escolha == 3 or escolha == 4:
            while True:
                perguntas()
                operacao = int(input("Digite o número correspondente à operação que deseja fazer:"))

                if operacao == 1:
                    ordem = input("Deseja que os contatos sejam armazenados em ordem alfabética?")
                    nome = input("\nDigite o nome do contato:")
                    telefone = input("Digite o telefone:")

                    print(incluir(nome, telefone))

                elif operacao == 2:
                    nome = input("\nDigite o nome do contato:")
                    print(excluir(nome))

                elif operacao == 3:
                    if len(lista_telefonica) > 0:
                        nome = input("\nDigite o nome do contato:")
                        print(pesquisar(nome))
                    else:
                        print("\nA lista telefônica ainda não possui nenhum contato salvo!")
                while True:
                    if operacao == 4:
                        if ordem == "Sim" or ordem == "SIM" or ordem == "sim":
                            todasordenadas()
                            break
                        elif ordem == "Nao" or ordem == "NAO" or ordem == "nao" or ordem == "Não" or ordem == "NÃO" or ordem == "não":
                            todas()
                            break
                        else:
                            print("Perdão,não conseguir entender")

            if operacao == 5:
                print("Salvando as informações da lista...")
            time.sleep(3)
            print("Voltando para o menu principal...\n")
            time.sleep(3)
            break

        else:
            print("Operação inválida! Por favor, escolha uma opção válida (1, 2, 3, 4 ou 5).")

else:
    print("Operação inválida! Por favor, escolha uma opção válida (1, 2, 3 ou 4).")
