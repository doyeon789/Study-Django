-- 01. Querying data
SELECT 
  LastName
FROM
  employees;


SELECT
  LastName, FirstName
FROM
  employees;


SELECT
  *
FROM
  employees;  


SELECT
  FirstName AS '이름'
FROM
  employees;


SELECT
  Name,
  Milliseconds / 60000 AS '재생 시간(분)'
FROM
  tracks;



-- 02. Sorting data
SELECT 
  FirstName
FROM 
  employees
ORDER BY
  FirstName ASC;


SELECT
  FirstName
FROM
  employees
ORDER BY
  FirstName DESC;


SELECT
  Country, City
FROM 
  customers
ORDER BY
  Country DESC,
  City ASC;


SELECT
  Name,
  Milliseconds / 60000 AS '재생 시간(분)'
FROM
  tracks
ORDER BY
  Milliseconds DESC;



-- NULL 정렬 예시
SELECT 
  ReportsTo
FROM
  employees
ORDER BY
  ReportsTo;


-- 03. Filtering data
SELECT DISTINCT
  Country
FROM
  customers
ORDER BY
  Country;


SELECT 
  LastName, FirstName, City
FROM
  customers
WHERE
  City = 'Prague';


SELECT 
  LastName, FirstName, City
FROM
  customers
WHERE
  City != 'Prague';


SELECT
  LastName, Firstname, Company, Country
FROM
  customers
WHERE
-- NULL = NULL
-- 값이 없는 것 = 값이 없는 것  ==> 둘 다 모르는 상태에서 비교하는거라 결과도 모름
-- 3차(진) 논리
  Company IS NULL
  AND Country = 'USA';


SELECT
  LastName, Firstname, Company, Country
FROM
  customers
WHERE
  Company IS NULL
  OR Country = 'USA';


SELECT
  Name, Bytes
FROM 
  tracks
WHERE
  Bytes BETWEEN 10000 AND 500000;


SELECT
  Name, Bytes
FROM
  tracks
WHERE 
  Bytes BETWEEN 10000 AND 500000
ORDER BY
  Bytes ASC;


SELECT
  LastName, FirstName, Country
FROM
  customers
WHERE
  Country IN ('Canada','France','Germany')


SELECT
  LastName, FirstName
FROM
  customers
WHERE
  LastName LIKE '%son';


SELECT
  LastName, FirstName
FROM
  customers
WHERE
  FirstName LIKE '___a';


SELECT
  TrackId, Name, Bytes
FROM
  tracks
ORDER BY
  Bytes DESC
LIMIT 7;


SELECT
  TrackId, Name, Bytes
FROM
  tracks
ORDER BY
  Bytes DESC
LIMIT 4 OFFSET 3;


-- 04. Grouping data
-- SELECT 
--   c1, c2,..., cn, aggregate_function(ci)
-- FROM
--   table_name
-- GROUP BY 
--   c1, c2, ..., cn;

SELECT
  Country
FROM
  customers
GROUP BY
  Country;


SELECT
  Country, count(*)
FROM
  customers
GROUP BY
  Country;


SELECT 
  Composer, 
  AVG(Bytes) AS avgOfBytes
FROM 
  tracks
GROUP BY
  Composer
ORDER BY  
  avgOfBytes DESC;


SELECT
  Composer,
  AVG(Milliseconds / 60000) AS avgOfMinute
FROM
  tracks
HAVING
  avgOfMinute < 10
ORDER BY
  Composer


-- 에러
SELECT
  Composer,
  AVG(Milliseconds / 60000) AS avgOfMinute
FROM
  tracks
WHERE 
  avgOfMinute < 10
GROUP BY
  Composer;

-- 에러 해결
