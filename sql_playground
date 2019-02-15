# show database
SHOW DATABASES;

# create databse
CREATE DATABASE test_db;

# drop databse
DROP DATABASE test_db;

# INSERT DATA
INSERT INTO cats(name, age) VALUES("Blue", 1);
INSERT INTO cats(age, name) VALUES(1, "Blue");

# Multiple Insert Data
INSERT INTO cats(name, age) VALUES("Heck", 20), ("Ride", 22), ("Crayon", 15);

# TABLE with NOT NULL
# 아무런 값도 Insert 하지 않는다면 NULL이 아닌 False값이 들어감 (string이라면 "", INT라면 0)
CREATE TABLE cats2(name varchar(50) NOT NULL, age INT NOT NULL);

# SET DEFAULT
CREATE TABLE cats3(name varchar(50) NOT NULL DEFAULT "Unnamed", age INT NOT NULL DEFAULT 99);

# SET PRIMARY KEY with Auto Increment
CREATE TABLE cats(cat_id INT NOT NULL AUTO_INCREMENT, name VARCHAR(50), age INT, PRIMARY KEY (cat_id))
# or
CREATE TABLE cats(cat_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), age INT)

# FOREIGN KEY CONSTRAINT
CREATE TABLE Orders (
    OrderID int NOT NULL,
    OrderNumber int NOT NULL,
    PersonID int,
    PRIMARY KEY (OrderID),
    FOREIGN KEY (PersonID) REFERENCES Persons(PersonID)
);
                                                                                              
# CONCAT
SELECT book_id, title, CONCAT(author_fname, ' ', author_lname) FROM books;
SELECT book_id, title, CONCAT_WS('-', author_fname, author_lname) FROM books;

# SUBSTRING
SELECT SUBSTRING("hello world", 1, 4) # hell
SELECT SUBSTRING("hello world", 7) # world (n번째 부터 모두)
SELECT SUBSTRING("Hello World", -3) #rld (끝에서 3번째부터 모두)
SELECT SUBSTRING(title, 1, 10) FROM books
SELECT SUBSTR(title, 1, 10) FROM books  # 세 글자 짧음

# CONCAT + SUBSTRING
SELECT CONCAT(SUBSTRING(title, 1, 10), "...") FROM books;

