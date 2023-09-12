import time
import os

# Dicionários para armazenar informações de contatos
lista_telefonica = {}  # Dicionário para armazenar contatos (nome: telefone)
lista_telefonica_ordem = {}  # Dicionário para informar ao usuário a ordem em que os contatos foram armazenados
lista_de_afazeres = {}  # Dicionário para armazenar afazeres da rotina (ainda não implementado)
lista_de_compromissos = {}  # Dicionário para armazenar compromissos (ainda não implementado)
count = 0  # Contador para controlar a criação de contatos com mesmo nome


# Função para exibir opções do menu
def escolhaagenda():
    print("Para acessar a lista telefônica digite 1!")
    print("Para acessar a lista de afazeres digite 2!")
    print("Para acessar a lista de compromissos digite 3!")
    print("Para sair do programa digite 0!\n")


# Função para adicionar contatos
def incluir(nome, telefone):
    # Verificação de duplicidade de contatos
    for nome_salvo, telefone_salvo in lista_telefonica.items():
        if nome == nome_salvo and telefone == telefone_salvo:
            return f"\nO contato com o nome {nome} e o mesmo telefone informado já estão armazenados na lista telefônica!"  # O número e o nome do contato já estão armazenados na lista.
        elif nome == nome_salvo:
            # Tratamento para contatos com mesmo nome
            while True:
                print(f"\nJá existe um contato com o nome {nome}. O que você deseja fazer?\n")
                perguntascontatorep()
                resposta = input("Digite o número correspondente a ação desejada:")

                # Opções para lidar com o contato existente
                if resposta == "1":
                    lista_telefonica[nome] = telefone
                    lista_telefonica_ordem[nome] = telefone
                    return "\nO número de telefone foi atualizado para o contato existente."
                elif resposta == "2":
                    lista_telefonica[f"{nome}2"] = telefone
                    lista_telefonica_ordem[f"{nome}_2"] = telefone
                    return f"\nNovo contato com o nome {nome}_2 criado com o número de telefone fornecido."
                elif resposta == "3":
                    print("\nAção cancelada. Voltando à página de seleção da lista...")
                    time.sleep(1.5)
                    return

                else:
                    print("Opção inválida. Por favor, escolha uma opção válida.")

    # Adiciona um novo contato à lista
    lista_telefonica[nome] = telefone
    lista_telefonica_ordem[nome] = telefone
    sucesso = "\nO contato foi armazenado com sucesso!!"
    return sucesso


# Função para apresentar opções ao usuário quando há contatos com mesmo nome
def perguntascontatorep():
    print("Para atualizar o número de telefone do contato existente digite 1!")
    print("Para criar um novo contato com o mesmo nome, mas com um número diferente digite 2!")
    print("Para cancelar a ação e voltar à página de seleção da lista digite 3!")


# Função para excluir um contato da lista telefônica
def excluir(nome):
    if nome in lista_telefonica:
        lista_telefonica.pop(nome)
        return "\nO contato foi excluído com sucesso!!"
    else:
        return "\nO contato informado não foi encontrado!!"


# Função para pesquisar e exibir o telefone de um contato
def pesquisar(nome):
    if len(lista_telefonica) > 0:
        if nome in lista_telefonica:
            print("\nO número de", nome, "é:")
            return lista_telefonica[nome]
        else:
            return "\nO contato informado não foi encontrado!!"
    else:
        print("\nA lista telefônica ainda não possui nenhum contato salvo!")


# Função para pesquisar e exibir o nome associado a um telefone
def pesquisar_tel(telefone):
    if len(lista_telefonica) > 0:
        for nome, telefone_salvo in lista_telefonica.items():
            if telefone == telefone_salvo:
                return f"\nO contato referente ao telefone {telefone} é: {nome} - {telefone_salvo}"
        return "\nO telefone informado não está relacionado a nenhum contato!"
    else:
        return "\nA lista telefônica ainda não possui nenhum contato salvo!"


# Função para exibir todos os contatos da lista telefônica
def todas():
    if len(lista_telefonica) > 0:
        print("\nContatos salvos na lista telefônica:\n")
        for nome in lista_telefonica:
            print(f"{nome}: {lista_telefonica[nome]}")


# Função para limpar a tela do terminal
def limpar_tela():
    os.system('cls')


# Função para exibir todos os contatos da lista telefônica em ordem alfabética
def todasordenadas():
    if len(lista_telefonica) > 0:
        print("\nContatos salvos na lista telefônica:\n")
        for nome in sorted(lista_telefonica.keys()):
            print(f"{nome}: {lista_telefonica[nome]}")


# Função para apresentar opções ao usuário no menu de operações
def perguntas():
    print("\nPara incluir um contato na lista digite 1! ")
    print("Para excluir um contato na lista digite 2! ")
    print("Para alterar um contato salvo digite 3!")
    print("Para pesquisar o telefone de um contato na lista digite 4!")
    print("Para pesquisar um telefone na lista digite 5!")
    print("Para visualizar todos os contatos armazenados na lista digite 6!")
    print("Para visualizar a ordem em que os contatos foram armazenados digite 7!")
    print("Para visualizar a quantiadade de contatos armazenados na lista digite 8!")
    print("Para voltar ao menu principal digite 9!")


