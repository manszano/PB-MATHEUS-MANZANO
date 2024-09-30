SELECT COUNT(livro.cod) AS quantidade, editora.nome, endereco.estado, endereco.cidade
FROM livro
JOIN editora ON livro.editora = editora.codeditora
JOIN endereco ON editora.endereco = endereco.codendereco
GROUP BY editora.codeditora, editora.nome, endereco.estado, endereco.cidade
ORDER BY quantidade DESC
LIMIT 5;
