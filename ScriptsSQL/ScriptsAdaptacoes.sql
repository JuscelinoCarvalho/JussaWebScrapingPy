--
select * from tbDIARIO_OFICIAL WHERE nome_arquivo = 'concorrencia-publica-n0-0062019-processo-licitatorio-n0-1632019'

select LOWER( replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(replace([desc_publicacao],'Cidade: TR�S LAGOAS', ''),' ','-'),'/',''), '�', 'o'),'�','a'),'�','e'), '�', 'i'), '�', 'o'), '�', 'u'), '�', 'o'), '�', 'c'), '�', 'a'), '�', 'o') ) from tbDIARIO_OFICIAL

select ASCII('�')
select ASCII('�')

update tbDIARIO_OFICIAL
set nome_arquivo = LOWER(replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(replace([desc_publicacao],'Cidade: TR�S LAGOAS', ''), ',',''),' ','-'),'/',''), '�', 'o'),'�','a'),'�','e'),'�','e'),'�', 'i'), '�', 'o'), '�', 'u'), '�', '0'), '�', 'c'), '�', 'a'), '�', 'o'), '�','a'), '�','e'), '�', 'i'), '�', 'o'), '�', 'u'), '�', 'c'), '�', 'a'), '�', 'o'), '.',''), ':','')) 


select *
from tbDIARIO_OFICIAL
    

select char(176)
select char(186)

alter table tbDIARIO_OFICIAL alter column nome_arquivo varchar(max) not null
alter table tbDIARIO_OFICIAL alter column nome_arquivo varchar(2000) not null
