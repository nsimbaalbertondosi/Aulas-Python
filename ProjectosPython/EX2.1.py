pessoas = [
    {"nome": "Ana", "idade": 30},
    {"nome": "Bruno", "idade": 25},
    {"nome": "Carla", "idade": 30},
    {"nome": "Daniel", "idade": 25},
    {"nome": "Eduardo", "idade": 35}
]
pessoas_ordenadas = sorted(
    pessoas,
    key=lambda p: (p["idade"], p["nome"])
)
print("\n--- Pessoas Ordenadas ---")
for pessoa in pessoas_ordenadas:
    print(pessoa)
