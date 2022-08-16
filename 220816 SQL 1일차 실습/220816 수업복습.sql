-- SQLite
-- members라는 이름의 테이블 생성
CREATE TABLE family (
    id INTEGER PRIMARY KEY, 
    name TEXT,
    address TEXT,
    age INTEGER
);

-- 값 추가
INSERT INTO family VALUES (1, '황지선', '여수시 봉계동', 25);
INSERT INTO family VALUES (2, '채형원', '서울특별시 동대문구', 29);
INSERT INTO family VALUES 
(3, '나재민', '부산광역시 진구', 23),
(4, '김도영', '경기도 안산시', 27);
INSERT INTO family VALUES (5, '채형원', '광주광역시 광산구 월계동', 29);

-- 테이블 조회
SELECT * FROM family;
SELECT name FROM family;
SELECT COUNT(name) AS count FROM family;
SELECT * FROM family LIMIT 2;
SELECT * FROM family WHERE age >= 25;
SELECT DISTINCT address FROM family WHERE name = '채형원';
SELECT DISTINCT age FROM family WHERE name = '채형원';

-- 테이블 삭제
-- DROP TABLE family;