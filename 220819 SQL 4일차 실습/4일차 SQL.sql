-- SQLite
-- 4일차 SQL.sql

SELECT 
    id, 
    smoking, 
    CASE 
        WHEN smoking = 1 THEN '비흡연자'
        WHEN smoking = 2 THEN '흡연자'
        WHEN smoking = 3 THEN '헤비스모커'
        ELSE '무응답'
    END
FROM healthcare
LIMIT 50;

-- 청소년(~18), 청년(~35), 중년(~60), 장년(~75), 노년(75~)
SELECT 
    first_name,
    last_name,
    age,
    CASE 
        WHEN age <= 18 THEN '청소년'
        WHEN age <= 35 THEN '청년'
        WHEN age <= 60 THEN '중년'
        WHEN age <= 75 THEN '장년'
        ELSE '노년' 
    END
FROM users
LIMIT 5;

SELECT COUNT(*)
FROM users 
WHERE age = (SELECT MIN(age) FROM users);

SELECT COUNT(*)
FROM users
WHERE balance > (SELECT AVG(balance) FROM users);

SELECT 
    COUNT(*)
FROM users
WHERE country = (SELECT country FROM users
WHERE last_name = '고' AND first_name = '병철');

SELECT 
    (SELECT COUNT(*) FROM users) AS 총인원,
    (SELECT AVG(balance) FROM users) AS 평균연봉;

SELECT 
    COUNT(*)
FROM users
WHERE country = (SELECT country FROM users
WHERE last_name = '고' AND first_name = '병철');


SELECT 
    COUNT(*)
FROM users
WHERE country IN (SELECT country FROM users
WHERE last_name = '김' AND first_name = '서영');

SELECT 
    last_name,
    MIN(age)
FROM users
GROUP BY last_name;

SELECT
    last_name,
    first_name,
    age
FROM users
WHERE (last_name, age) IN (
    SELECT 
        last_name,
        MIN(age)
    FROM users
    GROUP BY last_name)
ORDER BY last_name;

SELECT ArtistId 
FROM artists
WHERE Name = 'Queen';

SELECT * 
FROM albums
WHERE ArtistId = (
SELECT ArtistId 
FROM artists
WHERE Name = 'Queen');