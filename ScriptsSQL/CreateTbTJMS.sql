use dbSCRAPING
go


create table tbTJMS
(
	ID				int identity not null,
	no_processo		varchar(25) not null,
	nome_parte		varchar(200) not null, 
	adv_parte		varchar(200) not null default '',
	nome_reu		varchar(200) not null, 
	adv_reu			varchar(200) not null default '',
	dt_andamento	datetime not null, 
	desc_andamento	varchar(8000) not null,
	nome_anexo		varchar(200) null, 
	cont_anexo		varbinary(max)  null

)
go