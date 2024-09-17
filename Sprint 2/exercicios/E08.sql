SELECT
    v.cdvdd,
    v.nmvdd
FROM
    tbvendedor v
JOIN
    tbvendas vd ON v.cdvdd = vd.cdvdd
WHERE
    vd.status = 'Concluído'
GROUP BY
    v.cdvdd, v.nmvdd
ORDER BY
    COUNT(vd.cdven) DESC
LIMIT 1;
