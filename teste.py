import time
import os

lista_telefonica = {}
lista_telefonica_ordem = {}
lista_de_afazeres = {}
lista_de_compromissos = {}
count = 0


def escolhaagenda():
    print("Para acessar a lista telefônica digite 1!")
    print("Para acessar a lista de afazeres digite 2!")
    print("Para acessar a lista de compromissos digite 3!")
    print("Para sair do programa digite 0!")


def incluir(nome, telefone):
    lista_telefonica[nome] = telefone
    lista_telefonica_ordem[nome] = telefone
    sucesso = "\nO contato foi armazenado com sucesso!!"
    return sucesso


def excluir(nome):
    if nome in lista_telefonica:
        lista_telefonica.pop(nome)
        return "\nO contato foi excluído com sucesso!!"
    else:
        return "\nO contato informado não foi encontrado!!"


def pesquisar(nome):
    if len(lista_telefonica) > 0:
        if nome in lista_telefonica:
            print("\nO contato de", nome, "é:")
            return lista_telefonica[nome]
        else:
            return "\nO contato informado não foi encontrado!!"
    else:
        print("\nA lista telefônica ainda não possui nenhum contato salvo!")


def pesquisar_tel(telefone):
    if len(lista_telefonica) > 0:
        for nome, telefone_salvo in lista_telefonica.items():
            if telefone == telefone_salvo:
                return f"\nO contato referente ao telefone {telefone} é: {nome} - {telefone_salvo}"
        return "\nO telefone informado não está relacionado a nenhum contato!"
    else:
        return "\nA lista telefônica ainda não possui nenhum contato salvo!"


def todas():
    if len(lista_telefonica) > 0:
        print("\nContatos salvos na lista telefônica:")
        for nome in lista_telefonica:
            print(f"{nome}: {lista_telefonica[nome]}")
    else:
        print("\nA lista telefônica ainda não possui nenhum contato salvo!")


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def todasordenadas():
    if len(lista_telefonica) > 0:
        print("\nContatos salvos na lista telefônica:")
        for nome in sorted(lista_telefonica.keys()):
            return (f"{nome}: {lista_telefonica[nome]}")
    else:
        return ("\nA lista telefônica ainda não possui nenhum contato salvo!")


def perguntas():
    print("\nPara incluir um contato na lista digite 1! ")
    print("Para excluir um contato na lista digite 2! ")
    print("Para pesquisar um contato na lista digite 3! ")
    print("Para pesquisar um telefone na lista digite 4! ")
    print("Para visualizar todos os contatos armazenados na lista digite 5!")
    print("Para visualizar a ordem em que os contatos foram armazenados digite 6!")
    print("Para voltar ao menu principal digite 7!")


def ordem_cadastro():
    if len(lista_telefonica) > 0:
        print("A ordem em que os contatos foram salvos é:")
        for c in range(1, len(lista_telefonica)):
            print(f"{c}:{lista_telefonica_ordem[nome]}")
    else:
        print("\nA lista telefônica ainda não possui nenhum contato salvo!")


if __name__ == '__main__':

    while True:
        escolhaagenda()
        escolha = int(input("\nDigite o número correspondente à função da agenda a ser acessada:"))
        limpar_tela()
        os.system('cls')

        if escolha == 0:
            print("Saindo da agenda...")
            time.sleep(1.5)
            break

        elif escolha == 1 or escolha == 2 or escolha == 3:
            while True:
                perguntas()
                operacao = int(input("\nDigite o número correspondente à operação que deseja fazer:"))
                limpar_tela()

                if operacao == 1:
                    if count == 0:
                        while True:
                            ordem = input(
                                "\nDeseja que os contatos sejam armazenados em ordem alfabética? (Sim/Não): ").lower()

                            if ordem == "sim":
                                break
                            elif ordem == "não" or ordem == "nao":
                                break
                            else:
                                print("Opção inválida! Por favor, responda com 'Sim' ou 'Não'.")

                        count += 1

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

                elif operacao == 4:
                    if len(lista_telefonica) > 0:
                        telefonebusca = input("Digite o número de telefone:")
                        print(pesquisar_tel(telefonebusca))
                    else:
                        print("A lista telefônica não possui nenhum contato salvo!")

                elif operacao == 5:
                    if len(lista_telefonica) > 0:
                        if ordem == "sim":
                            todasordenadas()

                        if ordem == "não" or ordem == "nao":
                            todas()

                    else:
                        print("\nA lista telefônica ainda não possui nenhum contato salvo!")

                elif operacao == 6:
                    if len(lista_telefonica) > 0:
                        ordem_cadastro()

                elif operacao == 7:
                    print("Salvando as informações da lista...")
                    time.sleep(3)
                    print("Informações salvas com sucesso!")
                    time.sleep(1.25)
                    print("Voltando para o menu principal...\n")
                    time.sleep(3)
                    break
        else:
            print("\nOperação inválida! Por favor, escolha uma opção válida (0, 1, 2 ou 3).\n")
