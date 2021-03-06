# Atlas-API

This project is a collection of APIs that make up the Atlas API.

## Prerequisites
There are a few prerequisites to running this code:

`Python 3.7+`\
`Pip3`\
`pyenv and poetry`


If this is a new system, ensure that Python 3.7 is set to prevent conflicts:\

`pyenv install 3.7.5` \
`pyenv global 3.7.5`

### Install poetry:
Run below command and follow directions from output

`curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_VERSION=1.0.10 python` 

Whenever the pyproject updated need to update the portry.\
`poetry install  # one time`\
`poetry update
`

### Install Sqlite

On macOS, don’t need to do anything to install sqlite. It’s preinstalled in all modern versions of macOS.
Just need to do is to open a terminal and run the below command:

`sqlite3`

For widows need to install `sqlite3`. Follow below link to install it.

`https://www.sqlitetutorial.net/download-install-sqlite/
`
## Import Data file

The raw data will be stored into the Sqlite data store. To import the raw data need to run below comamnd.
\
`cd ~/atlas` \
`sh db_import.sh` 

It will take few min to load all the data. Run below query to confirm the load.

`select count(*) from ReceitaFederal_QuadroSocietario;`\
`17,780,860 Records`

The result will be (17.7m~) Records.


### Data Dictionary

| Field Name | DataType | Description |
| --- | ----------- |-----------------
|nr_cnpj|TEXT|Company’s registration ID (Used as a string, so that leading 0 will not trim.)|
|nm_fantasia|TEXT|Company’s name|
|sg_uf|TEXT|Company Location|
|in_cpf_cnpj|INTEGER|business partner -> Company (1) or a Person (2)|
|nr_cpf_cpnj_socio|INTEGER|Business partner registration ID|
|cd_qualificacao_socio|INTEGER|business partner role|
|ds_qualificacao_socio|TEXT|Description of the business partner role|
|nm_socio|TEXT|operator / administrator name|


## Run the application

To run the API Locally, here is the command:

`uvicorn atlas_api.main:app --reload`

Hit the API using web browser or Postman.

Example to access Endpoints:

`
http://localhost:8000/api/v1/app/operators/?company_id='17207979000176'
http://localhost:8000/api/v1/app/shared_companies/?company_id='36863652000105'
http://localhost:8000/api/v1/app/companies/?operator='CHIANG DE GOMES'
`


## Swagger UI
For API documentation swagger UI can be accessed with below URI:

`http://localhost:8000/docs`

## Architecture of the system

![System Design](/docs/Current_Architecture.jpg "architecture")


## Future work
- The folder structure is created so that we can add unit test by using pytest.
- Model can be used by using `Pydentic` to get request and send request, so that response model can be managed.


## High level Architecture to implement in AWS Cloud (**Proposed**)

![The cloud Architecture of the API](/docs/cloud.jpg "Proposed architecture")


## Design Notes:

AWS Lambda can be used to monitor the S3 bucket.\
One the file lands into S3 Lambda will call Glue job and which load data into RDS.\
AWS API Gateway can be used to for API deployment.\
Lambda will pull the data from RDS and send to user who calling APIs.
