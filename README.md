# Final_test_for_the_specialization_block

history linux
  401  echo "# Final_test_for_the_specialization_block" >> README.md
  402  git init
  403  git add README.md
  404  git commit -m "first commit"
  405  git branch -M main
  406  git remote add origin git@github.com:Levochka108/Final_test_for_the_specialization_block.git
  407  git push -u origin main
  408  git status
  409  git log
  410  echo "собаки" > "Домашние животные"
  411  echo "кошки" >> "Домашние животные"
  412  echo "хомяки" >> "Домашние животные"
  413  echo "лошади" > "Вьючные животные"
  414  echo "верблюды" >> "Вьючные животные"
  415  echo "ослы" >> "Вьючные животные"
  416  cat "Домашние животные" "Вьючные животные" > "Друзья человека"
  417  cat "Друзья человека"
  418  git add .
  419  git commit -m "Задача 1"
  420  history




Задания с 7 по 12


levochka108@levochka108-VirtualBox:~/levochka108/GB$ mysql -u root -p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 8
Server version: 8.0.34-0ubuntu0.23.04.1 (Ubuntu)

Copyright (c) 2000, 2023, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> USE FriendsOfHumans;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> INSERT INTO DomesticAnimals (AnimalType, Name, Command, BirthDate)
    -> VALUES
    ->     ('Dog', 'Rex', 'Fetch the ball', '2020-05-15'),
    ->     ('Cat', 'Whiskers', 'Purr', '2019-07-10'),
    ->     ('Hamster', 'Nibbles', 'Run in the wheel', '2021-02-28');
Query OK, 3 rows affected (0.00 sec)
Records: 3  Duplicates: 0  Warnings: 0

mysql> INSERT INTO PackAnimals (AnimalType, Name, Command, BirthDate)
    -> VALUES
    ->     ('Horse', 'Shadow', 'Carry heavy loads', '2018-03-20'),
    ->     ('Camel', 'Sandy', 'Carry cargo in the desert', '2017-11-05'),
    ->     ('Donkey', 'Eeyore', 'Carry goods up the mountain', '2019-09-12');
Query OK, 3 rows affected (0.00 sec)
Records: 3  Duplicates: 0  Warnings: 0

mysql> DELETE FROM PackAnimals WHERE AnimalType = 'Camel';
Query OK, 1 row affected (0.01 sec)

mysql> CREATE TABLE HorsesAndDonkeys AS
    -> SELECT * FROM PackAnimals WHERE AnimalType = 'Horse'
    -> UNION ALL
    -> SELECT * FROM PackAnimals WHERE AnimalType = 'Donkey';
Query OK, 2 rows affected (0.03 sec)
Records: 2  Duplicates: 0  Warnings: 0

mysql> CREATE TABLE YoungAnimals (
    ->     AnimalID INT AUTO_INCREMENT PRIMARY KEY,
    ->     AnimalType VARCHAR(50) NOT NULL,
    ->     Name VARCHAR(50) NOT NULL,
    ->     Command VARCHAR(100),
    ->     BirthDate DATE
    -> );
Query OK, 0 rows affected (0.04 sec)

mysql> INSERT INTO YoungAnimals (AnimalType, Name, Command, BirthDate)
    -> SELECT
    ->     AnimalType,
    ->     Name,
    ->     Command,
    ->     BirthDate
    -> FROM
    ->     (SELECT
    ->         AnimalType,
    ->         Name,
    ->         Command,
    ->         BirthDate,
    ->         TIMESTAMPDIFF(YEAR, BirthDate, CURDATE()) AS AgeInYears,
    ->         TIMESTAMPDIFF(MONTH, BirthDate, CURDATE()) AS AgeInMonths
    ->     FROM
    ->         DomesticAnimals
    ->     UNION ALL
    ->     SELECT
    ->         AnimalType,
    ->         Name,
    ->         Command,
    ->         BirthDate,
    ->         TIMESTAMPDIFF(YEAR, BirthDate, CURDATE()) AS AgeInYears,
    ->         TIMESTAMPDIFF(MONTH, BirthDate, CURDATE()) AS AgeInMonths
    ->     FROM
    ->         PackAnimals) AS AllAnimals
    -> WHERE
    ->     AgeInYears >= 1 AND AgeInYears < 3;
Query OK, 1 row affected (0.00 sec)
Records: 1  Duplicates: 0  Warnings: 0

mysql> 12. Объединить все таблицы в одну, при этом сохраняя поля, указывающие на 
    -> прошлую принадлежность к старым таблицам.
    -> CREATE TABLE AllAnimals (
    ->     AnimalID INT AUTO_INCREMENT PRIMARY KEY,
    ->     AnimalType VARCHAR(50) NOT NULL,
    ->     Name VARCHAR(50) NOT NULL,
    ->     Command VARCHAR(100),
    ->     BirthDate DATE,
    ->     SourceTable VARCHAR(50) NOT NULL
    -> );
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '12. Объединить все таблицы в одну, при этом со' at line 1
mysql> CREATE TABLE AllAnimals (
    ->     AnimalID INT AUTO_INCREMENT PRIMARY KEY,
    ->     AnimalType VARCHAR(50) NOT NULL,
    ->     Name VARCHAR(50) NOT NULL,
    ->     Command VARCHAR(100),
    ->     BirthDate DATE,
    ->     SourceTable VARCHAR(50) NOT NULL
    -> );
Query OK, 0 rows affected (0.03 sec)

mysql> -- Добавляем данные из таблицы DomesticAnimals и указываем источник "DomesticAnimals"
mysql> INSERT INTO AllAnimals (AnimalType, Name, Command, BirthDate, SourceTable)
    -> SELECT
    ->     AnimalType,
    ->     Name,
    ->     Command,
    ->     BirthDate,
    ->     'DomesticAnimals' AS SourceTable
    -> FROM DomesticAnimals;
Query OK, 3 rows affected (0.00 sec)
Records: 3  Duplicates: 0  Warnings: 0

mysql> 
mysql> -- Добавляем данные из таблицы PackAnimals и указываем источник "PackAnimals"
mysql> INSERT INTO AllAnimals (AnimalType, Name, Command, BirthDate, SourceTable)
    -> SELECT
    ->     AnimalType,
    ->     Name,
    ->     Command,
    ->     BirthDate,
    ->     'PackAnimals' AS SourceTable
    -> FROM PackAnimals;
Query OK, 2 rows affected (0.01 sec)
Records: 2  Duplicates: 0  Warnings: 0

mysql> 
mysql> -- Добавляем данные из таблицы YoungAnimals и указываем источник "YoungAnimals"
mysql> INSERT INTO AllAnimals (AnimalType, Name, Command, BirthDate, SourceTable)
    -> SELECT
    ->     AnimalType,
    ->     Name,
    ->     Command,
    ->     BirthDate,
    ->     'YoungAnimals' AS SourceTable
    -> FROM YoungAnimals;
Query OK, 1 row affected (0.01 sec)
Records: 1  Duplicates: 0  Warnings: 0

