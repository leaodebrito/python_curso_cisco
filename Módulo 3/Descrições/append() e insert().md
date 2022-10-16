# Adicionar elementos a uma lista: append() e insert()

Um novo elemento pode ser colado no fim da lista existente:

```
list.append(value)
```

Tal operação é realizada por um método chamado append(). Toma o valor do seu argumento e coloca-o no final da lista que possui o método.

O comprimento da lista aumenta então em um.

O método insert() é um pouco mais inteligente - pode acrescentar um novo elemento em qualquer lugar da lista, e não apenas no final.

```
list.insert(location, value)
```

São necessários dois argumentos:

1. o primeiro mostra a localização necessária do elemento a ser inserido; nota: todos os elementos existentes que ocupam locais à direita do novo elemento (incluindo o que se encontra na posição indicada) são deslocados para a direita, a fim de criar espaço para o novo elemento; 
2. o segundo é o elemento a ser inserido.

Veja o código no editor. Veja como utilizamos os append() e insert() métodos. Preste atenção ao que acontece após a utilização insert(): o primeiro elemento é agora o segundo, o segundo o terceiro, e assim por diante.
Adicione o seguinte snippet após a última linha de código no editor:

```
numbers.insert(1, 333)
```

Imprima o conteúdo da lista final para o ecrã e veja o que acontece. O snippet acima do snippet insere 333 na lista, tornando-o no segundo elemento. O anterior segundo elemento torna-se o terceiro, o terceiro o quarto, e assim por diante.