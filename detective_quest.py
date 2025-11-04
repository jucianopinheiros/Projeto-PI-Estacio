
# ================================================
# Detective Quest – Tema 4
# Estrutura de Dados — Algoritmos Avançados
# Autor: Francisco Juciano Pinheiro
#
# Objetivo:
# Simulação de investigação utilizando algoritmos avançados.
# Aqui, combinamos:
# ✅ Filtragem de dados
# ✅ Ordenação (algoritmo eficiente)
# ✅ Busca Binária
# ================================================

suspeitos = [
    {"id": 5, "nome": "Carlos", "idade": 32, "cidade": "Rio"},
    {"id": 1, "nome": "Ana", "idade": 25, "cidade": "São Paulo"},
    {"id": 3, "nome": "Bruno", "idade": 29, "cidade": "Curitiba"},
    {"id": 2, "nome": "Fernanda", "idade": 22, "cidade": "Recife"},
    {"id": 4, "nome": "Juliana", "idade": 27, "cidade": "Belo Horizonte"}
]

print("\n==============================")
print("🔎 Detective Quest: Investigação")
print("==============================\n")

print("📌 Pistas levantadas pelo detetive:")
print("- O suspeito tem entre 25 e 30 anos")
print("- Morador de cidade da região Sul ou Sudeste\n")

# Filtra suspeitos com base nas pistas
filtrados = [
    s for s in suspeitos
    if 25 <= s["idade"] <= 30 and s["cidade"] in ["Curitiba", "São Paulo", "Belo Horizonte"]
]

print(f"👥 Suspeitos após filtragem: {[s['nome'] for s in filtrados]}\n")

# Ordenação pelo algoritmo eficiente (Sort O(n log n))
filtrados.sort(key=lambda x: x["id"])

print("📊 Lista ordenada para busca binária:")
for s in filtrados:
    print(f"ID: {s['id']} - {s['nome']}")
print()

# Suspeito correto (com base nas pistas mais fortes)
id_procurado = 3

def busca_binaria(lista, alvo):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio]["id"] == alvo:
            return lista[meio]
        elif lista[meio]["id"] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1

    return None

print("🚨 Procurando suspeito principal...\n")
resultado = busca_binaria(filtrados, id_procurado)

if resultado:
    print("✅ SUSPEITO ENCONTRADO!")
    print(f"Nome: {resultado['nome']}")
    print(f"Idade: {resultado['idade']} anos")
    print(f"Cidade: {resultado['cidade']}")
else:
    print("❌ Nenhum suspeito atende a todas as pistas.")
