-- 1. tracks 테이블의 모든 데이터를 조회
SELECT * FROM tracks;

-- 2. Name, Milliseconds, UnitPrice 열의 모든 데이터를 조회
SELECT Name, Milliseconds, UnitPrice FROM tracks;

-- 3. GenreId 값이 1인 모든 데이터를 조회
SELECT * FROM tracks WHERE GenreId = 1;

-- 4. 모든 데이터를 Name 기준으로 오름차순 정렬하여 조회
SELECT * FROM tracks ORDER BY Name ASC;

-- 5. 모든 데이터를 조회하되 10개만 출력
SELECT * FROM tracks LIMIT 10;