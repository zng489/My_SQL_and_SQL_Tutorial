# Python-And-SQL

<h10> 
 
<ul>
 
  <li> <strong>ON DELETE</strong> significa que a ação referencial será executada quando um registro for excluído da tabela pai, e <strong> ON UPDATE </strong> indica que a ação referencial será executada quando um registro for modificado na tabela pai. As principais opções para as ações referenciais são as seguintes: <strong> CASCADE </strong>: A opção <strong> CASCADE </strong> permite excluir ou atualizar os registros relacionados presentes na tabela filha automaticamente, quando um registro da tabela pai for atualizado <strong> (ON UPDATE) </strong> ou excluído <strong> (ON DELETE) </strong>. É a opção mais comum aplicada Vejamos um exemplo usando a cláusula <strong> ON DELETE CASCADE </strong>, que é uma das mais comuns usadas em chaves estrangeiras. Todos os exemplos mostrados aqui também podem ser utilizados com a cláusula <strong> ON UPDATE </strong> e, na prática, podemos usar ambas as cláusulas na mesma tabela.Para isso, vamos criar um banco de dados de nome “testes”, contendo duas tabelas relacionadas, chamadas de “Pai” e “Filho”, conforme a seguinte estrutura:
 </li>
 
<li>Second item</li>
<li>Third item</li>
<li>Fourth item</li>
  

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


      <li>
<strong><em> Constraints </em></strong> (restrições) mantém os dados do usuário restritos, e assim evitam que dados inválidos sejam inseridos no banco. A mera definição do tipo de dado para uma coluna é por si só um constraint. Por exemplo, uma coluna de tipo DATE restringe o conteúdo da mesma para datas válidas. 
      </li>



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
	 
```
DROP TABLE sales;

DROP TABLE customers;

DROP TABLE items;

DROP TABLE companies;
```
	 

      <li>
<strong><em> Constraints </em></strong> (restrições) mantém os dados do usuário restritos, e assim evitam que dados inválidos sejam inseridos no banco. A mera definição do tipo de dado para uma coluna é por si só um constraint. Por exemplo, uma coluna de tipo DATE restringe o conteúdo da mesma para datas válidas. 
      </li>

-----------------------------------------------------------	
	
<li><strong><em> UNIQUE KEY </em></strong></li>
	
```
CREATE TABLE customers
(
customer_id INT,
first_name VARCHAR (255),
last_name VARCHAR (255),
email_address VARCHAR (255),
number_of_complaints INT,

PRIMARY KEY (customer_id),
UNIQUE KEY (email_address)
);
	
or
	
DROP TABLE customers;

CREATE TABLE customers
(
customer_id INT AUTO_INCREMENT,
first_name VARCHAR (255),
last_name VARCHAR (255),
email_address VARCHAR (255),
number_of_complaints INT,

PRIMARY KEY (customer_id)
);

ALTER TABLE customers
ADD UNIQUE KEY (email_address);
	
or
	
DROP TABLE customers;

CREATE TABLE customers
(
customer_id INT AUTO_INCREMENT,
first_name VARCHAR (255),
last_name VARCHAR (255),
email_address VARCHAR (255),
number_of_complaints INT,

PRIMARY KEY (customer_id)
);

ALTER TABLE customers
ADD UNIQUE KEY (email_address);

ALTER TABLE customers
DROP INDEX email_address;
	
```
-----------------------------------------------------------	
	
<li><strong><em> DEAFAULT </em></strong> </li>
	
| First Header  | Default |
| ------------- | ------- |
| Content Cell  | 0 |
| Content Cell  | 1 |
	
	
```
DROP TABLE customers;

CREATE TABLE customers
(
customer_id INT,
first_name VARCHAR (255),
last_name VARCHAR (255),
email_address VARCHAR (255),
number_of_complaints INT,

PRIMARY KEY (customer_id)
);


ALTER TABLE customers
CHANGE COLUMN number_of_complaints number_of_complaints_changed INT DEFAULT 0;	
```
-----------------------------------------------------------	
<li><strong><em> CREATE, ALTER, DROP </em></strong></li>	
	
