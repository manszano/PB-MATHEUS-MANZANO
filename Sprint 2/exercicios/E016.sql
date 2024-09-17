SELECT
    v.estado,
    v.nmpro,
    ROUND(AVG(v.qtd), 4) AS quantidade_media
FROM
    tbvendas v
WHERE
    v.status = 'Concluído'
GROUP BY
    v.estado, v.nmpro
ORDER BY
    v.estado ASC,
    v.nmpro ASC;
