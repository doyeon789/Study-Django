-- 공통
SELECT * FROM articles;
DROP TABLE articles;
PRAGMA table_info('articles');


-- 실습 테이블 생성
CREATE TABLE articles(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(100) NOT NULL,
    content VARCHAR(200) NOT NULL,
    createAt DATE NOT NULL
);


-- 1. Insert data into table
INSERT INTO 
    articles(title, content, createAt) 
VALUES
    ('hello', 'world', '2026-04-28'); 


INSERT INTO 
    articles(title, content, createAt) 
VALUES
    ('title1', 'content1', '2026-04-28'),
    ('title2', 'content2', '2026-04-28'),
    ('title3', 'content3', '2026-04-28');
    

INSERT INTO 
    articles(title, content, createAt) 
VALUES
    ('제목', '내용', DATE()); 


-- 2. Update data in table
UPDATE
    articles
SET
    title = 'update Title'
WHERE
    id = 1

-- 전체 레코드르 ㄹ수정하지 않도록 하는 방법
-- 1. 먼저 SLEECT로 검증
-- (1) 영향 받을 행을 확안
-- SLECT * FROM articles WHERE id =  1
-- (2) 확인 후 UPDATE/DELETE


UPDATE
    articles
SET
    title = 'update Title',
    content = 'update Content'
WHERE
    id = 2;


-- 3. Delete data from table
DELETE FROM articles
WHERE id = 1;


-- 심화
DELETE FROM articles
WHERE id IN (
    SELECT id
    FROM articles
    ORDER BY createAt ASC
    LIMIT 2
);