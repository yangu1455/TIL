CREATE TABLE users (
    id INT PRIMARY KEY,
    name TEXT,
    role_id INT
);

INSERT INTO users VALUES 
    (1, '관리자', 1),
    (2, '황지선', 2),
    (3, '채형원', 1);

CREATE TABLE role (
    id INT PRIMARY KEY, 
    title TEXT
);

INSERT INTO role VALUES 
    (1, 'admin'),
    (2, 'staff'),
    (3, 'student');

CREATE TABLE articles (
    id INT PRIMARY KEY, 
    title TEXT,
    content TEXT,
    user_id INT
);

INSERT INTO articles VALUES 
    (1, '1번글', '111', 1),
    (2, '2번글', '222', 2),
    (3, '3번글', '333', 1),
    (4, '4번글', '444', NULL);

.mode column
SELECT * FROM users;
SELECT * FROM role;
SELECT * FROM articles;


------------


SELECT *
FROM users 
INNER JOIN role
    ON users.role_id = role.id;
-- id  name  role_id  id  title
-- --  ----  -------  --  -----
-- 1   관리자   1        1   admin
-- 2   황지선   2        2   staff
-- 3   채형원   1        1   admin

SELECT 
    users.name, 
    role.title
FROM users 
INNER JOIN role
    ON users.role_id = role.id;
-- name  title
-- ----  -----
-- 관리자   admin
-- 황지선   staff
-- 채형원   admin

SELECT *
FROM users 
INNER JOIN role
    ON users.role_id = role.id
WHERE role.id = 2;
-- id  name  role_id  id  title
-- --  ----  -------  --  -----
-- 2   황지선   2        2   staff

SELECT *
FROM users 
INNER JOIN role
    ON users.role_id = role.id
ORDER BY users.name DESC;
-- id  name  role_id  id  title
-- --  ----  -------  --  -----
-- 2   황지선   2        2   staff
-- 3   채형원   1        1   admin
-- 1   관리자   1        1   admin

SELECT * 
FROM articles 
LEFT OUTER JOIN users
    ON articles.user_id = users.id;

-- id  title  content  user_id  id  name  role_id
-- --  -----  -------  -------  --  ----  -------
-- 1   1번글    111      1        1   관리자   1      
-- 2   2번글    222      2        2   황지선   2      
-- 3   3번글    333      1        1   관리자   1      
-- 4   4번글    444                              

SELECT * 
FROM articles 
LEFT OUTER JOIN users
    ON articles.user_id = users.id
WHERE articles.user_id IS NOT NULL;
-- id  title  content  user_id  id  name  role_id
-- --  -----  -------  -------  --  ----  -------
-- 1   1번글    111      1        1   관리자   1      
-- 2   2번글    222      2        2   황지선   2      
-- 3   3번글    333      1        1   관리자   1  

SELECT * 
FROM articles 
FULL OUTER JOIN users
    ON articles.user_id = users.id;
-- Error: in prepare, RIGHT and FULL OUTER JOINs are not currently supported (1)

SELECT * 
FROM users 
CROSS JOIN role;
-- id  name  role_id  id  title  
-- --  ----  -------  --  -------
-- 1   관리자   1        1   admin  
-- 1   관리자   1        2   staff  
-- 1   관리자   1        3   student
-- 2   황지선   2        1   admin  
-- 2   황지선   2        2   staff  
-- 2   황지선   2        3   student
-- 3   채형원   1        1   admin  
-- 3   채형원   1        2   staff  
-- 3   채형원   1        3   student

-- 3개의 테이블 조인
SELECT * 
FROM articles
JOIN users
    ON articles.user_id = users.id
JOIN role
    ON users.role_id = role.id;
-- id  title  content  user_id  id  name  role_id  id  title
-- --  -----  -------  -------  --  ----  -------  --  -----
-- 1   1번글    111      1        1   관리자   1        1   admin
-- 2   2번글    222      2        2   황지선   2        2   staff
-- 3   3번글    333      1        1   관리자   1        1   admin


---------------------------------


SELECT * 
FROM albums 
JOIN artists 
    ON albums.ArtistId = artists.ArtistId
LIMIT 5;

SELECT * 
FROM albums 
LEFT JOIN artists 
    ON albums.ArtistId = artists.ArtistId
LIMIT 5;