```
DROP TABLE customers;

CREATE TABLE customers
(
customer_id INT AUTO_INCREMENT,
first_name VARCHAR (255),
last_name VARCHAR (255),
gender VARCHAR (255),
email_address VARCHAR (255),
number_of_complaints INT,

PRIMARY KEY (customer_id)
);


ALTER TABLE customers
CHANGE COLUMN number_of_complaints number_of_complaints_changed INT DEFAULT 0;

INSERT INTO customers (first_name, last_name, gender)
VALUES  ('Peter', 'Figaro', 'M');

SELECT * FROM customers;

ALTER TABLE customers
ALTER COLUMN number_of_complaints_changed DROP DEFAULT;
	
	
	
	
DROP TABLE customers;

CREATE TABLE customers
(
customer_id INT AUTO_INCREMENT,
first_name VARCHAR (255),
last_name VARCHAR (255),
gender VARCHAR (255),
email_address VARCHAR (255),
number_of_complaints INT,

PRIMARY KEY (customer_id)
);


ALTER TABLE customers
CHANGE COLUMN number_of_complaints number_of_complaints_changed INT DEFAULT 0;

INSERT INTO customers (first_name, last_name, gender)
VALUES  ('Peter', 'Figaro', 'M');

SELECT * FROM customers;

ALTER TABLE customers
ALTER COLUMN number_of_complaints_changed DROP DEFAULT;


DROP TABLE companies;


CREATE TABLE companies 
(
company_id INT AUTO_INCREMENT,
headquarters_phone_number VARCHAR (255) ,
company_name VARCHAR (255) NOT NULL,
PRIMARY KEY (company_id)
);

ALTER TABLE companies
MODIFY company_name VARCHAR(255) NULL;

ALTER TABLE companies
CHANGE COLUMN company_name company_name VARCHAR(255) NOT NULL;

ALTER TABLE companies
CHANGE COLUMN headquarters_phone_number headquarters_phone_number VARCHAR(255) DEFAULT NULL;

INSERT INTO companies (headquarters_phone_number, company_name)
VALUES ('+1 (202) 555-0196)', 'Company A');

SELECT * FROM companies;
	
	
SELECT 
    first_name, last_name
FROM
    employees;
    
/* 
WHERE Condition
*/
    
SELECT * FROM employees
WHERE first_name = 'Denis';

SELECT * FROM employees
WHERE first_name = 'Denis' AND gender = 'F';


SELECT * FROM employees
WHERE first_name = 'Denis' OR first_name = 'Elvis';


SELECT * FROM employees
WHERE first_name = 'Denis' AND gender = 'M' OR first_name = 'Elvis';

SELECT * FROM employees
WHERE first_name = 'Denis' AND (gender = 'M' OR gender = 'F');


/* 
IN - NOT IN
*/

SELECT * FROM employees
WHERE first_name = 'Cathie' OR first_name = 'Mark' OR first_name = 'Nathan';

SELECT * FROM employees
WHERE first_name IN ('Cathie','Mark','Nathan');


SELECT * FROM employees
WHERE first_name NOT IN ('Cathie','Mark','Nathan');

/* 
LIKE - NOT LIKE
*/

# Mar% --> Mar% any character
SELECT * FROM employees
WHERE first_name LIKE ('Mar%'); 

# Mar% --> Mar% any 4 character
SELECT * FROM employees
WHERE first_name LIKE ('Mar_');

SELECT * FROM employees
WHERE first_name NOT LIKE ('%Mar%');
	
SELECT 
    first_name, last_name
FROM
    employees;
    
/* 
BETWEEN - AND
*/

SELECT * FROM employees
WHERE hire_date NOT BETWEEN '1990-01-01' AND '2000-01-01';
# BETWEEN '1990-01-01' ---------- '2000-01-01'
# -------- NOT BETWEEN '1990-01-01' AND '2000-01-01' -----------
# the hire_date is before '1990-01-01'  or the hire_date is after '2000-01-01'

/* 
IS NOT NULL
*/

SELECT * FROM employees
WHERE first_name IS NOT NULL;

SELECT * FROM employees
WHERE first_name IS NULL;


/* 
Other comparison operator
*/

SELECT * FROM employees
WHERE first_name = 'Mark';

SELECT * FROM employees
WHERE first_name != 'Mark';

SELECT * FROM employees
WHERE hire_date > '2000-01-01';

SELECT * FROM employees
WHERE hire_date >= '2000-01-01';

/* 
SELECTING DISTINCT
*/

SELECT gender FROM employees;
#|gender|
#|  M  |
#|  F  |
#|  M  |	

SELECT DISTINCT gender FROM employees;
#|gender|
#|  M  |
#|  F  	
	
	

/* 
Introduction to Aggregate Functions
COUNT()
SUM()
MIN()
MAX()
AVG()
*/

SELECT count(emp_no) FROM employees;

SELECT * FROM employees WHERE first_name IS NULL;

SELECT COUNT(emp_no) FROM employees;

SELECT COUNT(first_name) FROM employees;
# Differents COUNT names



/* 
ORDER BY
*/

SELECT * FROM employees ORDER BY first_name;

SELECT * FROM employees ORDER BY first_name ASC;

SELECT * FROM employees ORDER BY first_name DESC;

SELECT * FROM employees ORDER BY emp_no DESC;

/* 
ORDER BY
*/

SELECT first_name FROM employees GROUP BY first_name;
# first_name
# Georgi
# Bezalel
# Parto
# Chirstian
# Kyoichi

SELECT DISTINCT first_name FROM employees;
# first_name
# Georgi
# Bezalel
# Parto
# Chirstian
# Kyoichi

SELECT COUNT(first_name) FROM employees GROUP BY first_name;

SELECT first_name, COUNT(first_name) FROM employees GROUP BY first_name;
# first_name | COUNT(first_name)
# Georgi	      253
# Bezalel	      228
# Parto		      228

SELECT 
    first_name, COUNT(first_name)
FROM
    employees
GROUP BY first_name
ORDER BY first_name DESC;

SELECT column_names(s)
FROM table_name
WHERE conditions
GROUP BY column_names(s)
ORDER BY column_name(s);

############################################
/* 
Using Aliases (AS)
*/

SELECT 
    first_name, COUNT(first_name) AS names_count
FROM
    employees
GROUP BY first_name
ORDER BY first_name;

/* 
HAVING
The HAVING clause was added to SQL because the WHERE keyword cannot be used with aggregate functions.
HAVING COUNT()
*/

SELECT 
   *
FROM
    employees
HAVING hire_date >= '2000-01-01';



SELECT 
    first_name, COUNT(first_name) AS names_count
FROM
    employees
GROUP BY first_name
HAVING COUNT(first_name) > 250
ORDER BY first_name;
	
	
SELECT 
    *
FROM
    employees
ORDER BY emp_no DESC
LIMIT 10;

INSERT INTO employees 
( 
emp_no,
birth_date,
first_name, 
last_name, 
gender, 
hire_date
 ) VALUES
 (
999901,
'1986-04-21',
'John',
'Smith',
'M',
'2011-01-01'
 )
 
 
 CREATE TABLE departments_dup
 (
 dept_no CHAR(4) NOT NULL,
 dept_name VARCHAR(40) NOT NULL
 );
 
 
 INSERT INTO departments_dup
 (
 dept_no,
 dept_name
 )
 SELECT * FROM departments;
 
 SELECT * FROM departments_dup
 ORDER BY dept_no;
```
-----------------------------------------------------------	
<strong>
/* The UPDATE Statement*/
</strong>	
	
