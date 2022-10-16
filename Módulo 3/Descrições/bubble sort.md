# O bubble sort
Agora que pode efetivamente fazer malabarismos com os elementos das listas, é tempo de aprender a ordená-los. Muitos algoritmos de ordenação foram inventados até agora, que diferem muito na velocidade, bem como na complexidade. Vamos mostrar-lhe um algoritmo muito simples, fácil de compreender, mas infelizmente também não muito eficiente. É utilizado muito raramente, e certamente não para listas grandes e extensas.

Digamos que uma lista pode ser ordenada de duas maneiras:

1. crescente (ou mais precisamente - não decrescente) - se em cada par de elementos adjacentes, o primeiro elemento não for maior do que o segundo; 
2. decrescente (ou mais precisamente - não crescente) - se em cada par de elementos adjacentes, o primeiro elemento não for inferior ao segundo.

Nas secções seguintes, ordenaremos a lista por ordem crescente, de modo a que os números sejam ordenados do mais pequeno para o maior.

Aqui está a lista:

8
10
6
2
4

Tentaremos usar a seguinte abordagem: tomaremos o primeiro e o segundo elementos e compará-los-emos; se determinarmos que estão na ordem errada (ou seja, o primeiro é maior que o segundo), trocá-los-emos; se a sua ordem for válida, não faremos nada. Um olhar sobre a nossa lista confirma esta última - os elementos 01 e 02 estão na ordem correta, como em 8 < 10.

Agora olhe para o segundo e o terceiro elementos. Estão nas posições erradas. Temos de os trocar:

8
6
10
2
4

Vamos mais longe, e olhemos para o terceiro e quarto elementos. Novamente, não é assim que deveria ser. Temos de os trocar:

8
6
2
10
4

Agora verificamos o quarto e o quinto elementos. Sim, eles também estão nas posições erradas. Outra troca ocorre:

8
6
2
4
10

A primeira passagem pela lista já está terminada. Ainda estamos longe de terminar o nosso trabalho, mas algo de curioso aconteceu entretanto. O maior elemento, 10, já foi para o final da lista. Note-se que este é o lugar desejado para ele. Todos os elementos restantes formam uma confusão pitoresca, mas este já está no lugar.

Agora, por um momento, tente imaginar a lista de uma forma ligeiramente diferente - nomeadamente, assim:

10
4
2
6
8

Olhe - 10 está no topo. Poderíamos dizer que flutuou do fundo para a superfície, tal como a bolha numa taça de champanhe. O método de classificação deriva o seu nome da mesma observação - chama-se um bubble sort (uma espécie de bolha).

Agora começamos com a segunda passagem através da lista. Olhamos para o primeiro e segundo elementos - é necessária uma troca:

6
8
2
4
10

Tempo para o segundo e terceiro elementos: temos de os trocar também:

6
2
8
4
10

Agora o terceiro e quarto elementos, e a segunda passagem está terminada, visto 8 já estar no lugar:

6
2
4
8
10

Começamos a próxima passagem imediatamente. Observe cuidadosamente o primeiro e o segundo elementos - é necessária outra troca:

2
6
4
8
10

Agora 6 precisa de ser posto no lugar. Trocamos o segundo e o terceiro elementos:

2
4
6
8
10

A lista já está ordenada. Não temos mais nada a fazer. Isto é exatamente o que queremos.

Como pode ver, a essência deste algoritmo é simples: comparamos os elementos adjacentes e, trocando alguns deles, atingimos o nosso objetivo

Vamos codificar em Python todas as ações realizadas durante uma única passagem através da lista, e depois vamos considerar quantas passagens realmente precisamos para a realizar. Ainda não explicámos isto até agora, e faremos isso um pouco mais tarde.

