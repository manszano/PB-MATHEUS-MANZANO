WITH VendedorVendas AS (
    SELECT 
        vd.cdvdd,
        SUM(v.qtd * v.vrunt) AS valor_total_vendas
    FROM 
        tbvendas v
    JOIN 
        tbvendedor vd ON v.cdvdd = vd.cdvdd
    WHERE 
        v.status = 'Concluído'
    GROUP BY 
        vd.cdvdd
    HAVING 
        valor_total_vendas > 0
    ORDER BY 
        valor_total_vendas ASC
    LIMIT 1
)
SELECT 
    d.cddep,
    d.nmdep,
    d.dtnasc,
    vv.valor_total_vendas
FROM 
    tbdependente d
JOIN 
    VendedorVendas vv ON d.cdvdd = vv.cdvdd
ORDER BY 
    d.nmdep;
