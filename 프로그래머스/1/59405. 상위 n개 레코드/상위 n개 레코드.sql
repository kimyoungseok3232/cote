-- 코드를 입력하세요
-- 데이터에서 가장 작은 DATETIME 값 탐색 후 해당 값과 동일한 데이터 찾아 NAME 확인
-- 데이터 비교에서 오버헤드 발생, 가장 작은 값이 여러 개인 경우 여러 NAME 반환 가능
-- SELECT NAME
-- FROM ANIMAL_INS
-- WHERE DATETIME = (SELECT MIN(DATETIME) FROM ANIMAL_INS)

-- 데이터 정렬 후 가장 위에서 부터 N개 가져옴
-- 원하는 갯수만큼만 가져옴
-- DATETIME에 인덱스가 존재하는 경우 더 빠름
-- 일부 LIMIT 지원하지 않는 DBMS에서는 사용 어려움
-- 인덱스 없는 경우 성능 저하
SELECT NAME
FROM ANIMAL_INS
ORDER BY DATETIME ASC
LIMIT 1
