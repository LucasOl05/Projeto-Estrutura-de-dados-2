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
    caso_melhor = np.sort(caso_medio)
    caso_pior = caso_melhor[::-1]
    return caso_medio, caso_melhor, caso_pior



def bubble_sort_array(arr):
    arr = list(arr)
    n = len(arr)
    comparisons = 0
    swaps = 0
    t0 = time.perf_counter()
    for i in range(n - 1):
        trocou = False
        for j in range(n - 1 - i):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                trocou = True
        if not trocou:
            break
    elapsed = time.perf_counter() - t0
    return arr, comparisons, swaps, elapsed


def selection_sort_array(arr):
    arr = list(arr)
    n = len(arr)
    comparisons = 0
    swaps = 0
    t0 = time.perf_counter()
    for i in range(n - 1):
        idx_min = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[idx_min]:
                idx_min = j
        if idx_min != i:
            arr[i], arr[idx_min] = arr[idx_min], arr[i]
            swaps += 1
    elapsed = time.perf_counter() - t0
    return arr, comparisons, swaps, elapsed


def insertion_sort_array(arr):
    arr = list(arr)
    n = len(arr)
    comparisons = 0
    swaps = 0
    t0 = time.perf_counter()
    for i in range(1, n):
        chave = arr[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if arr[j] > chave:
                arr[j + 1] = arr[j]
                swaps += 1
                j -= 1
            else:
                break
        arr[j + 1] = chave
    elapsed = time.perf_counter() - t0
    return arr, comparisons, swaps, elapsed


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
        self.head = None
        self._tail = None
        if iterable is not None:
            for v in iterable:
                self.append(v)

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self._tail = node
        else:
            self._tail.next = node
            self._tail = node

    def to_list(self):
        out = []
        node = self.head
        while node is not None:
            out.append(node.data)
            node = node.next
        return out

    def copy(self):
        return LinkedList(self.to_list())


def bubble_sort_ll(linked_list):
    ll = linked_list.copy()
    comparisons = 0
    swaps = 0
    t0 = time.perf_counter()
    if ll.head is None or ll.head.next is None:
        return ll, 0, 0, time.perf_counter() - t0

    trocou = True
    fim = None
    while trocou:
        trocou = False
        node = ll.head
        while node.next is not fim:
            comparisons += 1
            if node.data > node.next.data:
                node.data, node.next.data = node.next.data, node.data
                swaps += 1
                trocou = True
            node = node.next
        fim = node
    elapsed = time.perf_counter() - t0
    return ll, comparisons, swaps, elapsed


def selection_sort_ll(linked_list):
    ll = linked_list.copy()
    comparisons = 0
    swaps = 0
    t0 = time.perf_counter()
    node_i = ll.head
    while node_i is not None and node_i.next is not None:
        no_min = node_i
        node_j = node_i.next
        while node_j is not None:
            comparisons += 1
            if node_j.data < no_min.data:
                no_min = node_j
            node_j = node_j.next
        if no_min is not node_i:
            node_i.data, no_min.data = no_min.data, node_i.data
            swaps += 1
        node_i = node_i.next
    elapsed = time.perf_counter() - t0
    return ll, comparisons, swaps, elapsed


def insertion_sort_ll(linked_list):
    ll = linked_list.copy()
    comparisons = 0
    swaps = 0
    t0 = time.perf_counter()
    if ll.head is None or ll.head.next is None:
        return ll, 0, 0, time.perf_counter() - t0

    node_i = ll.head.next
    while node_i is not None:
        proximo = node_i.next
        chave = node_i.data

        cur = ll.head
        while cur is not node_i:
            comparisons += 1
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

    elapsed = time.perf_counter() - t0
    return ll, comparisons, swaps, elapsed


LL_SORTERS = {
    "Bubble": bubble_sort_ll,
    "Selection": selection_sort_ll,
    "Insertion": insertion_sort_ll,
}
