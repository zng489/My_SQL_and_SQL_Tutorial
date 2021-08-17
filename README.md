# Python-And-SQL

Os itens entre colchetes [ ] são opcionais. ON DELETE significa que a ação referencial será executada quando um registro for excluído da tabela pai, e ON UPDATE indica que a ação referencial será executada quando um registro for modificado na tabela pai.

As principais opções para as ações referenciais são as seguintes:

CASCADE: A opção CASCADE permite excluir ou atualizar os registros relacionados presentes na tabela filha automaticamente, quando um registro da tabela pai for atualizado (ON UPDATE) ou excluído (ON DELETE). É a opção mais comum aplicada


Vejamos um exemplo usando a cláusula ON DELETE CASCADE, que é uma das mais comuns usadas em chaves estrangeiras. Todos os exemplos mostrados aqui também podem ser utilizados com a cláusula ON UPDATE e, na prática, podemos usar ambas as cláusulas na mesma tabela.
Para isso, vamos criar um banco de dados de nome “testes”, contendo duas tabelas relacionadas, chamadas de “Pai” e “Filho”, conforme a seguinte estrutura:


```mermaid
graph TD;
  A-->B;
  A-->C;
  B-->D;
  C-->D;
```
















