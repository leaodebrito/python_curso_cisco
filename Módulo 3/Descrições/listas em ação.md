# Listas em ação
Deixemos as listas de lado por um breve momento e vejamos uma questão intrigante.

Imagine que precisa de reorganizar os elementos de uma lista, ou seja, inverter a ordem dos elementos: o primeiro e o quinto, bem como o segundo e o quarto elementos serão trocados. O terceiro permanecerá intocado.


Pergunta: como se pode trocar os valores de duas variáveis?

Veja o snippet:

```
variable_1 = 1
variable_2 = 2

variable_2 = variable_1
variable_1 = variable_2
```

Se fizer algo como isto, perderá o valor previamente armazenado em variable_2. Alterar a ordem das atribuições não ajudará. É necessária uma terceira variável que sirva como armazenamento auxiliar.

É assim que se pode fazer:

```
variable_1 = 1
variable_2 = 2

auxiliary = variable_1
variable_1 = variable_2
variable_2 = auxiliary
```

O Python oferece uma forma mais conveniente de fazer a troca - veja:
```
variable_1 = 1
variable_2 = 2

variable_1, variable_2 = variable_2, variable_1
```

Claro, eficaz e elegante - não é?

Agora pode facilmente trocar os elementos da lista para inverter a sua ordem:
```
my_list = [10, 1, 8, 3, 5]

my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]

print(my_list)
```

Execute o snippet. O seu output deve ter este aspeto:

[5, 3, 8, 1, 10]



Fica bem com cinco elementos.


Será ainda aceitável com uma lista contendo 100 elementos? Não, não será.

Pode utilizar o loop for para fazer a mesma coisa automaticamente, independentemente do comprimento da lista? Sim, pode.

Foi assim que o fizemos:
```
my_list = [10, 1, 8, 3, 5]
length = len(my_list)

for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print(my_list)
```

**Nota:**

_nós atribuímos a variável length com o comprimento da lista atual (isto torna o nosso código um pouco mais claro e mais curto)
lançámos o loop for para correr através do seu corpo length // 2 vezes (isto funciona bem para listas com comprimentos pares e ímpares, porque quando a lista contém um número ímpar de elementos, o do meio permanece intocado)
trocamos o i-ésimo elemento (desde o início da lista) com o que tem um index igual a (length - i - 1) (do final da lista); no nosso exemplo, para i igual a 0 o ramo (lenght - i - 1) dá 4; para i igual a 1, dá 3 - Isto é exatamente o que precisávamos.
As listas são extremamente úteis, e irá encontrá-las com muita frequência._



## Desafio 
Objetivos
Familiarizar o aluno a:

a criação e modificação de listas simples;
utilizar métodos para modificar listas.
Cenário
Os Beatles foram um dos grupos musicais mais populares dos anos 1960, e a banda mais best-seller da história. Algumas pessoas consideram-nas o ato mais influente da era do rock. De facto, foram incluídos na compilação da revista Time das 100 pessoas mais influentes do século XX.

A banda passou por muitas mudanças de formação, culminando em 1962 com o line-up de John Lennon, Paul McCartney, George Harrison, e Richard Starkey (mais conhecido como Ringo Starr).


Escreva um programa que reflita estas mudanças e lhe permita praticar com o conceito de listas. A sua tarefa é:

passo 1: criar uma lista vazia com o nome beatles;

passo 2: utilizar o método append() para adicionar os seguintes membros da banda à lista: John Lennon, Paul McCartney, e George Harrison;

passo 3: utilizar o loop for e o método append() para solicitar ao utilizador que adicione os seguintes membros da banda à lista: Stu Sutcliffe, e Pete Best;

passo 4: utilizar a instrução del para remover Stu Sutcliffe e Pete Best da lista;

passo 5: utilizar o método insert() para adicionar Ringo Starr ao início da lista.