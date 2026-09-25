import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

TAMANHOS = [500, 1000, 3000, 5000, 10000]
CENARIOS = ["melhor", "medio", "pior"]
ALGORITMOS = ["Bubble", "Selection", "Insertion"]
ESTRUTURAS = ["Array", "Lista Ligada"]


def gera_dados(size):
    caso_medio = np.random.randint(0, size * size, size=size)
    caso_melhor = np.sort(caso_medio).copy()
    caso_pior = caso_melhor[::-1].copy()
    return {"melhor": caso_melhor, "medio": caso_medio, "pior": caso_pior}



def bubble_sort_array(arr):
    arr = list(arr)
    n = len(arr)
    comps = swaps = 0
    t0 = time.perf_counter()
    for i in range(n - 1):
        trocou = False
        for j in range(n - 1 - i):
            comps += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                trocou = True
        if not trocou:
            break
    return comps, swaps, time.perf_counter() - t0


def selection_sort_array(arr):
    arr = list(arr)
    n = len(arr)
    comps = swaps = 0
    t0 = time.perf_counter()
    for i in range(n - 1):
        idx_min = i
        for j in range(i + 1, n):
            comps += 1
            if arr[j] < arr[idx_min]:
                idx_min = j
        if idx_min != i:
            arr[i], arr[idx_min] = arr[idx_min], arr[i]
            swaps += 1
    return comps, swaps, time.perf_counter() - t0


def insertion_sort_array(arr):
    arr = list(arr)
    n = len(arr)
    comps = swaps = 0
    t0 = time.perf_counter()
    for i in range(1, n):
        chave = arr[i]
        j = i - 1
        while j >= 0:
            comps += 1
            if arr[j] > chave:
                arr[j + 1] = arr[j]
                swaps += 1
                j -= 1
            else:
                break
        arr[j + 1] = chave
    return comps, swaps, time.perf_counter() - t0


ARRAY_SORTERS = {
    "Bubble": bubble_sort_array,
    "Selection": selection_sort_array,
    "Insertion": insertion_sort_array,
}




class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, iterable=None):
        self.head = self._tail = None
        if iterable:
            for v in iterable:
                self.append(v)

    def append(self, data):
        node = Node(data)
        if not self.head:
            self.head = self._tail = node
        else:
            self._tail.next = node
            self._tail = node

    def copy(self):
        ll = LinkedList()
        cur = self.head
        while cur:
            ll.append(cur.data)
            cur = cur.next
        return ll


def bubble_sort_ll(linked_list):
    ll = linked_list.copy()
    comps = swaps = 0
    t0 = time.perf_counter()
    if not ll.head or not ll.head.next:
        return comps, swaps, time.perf_counter() - t0

    trocou = True
    fim = None
    while trocou:
        trocou = False
        node = ll.head
        while node.next is not fim:
            comps += 1
            if node.data > node.next.data:
                node.data, node.next.data = node.next.data, node.data
                swaps += 1
                trocou = True
            node = node.next
        fim = node
    return comps, swaps, time.perf_counter() - t0





def selection_sort_ll(linked_list):
    ll = linked_list.copy()
    comps = swaps = 0
    t0 = time.perf_counter()
    node_i = ll.head
    while node_i and node_i.next:
        no_min = node_i
        node_j = node_i.next
        while node_j:
            comps += 1
            if node_j.data < no_min.data:
                no_min = node_j
            node_j = node_j.next
        if no_min is not node_i:
            node_i.data, no_min.data = no_min.data, node_i.data
            swaps += 1
        node_i = node_i.next
    return comps, swaps, time.perf_counter() - t0


def insertion_sort_ll(linked_list):
    ll = linked_list.copy()
    comps = swaps = 0
    t0 = time.perf_counter()
    if not ll.head or not ll.head.next:
        return comps, swaps, time.perf_counter() - t0

    node_i = ll.head.next
    while node_i:
        proximo = node_i.next
        chave = node_i.data

        cur = ll.head
        while cur is not node_i:
            comps += 1
            if cur.data > chave:
                break
            cur = cur.next

        if cur is not node_i:
            valor_pendente = chave
            w = cur
            while w is not node_i:
                antigo = w.data
                w.data = valor_pendente
                valor_pendente = antigo
                swaps += 1
                w = w.next
            node_i.data = valor_pendente
        node_i = proximo

    return comps, swaps, time.perf_counter() - t0


