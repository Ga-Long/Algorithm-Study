-- 코드를 입력하세요
SELECT RI.REST_ID, REST_NAME, FOOD_TYPE, FAVORITES, 
ADDRESS, ROUND(AVG(REVIEW_SCORE),2) AS SCORE
FROM REST_INFO RI
INNER JOIN REST_REVIEW RR ON RI.REST_ID = RR.REST_ID
GROUP BY RI.REST_ID
HAVING RI.ADDRESS like '서울%'
ORDER BY SCORE DESC, RI.FAVORITES DESC
