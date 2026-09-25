Respostas 1 a 6

1-) O selection sort é o algoritmo que deu maior numero de comparações e com forma mais consistente pois ele executa sempre seus 2 for até encontrar o menor numero independente da ordem inicial.

2-)o Bubble sort faz o maior numero de trocas sendo o 0(n2) no pior caso. 

3-) sim possui uma relação entre numero de trocas e eficiência de ordenação por causa do custo de escrita na memoria pois realizar uma comparação é uma operação rápida de leitura de cpu já uma troca ela envolve múltiplas operações escritas na memoria então em resumo as trocas custam mais que as comparações por isso o selection costuma ser mais rápido e o bubble costuma ser o mais lento por fazer varias trocas.

4-)O desempenho, à medida que o número de elementos aumenta faz com que o tempo cresça de forma quadrática se o tamanho da entrada quadruplica o tempo de execução aumenta 16 vezes seguindo a complexidade O(n²) O gráfico de linhas mostra que para o caso médio faz curvas bem acentuadas conforme o N passa de 500 para 10.000 mostrando o tempo de execução crescendo quadraticamente.Todos o 3 algoritmos operam com complexidade 0(1) pois tem apenas 1 quantidade fixa de variáveis auxiliar para contagem e troca.

5-) a ordenação previa altera bastante o comportamento dos métodos pois trás alguns benefícios como no caso do insertion sendo o mais beneficiado pois ele acaba fazendo apenas n-1 comparações e 0 trocas tendo complexidade linear 0(n) e executa quase instantaneamente . O Bubble com flag de otimização detecta que os dados já estão ordenados na primeira passagem, interrompendo o laço com O(n) comparações e 0 trocas.O Selection Sort é insensível às comparações porque o número de vezes que ele compara os elementos é sempre o mesmo, não importa se a lista já está ordenada ou fora de ordem. E quando acorre o pior caso quando a entrada esta invertida o insertion e o bubble sofrem o pior desempenho e faz com que eles tenham o limite máximo de movimentações e trocas sendo assim a ordenação pode mudar muito o desempenho dos métodos. 
