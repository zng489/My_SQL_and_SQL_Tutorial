# Python-And-SQL

<h10> 
 
<ul>
 
  <li> <strong>ON DELETE</strong> significa que a ação referencial será executada quando um registro for excluído da tabela pai, e <strong> ON UPDATE </strong> indica que a ação referencial será executada quando um registro for modificado na tabela pai. As principais opções para as ações referenciais são as seguintes: <strong> CASCADE </strong>: A opção <strong> CASCADE </strong> permite excluir ou atualizar os registros relacionados presentes na tabela filha automaticamente, quando um registro da tabela pai for atualizado <strong> (ON UPDATE) </strong> ou excluído <strong> (ON DELETE) </strong>. É a opção mais comum aplicada Vejamos um exemplo usando a cláusula <strong> ON DELETE CASCADE </strong>, que é uma das mais comuns usadas em chaves estrangeiras. Todos os exemplos mostrados aqui também podem ser utilizados com a cláusula <strong> ON UPDATE </strong> e, na prática, podemos usar ambas as cláusulas na mesma tabela.Para isso, vamos criar um banco de dados de nome “testes”, contendo duas tabelas relacionadas, chamadas de “Pai” e “Filho”, conforme a seguinte estrutura:
 </li>
 
<li>Second item</li>
<li>Third item</li>
<li>Fourth item</li>
</ul>
  
</h10>

 ```
 DROP TABLE sales;

 CREATE TABLE sales
 (
	 purchase_number INT AUTO_INCREMENT,
	 date_of_purchase DATE NOT NULL,
	 customer_id INT,
	 item_code VARCHAR(10),
 PRIMARY KEY (purchase_number)
 );

 ALTER TABLE Sales
 ADD FOREIGN KEY (customer_id) REFERENCES customers (customer_id) ON DELETE CASCADE;
 
```

<h10>
 <ul>
      <li>
<strong><em> Constraints </em></strong> (restrições) mantém os dados do usuário restritos, e assim evitam que dados inválidos sejam inseridos no banco. A mera definição do tipo de dado para uma coluna é por si só um constraint. Por exemplo, uma coluna de tipo DATE restringe o conteúdo da mesma para datas válidas. 
      </li>
  <ul>
</h10>

```
DROP TABLE sales;

CREATE TABLE sales
(
	purchase_number INT AUTO_INCREMENT,
	date_of_purchase DATE NOT NULL,
	customer_id INT,
	item_code VARCHAR(10),
PRIMARY KEY (purchase_number)
);

ALTER TABLE Sales
ADD FOREIGN KEY (customer_id) REFERENCES customers (customer_id) ON DELETE CASCADE;

ALTER TABLE sales
DROP FOREIGN KEY sales_ibfk_1;
```