```
UPDATE table_name
SET column_1 = value_1, column_2 = value_2
WHERE conditions;
	
USE employees;
SELECT * FROM employees
WHERE emp_no = 999901;	
	
SELECT 
    *
FROM
    employees
ORDER BY emp_no DESC
LIMIT 10;

INSERT INTO employees 
( 
emp_no,
birth_date,
first_name, 
last_name, 
gender, 
hire_date
 ) VALUES
 (
999901,
'1986-04-21',
'John',
'Smith',
'M',
'2011-01-01'
 )
 
 
 CREATE TABLE departments_dup
 (
 dept_no CHAR(4) NOT NULL,
 dept_name VARCHAR(40) NOT NULL
 );
 
 
 INSERT INTO departments_dup
 (
 dept_no,
 dept_name
 )
 SELECT * FROM departments;
 
 SELECT * FROM departments_dup
 ORDER BY dept_no;
 
```	
| Name     | Character || Name     | Character |
| ---      | ---       |
| Backtick | `         |

# DELETE FROM table_name
# WHERE conditions;

USE employees;
COMMIT;

SELECT * FROM employees WHERE emp_no = 99993;
SELECT * FROM titles WHERE emp_no = 99993;


DELETE FROM employees WHERE emp_no = 99993;

ROLLBACK;


SELECT * FROM departments_dup ORDER BY dept_no;

DELETE FROM departments_dup;

ROLLBACK;

	
-----------------------------------------------------------	
</ul>
</h10>





