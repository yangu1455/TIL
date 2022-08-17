-- SQLite

-- 테이블 생성
-- 정호,유,40,전라북도,016-7280-2855,370
CREATE TABLE users (
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country TEXT NOT NULL,
    phone TEXT NOT NULL,
    balance INTEGER NOT NULL
);

.mode csv
-- 같은 디렉토리에 있는 users.csv 파일을 users 테이블로
.import users.csv users


SELECT * FROM users LIMIT 5;
SELECT age, first_name FROM users WHERE age >= 40 AND last_name = '장';

SELECT COUNT(*) FROM users WHERE age >= 35;
SELECT MIN(age), first_name, country FROM users WHERE last_name = '김';
SELECT AVG(age) FROM users WHERE age >= 30;
SELECT MAX(balance), first_name, last_name FROM users;

SELECT COUNT(*) FROM users WHERE phone LIKE '016-%';
SELECT COUNT(*) FROM users WHERE country LIKE '전라%';

SELECT last_name, first_name FROM users ORDER BY age ASC LIMIT 5;
SELECT last_name, first_name, balance FROM users ORDER BY balance DESC, last_name ASC LIMIT 5;
