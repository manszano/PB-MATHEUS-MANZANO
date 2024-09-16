diretorio="./vendas/backup"
relatorio="$diretorio/relatorio_final.txt"

cat "$diretorio"/relatorio-*.txt > "$relatorio"
