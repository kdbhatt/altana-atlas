#!/bin/bash

# Shell script to load the raw file

# drop existing table
sqlite3 atlas_db.sqlite  "Drop Table If Exists ReceitaFederal_QuadroSocietario;"

# Create schema
sqlite3 atlas_db.sqlite "create table ReceitaFederal_QuadroSocietario (nr_cnpj text, nm_fantasia text, sg_uf text, in_cpf_cnpj INTEGER, nr_cpf_cnpj_socio INTEGER,	cd_qualificacao_socio INTEGER,	ds_qualificacao_socio text,	nm_socio text);"

#Import tab (\t) delimited data by skipping header record
sqlite3 atlas_db.sqlite ".separator \t " ".import --skip 1 ReceitaFederal_QuadroSocietario.csv ReceitaFederal_QuadroSocietario"