LL_SORTERS = {
    "Bubble": bubble_sort_ll,
    "Selection": selection_sort_ll,
    "Insertion": insertion_sort_ll,
}








def roda_benchmark(tamanhos=TAMANHOS):
    linhas = []
    for size in tamanhos:
        dados_por_cenario = gera_dados(size)

        for cenario, dados in dados_por_cenario.items():
            dados_lista = dados.tolist()
            ll_base = LinkedList(dados_lista)

            for nome_alg in ALGORITMOS:
                # Array
                comps, trocas, tempo = ARRAY_SORTERS[nome_alg](dados_lista)
                linhas.append({
                    "tamanho": size, "cenario": cenario, "algoritmo": nome_alg,
                    "estrutura": "Array", "tempo_s": tempo,
                    "comparacoes": comps, "trocas": trocas
                })

                # Lista Ligada
                comps, trocas, tempo = LL_SORTERS[nome_alg](ll_base)
                linhas.append({
                    "tamanho": size, "cenario": cenario, "algoritmo": nome_alg,
                    "estrutura": "Lista Ligada", "tempo_s": tempo,
                    "comparacoes": comps, "trocas": trocas
                })

    return pd.DataFrame(linhas)



def plota_barras(df, metrica, ylabel, arquivo_saida):
    tamanhos = sorted(df["tamanho"].unique())
    n_linhas = len(tamanhos)
    n_colunas = len(CENARIOS)

    fig, eixos = plt.subplots(n_linhas, n_colunas, figsize=(15, 3.5 * n_linhas), squeeze=False)
    largura = 0.35
    x = np.arange(len(ALGORITMOS))

    for i, tamanho in enumerate(tamanhos):
        for j, cenario in enumerate(CENARIOS):
            ax = eixos[i][j]
            sub = df[(df["tamanho"] == tamanho) & (df["cenario"] == cenario)]

            valores_array = [sub[(sub["algoritmo"] == a) & (sub["estrutura"] == "Array")][metrica].values[0] for a in ALGORITMOS]
            valores_ll = [sub[(sub["algoritmo"] == a) & (sub["estrutura"] == "Lista Ligada")][metrica].values[0] for a in ALGORITMOS]

            ax.bar(x - largura / 2, valores_array, largura, label="Array")
            ax.bar(x + largura / 2, valores_ll, largura, label="Lista Ligada")
            ax.set_xticks(x)
            ax.set_xticklabels(ALGORITMOS)
            ax.set_title(f"n={tamanho} | {cenario}")
            ax.set_ylabel(ylabel)
            
           
            ax.set_ylim(bottom=0)

            if i == 0 and j == 0:
                ax.legend()

    fig.suptitle(f"{ylabel} por Algoritmo, Cenário e Estrutura", fontsize=14)
    fig.tight_layout(rect=[0, 0, 1, 0.97])
    fig.savefig(arquivo_saida, dpi=150)
    plt.show()
    plt.close(fig)


def plota_linhas_tempo_medio(df, arquivo_saida):
    sub = df[df["cenario"] == "medio"]
    fig, ax = plt.subplots(figsize=(8, 6))

    estilos = {"Array": "-o", "Lista Ligada": "--s"}
    for estrutura in ESTRUTURAS:
        for alg in ALGORITMOS:
            dados_alg = sub[(sub["algoritmo"] == alg) & (sub["estrutura"] == estrutura)].sort_values("tamanho")
            ax.plot(dados_alg["tamanho"], dados_alg["tempo_s"], estilos[estrutura], label=f"{alg} ({estrutura})")

    ax.set_xlabel("Tamanho da entrada (n)")
    ax.set_ylabel("Tempo de execução (s)")
    ax.set_title("Caso médio: tamanho da entrada x tempo de execução")
    ax.legend()
    ax.grid(True, alpha=0.3)

    fig.tight_layout()
    fig.savefig(arquivo_saida, dpi=150)
    plt.show()  # Exibe no Colab
    plt.close(fig)



if __name__ == "__main__":
    df = roda_benchmark(TAMANHOS)

    plota_barras(df, "tempo_s", "Tempo de execução (s)", "grafico_tempo.png")
    plota_barras(df, "comparacoes", "Número de comparações", "grafico_comparacoes.png")
    plota_barras(df, "trocas", "Número de trocas", "grafico_trocas.png")
    plota_linhas_tempo_medio(df, "grafico_linha_tempo_medio.png")