# REPLACE
SELECT REPLACE("Hello World", "Hell", "####") > (####oWorld), (case sensitive)
SELECT CONCAT(SUBSTRING(REPLACE(title, "e", 3), 1, 10), "...") as eReplacedto3 FROM books;

# STRING CHALLENGES
SELECT
   author_lname AS forwards,
   REVERSE(author_lname) AS backwards
FROM books;

SELECT
   UPPER
   (
      CONCAT(author_fname, ' ', author_lname)
   ) AS 'full name in caps'
FROM books;

SELECT
   CONCAT(title, ' was released in ', released_year) AS blurb
FROM books;
SELECT
   title,
   CHAR_LENGTH(title) AS 'character count'
FROM books;

SELECT
   CONCAT(SUBSTRING(title, 1, 10), '...') AS 'short title',
   CONCAT(author_lname, ',', author_fname) AS author,
   CONCAT(stock_quantity, ' in stock') AS quantity
FROM books;

# _ wild card exactly match the number of character unlike % wildcard
SELECT
   title, stock_quantity
FROM books
WHERE stock_quantity LIKE '__'; 

# ORDER BY의 인자로 숫자를 주면 n번째 Column이라는 의미가 된다. 아래 예제는 author_lname으로 먼저 정렬하고 title로 2차 정렬.
SELECT title, author_lname FROM books ORDER BY 2,1;

# Count
SELECT COUNT(*) FROM books;


########### DATA TYPES ##################

# CHAR(5) - 5글자로 강제하고 5글자가 안되면 Pad, 넘으면 truncate함

# DECIMAL - 소수 DECIMAL(M, S) : 총 M자리의 수인데 소수점 이하 S자리만큼을 포함한 수
INSERT INTO item VALUES(200.829823); # 200.82 (만약 table이 decimal(5,2)라면)
INSERT INTO item VALUES(20.829823); # 20.829
INSERT INTO item VALUES(2.829823); # 2.8298


# FLOAT, DOUBLE : FLOAT은 작은 소수. DOUBLE은 큰 소수라고 일단 알아두기.
# FLOAT/DOUBLE은 DECIMAL에 비해 부정확하다. (엡실론 문제겠지)
# 만약 정확함이 크리티컬하게 중요한 부분이라면 DECIMAL을, 그렇지 않다면 FLOAT/DOUBLE을 고려하자.
# 만약 DECIMAL을 쓰지 않는다면, FLOAT/DOUBLE이 옵션인데 이 둘 중 더 정확한 녀석은 DOUBLE이니 DOUBLE을 고려하자.

# DATETIME : YYYY-MM-DD HH:MM:SS < 이 포맷만 지키면 DATETIME 자료형을 만족.
INSERT INTO people VALUES ('1990-11-13 12:24:18');
INSERT INTO people(name, birthdate, birthtime, birthday) VALUES ('Padma', '1983-11-11', '10:07:35', '1983-11-11 10:07:35');
CURDATE() - 현재 DATE
CURTIME() - 현재 TIME
NOW() - 현재 DATETIME


# DATETIME에서 사용 가능한 여러 Method가 존재함
# 하지만 끝판왕은 그냥 DATE_FORMAT. example) DATE_FORMAT(now(), '%y-%m-%d'); 와 같은 방식으로 만들면 원하는 포맷으로 데이터 출력이 가능.
SELECT name, birthdate, DAY(birthdate), DAYOFWEEK(birthday), DAYNAME(birthday), DAYOFYEAR(birthday) FROM people;  
SELECT name, birthdate, DATEDIFF(now(), birthdate) as since_born FROM people;

SELECT birthday, DATE_ADD(birthday, INTERVAL 1 YEAR) as '+1year' FROM people;
SELECT birthday, birthday + INTERVAL 1 YEAR as '+1year' FROM people;
SELECT birthday, birthday + INTERVAL 1 MONTH as '+1year' FROM people; (만료기한, 연장기한같은거 설정할 때 좋을 것 같다.)

# TIMESTAMP
# TIMESTAMP도 시간을 저장하는 자료형이다.
# 하지만 1970-01-01 ~ 2038-01-19 까지밖에 저장하지 못한다.
# 그럼에도 불구하고 이 자료형이 갖는 장점은, 크기가 4byte라는 것이다. (DATETIME은 8바이트)

CREATE TABLE comment(
   content VARCHAR(100),
   changed_at TIMESTAMP default now() on update now()
   # now()도 되고 current_timestamp도 가능
);

###### LOGICAL OPERATOR ########

# LIKE, NOT LIKE

SELECT title FROM books WHERE title LIKE 'W%';
SELECT title FROM books WHERE title NOT LIKE '%love%';

# 'a' = 'A'?
# 그렇다. 다른 language에서는 A가 더 크겠지만 SQL에서는 case sensitive하지 않다.
# where title = 'hello world' 를 하던 where title = 'HELLO WORLD'를 하던 결과가 같다.
# 따라서 lowercase = uppercase in SQL!

ALTER table topup_log add column rf_uid VARCHAR(45) character set utf8mb4 collate utf8mb4_general_ci NOT NULL AFTER user_Id;
ALTER TABLE topup_log DROP COLUMN rf_card_id;
ALTER TABLE topup_log ADD CONSTRAINT FOREIGN KEY(rf_card_id) REFERENCES rf_match(rf_uid);
ALTER TABLE topup_log DROP PRIMARY KEY, ADD PRIMARY KEY (`evt_date`, `user_id`, `rf_uid`);
ALTER TABLE topup_log_original CHANGE COLUMN `cnt_inc_dec` `evt_desc` VARCHAR(10) NOT NULL DEFAULT "NC";
                  
############# Relationships ###############

# Inner Join : 두 table의 교집합을 매칭
# Implicit Inner Join
select * from customers, orders where customers.id = orders.customer_id;

# Explicit Inner Join
select first_name, last_name, order_date, amount from customers join orders on customers.id = orders.customer_id;

# LEFT JOIN : Left Table의 모든 데이터 + (Left Table에 매칭되는 정보가 있으면) Rigth Table에서 Join
select * from customers left join orders on customers.id = orders.customer_id;
SELECT
    first_name,
    last_name,
    IFNULL(sum(amount), 0) as total_spent
FROM customers LEFT JOIN orders 
ON customers.id = orders.customer_id GROUP BY customers.id;

DELIMITER $$
CREATE trigger must_be_adult
    BEFORE Insert on users for each row
    BEGIN
        IF NEW.age < 18
        THEN
            SIGNAL SQLSTATE '45000'
                SET message_text = 'MUST BE AN ADULT!';
            END IF;
    END;
$$
DELIMITER ;
