SELECT
    v.cdven
FROM
    tbvendas v
WHERE
    v.deletado = '1'
ORDER BY
    v.cdven ASC;
