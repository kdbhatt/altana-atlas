# Atlas-API

This project is a collection of APIs that make up the Atlas API.

## Prerequisites
There are a few prerequisites to running this code:

Python 3.7+
Pip3
pyenv and poetry

If this is a new system, ensure that Python 3.7 is set to prevent conflicts:
pyenv install 3.7.5
pyenv global 3.7.5

Whenever the pyproject updated need to update the portry.
`
poetry install  # one time
poetry update
`

### Install poetry:
Run below command and follow directions from output

`curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_VERSION=1.0.10 python` 

### Install Sqlite

On macOS, don’t need to do anything to install sqlite. It’s preinstalled in all modern versions of macOS.
Just need to do is to open a terminal and run the below command:

`sqlite3`


## Import Data file

The raw data will be stored into the Sqlite data store. To import the raw data need to run below comamnd.

`cd ~/atlas
sh db_import.sh`

It will take few min to min all the data. Run below query to confirm the load.
`select count(*) from ReceitaFederal_QuadroSocietario;`
The result will be (17.7m~):
`17,780,860`

## Run API

To run the API Locally, here is the command:

`uvicorn main:app --reload`

Hit the API using web browser or Postman.

## Swagger UI
For API documentation use swagger UI with below URI:

`http://localhost:8000/docs`


![The cloud Architecture of the API](/atlas-api/docs/cloud.jpg "Text to show on mouseover")