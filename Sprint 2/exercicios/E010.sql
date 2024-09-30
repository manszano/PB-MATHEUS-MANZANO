SELECT 
    vd.nmvdd AS vendedor,
    SUM(v.qtd * v.vrunt) AS valor_total_vendas,
    ROUND(SUM(v.qtd * v.vrunt) * vd.perccomissao / 100, 2) AS comissao
FROM 
    tbvendas v
JOIN 
    tbvendedor vd ON v.cdvdd = vd.cdvdd
WHERE 
    v.status = 'Concluído'
GROUP BY 
    vd.nmvdd
ORDER BY 
    comissao DESC;