# Função para exibir a ordem de cadastro dos contatos
def ordem_cadastro():
    if len(lista_telefonica) > 0:
        print("A ordem em que os contatos foram salvos é:")
        for c, nome in enumerate(lista_telefonica_ordem.keys(), start=1):
            print(f"{c}: {nome}")
    else:
        print("\nA lista telefônica ainda não possui nenhum contato salvo!")


# Função para exibir a quantidade de cadastros armazenados
def quantidadedecontatos():
    if len(lista_telefonica) == 0:
        return 0
    elif len(lista_telefonica) > 0:
        return len(lista_telefonica)


def alterarcontato():
    if len(lista_telefonica) > 0:
        nomealtera = input("Digite o nome do contato a ser alterado:")
        if nomealtera in lista_telefonica:
            novonome = input("Digite o novo nome do contato:")
            novotelefone = input("Digite o novo telefone do contato:")
            # Atualiza o contato com o novo nome e telefone
            lista_telefonica[novonome] = novotelefone
            # Remove o contato antigo se o nome for diferente do novo nome
            if nomealtera != novonome:
                del lista_telefonica[nomealtera]
            return f"Contato '{nomealtera}' foi alterado para '{novonome}' com o novo telefone '{novotelefone}'."
        else:
            return "O nome informado não está presente em nenhum contato salvo!"
    else:
        return "A lista telefônica ainda não possui nenhum contato salvo!"


# Programa principal
if __name__ == '__main__':

    while True:
        escolhaagenda()  # Exibe as opções do menu principal
        escolha = int(input("Digite o número correspondente à função da agenda a ser acessada:"))

        if escolha == 0:
            print("Saindo da agenda...")
            time.sleep(1.5)
            break

        elif escolha == 1 or escolha == 2 or escolha == 3:
            while True:
                perguntas()  # Exibe as opções do menu de operações da lista telefônica
                operacao = int(input("\nDigite o número correspondente à operação que deseja fazer:"))
                os.system('cls')  # Limpa a tela do terminal

                if operacao == 1:  # Adicionar contato
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

                    # Solicita informações do novo contato
                    nome = input("\nDigite o nome do contato:")
                    telefone = input("Digite o telefone:")
                    print(incluir(nome, telefone))

                elif operacao == 2:  # Excluir contato
                    nome = input("\nDigite o nome do contato:")
                    print(excluir(nome))  # Chama a função para excluir o contato

                elif operacao == 3:
                    nomealtera = input("Digite o nome do contato a ser alterado:")
                    if nomealtera in lista_telefonica:
                        novonome = input("Digite o nome do novo contato:")
                        novotelefone = input("Digite o telefone do novo contato:")
                        lista_telefonica[novonome] = novotelefone
                        if nomealtera != novonome:
                            del lista_telefonica[nomealtera]
                        print(f"Contato {nomealtera} foi alterado para {novonome} com o novo telefone {novotelefone}.")
                    else:
                        print("O nome informado não está presente em nenhum contato salvo!")
                elif operacao == 4:  # Pesquisar telefone por nome
                    if len(lista_telefonica) > 0:
                        nome = input("\nDigite o nome do contato:")
                        print(pesquisar(nome))  # Chama a função para pesquisar o telefone
                    else:
                        print("\nA lista telefônica ainda não possui nenhum contato salvo!")

                elif operacao == 5:  # Pesquisar nome por telefone
                    if len(lista_telefonica) > 0:
                        telefonebusca = input("Digite o número de telefone:")
                        print(pesquisar_tel(telefonebusca))  # Chama a função para pesquisar o nome
                    else:
                        print("A lista telefônica não possui nenhum contato salvo!")

                elif operacao == 6:  # Visualizar todos os contatos
                    if len(lista_telefonica) > 0:
                        if ordem == "sim":
                            todasordenadas()  # Chama a função para listar ordenadamente
                        if ordem == "não" or ordem == "nao":
                            todas()  # Chama a função para listar todos os contatos
                    else:
                        print("\nA lista telefônica ainda não possui nenhum contato salvo!")

                elif operacao == 7:  # Visualizar ordem de cadastro dos contatos
                    if len(lista_telefonica) > 0:
                        ordem_cadastro()  # Chama a função para mostrar a ordem de cadastro

                elif operacao == 8:  # Visualizar a quantidade de contatos armazenados
                    print("A quantidade de contatos armazenados é:", quantidadedecontatos())

                elif operacao == 9:  # Voltar ao menu principal
                    print("Salvando as informações da lista...")
                    time.sleep(3)
                    print("Informações salvas com sucesso!")
                    time.sleep(1.25)
                    print("Voltando para o menu principal...\n")
                    time.sleep(3)
                    break
        else:
            print("\nOperação inválida! Por favor, escolha uma opção válida (0, 1, 2 ou 3).\n")  # Fé
