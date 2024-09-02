#!/bin/bash

diretorio="/home/matheus/ecommerce"

pasta_vendas="$diretorio/vendas"
pasta_backup="$pasta_vendas/backup"
data_agora=$(date +"%Y%m%d")

cp "$diretorio/dados_de_vendas.csv" "$pasta_backup/dados-$data_agora.csv"
mv "$pasta_backup/dados-$data_agora.csv" "$pasta_backup/backup-dados-$data_agora.csv"

{
    echo "data: $(date +"%Y/%m/%d %H:%M")"
    echo "primeiro registro de venda: $(awk -F, 'NR==2 {print $5}' "$pasta_backup/backup-dados-$data_agora.csv")"
    echo "ultimo registro de venda: $(awk -F, 'END {print $5}' "$pasta_backup/backup-dados-$data_agora.csv")"
    echo "total de itens diferentes vendidos: $(awk -F, '{print $2}' "$pasta_backup/backup-dados-$data_agora.csv" | tail -n +2 | sort | uniq | wc -l)"
    echo "Primeiras 10 linhas-$data_agora.csv:"

    head -n 10 "$pasta_backup/backup-dados-$data_agora.csv"
} > "$pasta_backup/relatorio-$data_agora.txt"

zip "$pasta_backup/backup-dados-$data_agora.zip" "$pasta_backup/backup-dados-$data_agora.csv"

# remover dados
rm "$pasta_backup/backup-dados-$data_agora.csv"
rm "$pasta_vendas/dados_de_vendas.csv"

