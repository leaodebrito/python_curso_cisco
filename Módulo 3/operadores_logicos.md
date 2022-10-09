Operadores de comparação: maior que
Pode também fazer uma pergunta de comparação usando o operador > (maior que).

Se quiser saber se há mais ovelhas pretas do que brancas, pode escrevê-lo da seguinte forma:

black_sheep > white_sheep  # Greater than


True confirma-o; False nega-o.


Operadores de comparação: maior que ou igual a
O operador maior que tem outra variante especial, não estrita, mas é denotada de forma diferente da notação aritmética clássica: >= (maior que ou igual a)

Existem dois sinais subsequentes, não um.

Ambos os operadores (estritos e não-estritos), bem como os outros dois discutidos na próxima secção, são operadores binários com ligação à esquerda, e a sua prioridade é maior do que a mostrada por == e !=.

Se quisermos descobrir se temos ou não de usar um chapéu quente, fazemos a seguinte pergunta:

centigrade_outside ≥ 0.0  # Greater than or equal to


Operadores de comparação: menor que ou igual a
Como já deve ter adivinhado, os operadores utilizados neste caso são: o < (less than) operator and its non-strict sibling: <= (menor que ou igual a).

Veja este exemplo simples:

current_velocity_mph < 85  # Less than
current_velocity_mph ≤ 85  # Less than or equal to


Vamos verificar se existe o risco de ser multado pela polícia rodoviária (a primeira pergunta é rigorosa, a segunda não).


Fazer uso das respostas
O que pode fazer com a resposta (ou seja, o resultado de uma operação de comparação) que obtém do computador?

Há pelo menos duas possibilidades: primeiro, pode memorizá-la (armazená-la numa variável) e utilizá-la mais tarde. Como se faz isso? Bem, utilizaria uma variável arbitrária como esta:

answer = number_of_lions >= number_of_lionesses


O conteúdo da variável dar-lhe-á a resposta à pergunta feita.


A segunda possibilidade é mais conveniente e muito mais comum: pode usar a resposta que obtém para tomar uma decisão sobre o futuro do programa.

Precisa de uma instrução especial para este fim, e discutiremos isso muito em breve.

Agora precisamos de atualizar a nossa tabela de prioridades e colocar todos os novos operadores na mesma. Agora parece-se com o seguinte:

Prioridade	Operador	
1	+, -	unário
2	**	
3	*, /, //, %	
4	+, -	binário
5	<, <=, >, >=	
6	==, !=	