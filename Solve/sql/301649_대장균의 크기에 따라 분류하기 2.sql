SELECT ID, (CASE
                WHEN a.PER <= 0.25 THEN 'CRITICAL'
                WHEN a.PER <= 0.5 THEN 'HIGH'
                WHEN a.PER <= 0.75 THEN 'MEDIUM'
                ELSE 'LOW'
            END) COLONY_NAME
FROM (
    -- 각 대장균 군집 크기의 백분위수를 내림차순으로 계산하는 서브쿼리
    SELECT ID, PERCENT_RANK() OVER (ORDER BY SIZE_OF_COLONY DESC) PER
    FROM ECOLI_DATA
) a
ORDER BY ID;