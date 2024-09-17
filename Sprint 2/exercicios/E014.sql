SELECT
    v.estado,
    ROUND(AVG(v.qtd * v.vrunt), 2) AS gastomedio
FROM
    tbvendas v
WHERE
    v.status = 'Concluído'
GROUP BY
    v.estado
ORDER BY
    gastomedio DESC;
