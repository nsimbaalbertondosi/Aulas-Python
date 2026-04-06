def permutar(lista):
    if len(lista) == 0:
        yield []
    elif len(lista) == 1:
        yield lista
    else:
        for i in range(len(lista)):
            elemento_atual = lista[i]
            elementos_restantes = lista[:i] + lista[i + 1:]

            for p in permutar(elementos_restantes):
                yield [elemento_atual] + p
print("\n--- Gerador de Permutações ---")
lista_exemplo = [1, 2, 3]
print(f"Permutações de {lista_exemplo}:")
for p in permutar(lista_exemplo):
    print(p)
lista_letras = ["A", "B"]
print(f"\nPermutações de {lista_letras}:")
for p in permutar(lista_letras):
    print(p)
