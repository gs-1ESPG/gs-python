import csv
import os

ARQUIVO = "estoque.csv"

# Função para inicializar o estoque
def inicializar_estoque():
    if not os.path.isfile(ARQUIVO):
        with open(ARQUIVO, 'w', newline='', encoding='utf-8') as f:
            escritor = csv.writer(f)
            escritor.writerow(["ID", "Nome", "Quantidade"])


# Carregar estoque do arquivo
def carregar_estoque():
    estoque = {}
    if os.path.isfile(ARQUIVO):
        with open(ARQUIVO, 'r', encoding='utf-8') as f:
            leitor = csv.DictReader(f)
            for linha in leitor:
                estoque[linha["ID"]] = {
                    "nome": linha["Nome"],
                    "quantidade": int(linha["Quantidade"])
                }
    return estoque


# Salvar estoque no arquivo
def salvar_estoque(estoque):
    with open(ARQUIVO, 'w', newline='', encoding='utf-8') as f:
        escritor = csv.writer(f)
        escritor.writerow(["ID", "Nome", "Quantidade"])
        for id_produto, dados in estoque.items():
            escritor.writerow([id_produto, dados["nome"], dados["quantidade"]])


# Mostrar o menu
def mostrar_menu():
    print("\n===== Sistema de Estoque SafePlace =====")
    print("1. Adicionar produto")
    print("2. Remover produto")
    print("3. Entrada no estoque")
    print("4. Saída do estoque")
    print("5. Listar produtos")
    print("6. Sair")


# Funções principais
def adicionar_produto(estoque):
    id_produto = input("ID do produto: ")
    if id_produto in estoque:
        print("Produto já cadastrado.")
        return

    nome = input("Nome do produto: ")
    try:
        quantidade = int(input("Quantidade inicial: "))
    except ValueError:
        print("Quantidade deve ser um número inteiro.")
        return

    estoque[id_produto] = {"nome": nome, "quantidade": quantidade}
    print("Produto adicionado com sucesso!")


def remover_produto(estoque):
    id_produto = input("ID do produto a remover: ")
    if id_produto in estoque:
        del estoque[id_produto]
        print("Produto removido.")
    else:
        print("Produto não encontrado.")


def entrada_estoque(estoque):
    id_produto = input("ID do produto: ")
    if id_produto in estoque:
        try:
            quantidade = int(input("Quantidade de entrada: "))
            estoque[id_produto]["quantidade"] += quantidade
            print("Entrada realizada.")
        except ValueError:
            print("Quantidade inválida.")
    else:
        print("Produto não encontrado.")


def saida_estoque(estoque):
    id_produto = input("ID do produto: ")
    if id_produto in estoque:
        try:
            quantidade = int(input("Quantidade de saída: "))
            if quantidade <= estoque[id_produto]["quantidade"]:
                estoque[id_produto]["quantidade"] -= quantidade
                print("Saída realizada.")
            else:
                print("Estoque insuficiente.")
        except ValueError:
            print("Quantidade inválida.")
    else:
        print("Produto não encontrado.")


def listar_produtos(estoque):
    if not estoque:
        print("Estoque vazio.")
    else:
        print("\n=== Lista de Produtos ===")
        print(f"{'ID':<10}{'Nome':<20}{'Quantidade':<10}")
        print("-" * 40)
        for id_produto, dados in estoque.items():
            print(f"{id_produto:<10}{dados['nome']:<20}{dados['quantidade']:<10}")


# Programa principal
def main():
    inicializar_estoque()
    estoque = carregar_estoque()

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_produto(estoque)
        elif opcao == "2":
            remover_produto(estoque)
        elif opcao == "3":
            entrada_estoque(estoque)
        elif opcao == "4":
            saida_estoque(estoque)
        elif opcao == "5":
            listar_produtos(estoque)
        elif opcao == "6":
            salvar_estoque(estoque)
            print("Estoque salvo. Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
