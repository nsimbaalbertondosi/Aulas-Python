pessoas = []
print("\n--- Cadastro de Pessoas ---")
while True:
    nome = input("Digite o nome (ou 'sair' para terminar): ")
    if nome.lower() == "sair":
        break
    idade = int(input("Digite a idade: "))
    pessoa = {
        "nome": nome,
        "idade": idade
    }
    pessoas.append(pessoa)
    print("Pessoa adicionada com sucesso!\n")
pessoas_ordenadas = sorted(
    pessoas,
    key=lambda p: (p["idade"], p["nome"])
)
print("\n--- Pessoas Ordenadas ---")
for pessoa in pessoas_ordenadas:
    print(pessoa)