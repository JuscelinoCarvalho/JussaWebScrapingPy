--
select * from tbDIARIO_OFICIAL WHERE nome_arquivo = 'concorrencia-publica-n0-0062019-processo-licitatorio-n0-1632019'

select LOWER( replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(replace([desc_publicacao],'Cidade: TRÊS LAGOAS', ''),' ','-'),'/',''), 'º', 'o'),'á','a'),'é','e'), 'í', 'i'), 'ó', 'o'), 'ú', 'u'), '°', 'o'), 'ç', 'c'), 'ã', 'a'), 'õ', 'o') ) from tbDIARIO_OFICIAL

select ASCII('º')
select ASCII('°')

update tbDIARIO_OFICIAL
set nome_arquivo = LOWER(replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(replace([desc_publicacao],'Cidade: TRÊS LAGOAS', ''), ',',''),' ','-'),'/',''), '°', 'o'),'á','a'),'é','e'),'ê','e'),'í', 'i'), 'ó', 'o'), 'ú', 'u'), 'º', '0'), 'ç', 'c'), 'ã', 'a'), 'õ', 'o'), 'Á','a'), 'É','e'), 'Í', 'i'), 'Ó', 'o'), 'Ú', 'u'), 'Ç', 'c'), 'Ã', 'a'), 'Õ', 'o'), '.',''), ':','')) 


select *
from tbDIARIO_OFICIAL
    

select char(176)
select char(186)

alter table tbDIARIO_OFICIAL alter column nome_arquivo varchar(max) not null
alter table tbDIARIO_OFICIAL alter column nome_arquivo varchar(2000) not null
