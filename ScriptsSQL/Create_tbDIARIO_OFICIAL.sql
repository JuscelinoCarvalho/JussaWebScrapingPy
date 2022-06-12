use dbDIARIO_OFICIAL
go

create table tbDIARIO_OFICIAL
(
	ID bigint identity not null,
	dt_publicacao datetime not null, 
	desc_publicacao varchar(2000) not null,
	conteudo_publicacao varchar(max) not null,
	 

)
go

