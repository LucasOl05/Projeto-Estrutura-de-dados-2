# Análise de Eficiência de Algoritmos de Ordenação

Trabalho da disciplina de **Estrutura de Dados 2**.

## Objetivo

Comparar o desempenho (tempo de execução, número de comparações e número de trocas) dos algoritmos de ordenação **Bubble Sort**, **Selection Sort** e **Insertion Sort**, implementados sobre duas estruturas de dados diferentes:

- **Array** (lista do Python)
- **Lista Ligada** (implementação própria, com `Node` e `LinkedList`)

## Cenários testados

Para cada algoritmo e estrutura, os testes são executados em três cenários distintos:

- **Melhor caso**: dados já ordenados
- **Caso médio**: dados em ordem aleatória
- **Pior caso**: dados ordenados de forma decrescente (inversa)

Os testes são repetidos para diferentes tamanhos de entrada: `500, 1000, 3000, 5000, 10000` elementos.

## Métricas coletadas

Para cada execução são medidos:

- Tempo de execução (segundos)
- Número de comparações
- Número de trocas (swaps)

## Estrutura do código

- `gera_dados(size)`: gera os três cenários (melhor, médio, pior) para um dado tamanho de entrada.
- `bubble_sort_array`, `selection_sort_array`, `insertion_sort_array`: implementações dos algoritmos para arrays.
- `Node` e `LinkedList`: implementação de lista ligada simples.
- `bubble_sort_ll`, `selection_sort_ll`, `insertion_sort_ll`: implementações dos mesmos algoritmos adaptadas para lista ligada.
- `ARRAY_SORTERS` e `LL_SORTERS`: dicionários que mapeiam o nome do algoritmo à função correspondente, facilitando a automação dos testes.

## Como executar

Pré-requisitos:

```bash
pip install numpy pandas matplotlib
```

Executar o script:

```bash
python sorting_benchmark.py
```

## Tecnologias utilizadas

- Python 3
- NumPy
- Pandas
- Matplotlib
