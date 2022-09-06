# with tab as (select num, dense_rank()
# over( order by num asc) as rnk
# from Logs)
# select distinct num from
# tab,Logs
# where count(rnk) =3

SELECT DISTINCT
    l1.Num AS ConsecutiveNums
FROM
    Logs l1,
    Logs l2,
    Logs l3
WHERE
    l1.Id = l2.Id - 1
    AND l2.Id = l3.Id - 1
    AND l1.Num = l2.Num
    AND l2.Num = l3.Num
;