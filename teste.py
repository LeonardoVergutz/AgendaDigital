lista_telefonica = {}


def incluir(nome, telefone):
    lista_telefonica[nome] = telefone
    sucesso = " \nO contato foi armazenado com sucesso!!"
    return sucesso


def excluir(nome):
    if nome in lista_telefonica:
        lista_telefonica.pop(nome)
        return "O contato foi excluído com sucesso!!"
    else:
        return "O contato informado não foi encontrado!!"


def pesquisar(nome):
    if nome in lista_telefonica:
        print("\nO contato de",nome,"é:")
        return lista_telefonica[nome]
    else:
        return "O contato informado não foi encontrado!!"


def perguntas():
    print("\nPara incluir um contato na lista digite 1 ")
    print("Para excluir um contato na lista digite 2 ")
    print("Para pesquisar um contato na lista digite 3 ")
    print("Para salvar as informações da lista digite 4 ")


if __name__ == '__main__':
    while True:
        perguntas()
        operacao = int(input("Digite o número correspondente à operação que deseja fazer:"))

        if operacao == 1:
            nome = input("\nDigite o nome do contato:")
            telefone = input("Digite o telefone:")

            print(incluir(nome, telefone))

        elif operacao == 2:
            nome = input("\nDigite o nome do contato:")
            print(excluir(nome))

        elif operacao == 3:
            nome = input("\nDigite o nome do contato:")
            print(pesquisar(nome))

        elif operacao == 4:
            print("Salvando as informações da lista...")
            break

        else:
            print("Operação inválida! Por favor, escolha uma opção válida (1, 2, 3 ou 4).")
