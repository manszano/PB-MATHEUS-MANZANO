SELECT DISTINCT autor.nome
FROM autor
JOIN livro ON autor.codautor = livro.autor
JOIN editora ON livro.editora = editora.codeditora
JOIN endereco ON editora.endereco = endereco.codendereco
WHERE endereco.estado NOT IN ('RIO GRANDE DO SUL', 'PARANÁ')
ORDER BY autor.nome ASC;
