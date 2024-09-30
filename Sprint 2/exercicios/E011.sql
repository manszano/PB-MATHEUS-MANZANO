SELECT
    v.cdcli,
    v.nmcli,
    SUM(v.qtd * v.vrunt) AS gasto
FROM
    tbvendas v
WHERE
    v.status = 'Concluído'
GROUP BY
    v.cdcli, v.nmcli
ORDER BY
    gasto DESC
LIMIT 1;
