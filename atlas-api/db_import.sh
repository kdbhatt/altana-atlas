#!/bin/bash

sqlite3 atlas_db.sqlite  "Drop Table If Exists ReceitaFederal_QuadroSocietario;"
sqlite3 atlas_db.sqlite "create table ReceitaFederal_QuadroSocietario (nr_cnpj text, nm_fantasia text, sg_uf text, in_cpf_cnpj text, nr_cpf_cnpj_socio text,	cd_qualificacao_socio text,	ds_qualificacao_socio text,	nm_socio text);"
sqlite3 atlas_db.sqlite ".separator \t " ".import --skip 1 ReceitaFederal_QuadroSocietario.csv ReceitaFederal_QuadroSocietario"
