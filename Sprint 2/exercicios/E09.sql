SELECT
    v.cdpro,
    v.nmpro
FROM
    tbvendas v
WHERE
    v.dtven BETWEEN '2014-02-03' AND '2018-02-02'
    AND v.status = 'Concluído'
GROUP BY
    v.cdpro, v.nmpro
ORDER BY
    SUM(v.qtd) DESC
LIMIT 1;
