from fastapi import FastAPI
from databases import Database

app = FastAPI()

database = Database("sqlite:///atlas_db.sqlite")


@app.on_event("startup")
async def database_connect():
    await database.connect()


@app.on_event("shutdown")
async def database_disconnect():
    await database.disconnect()


@app.get('/operators')
async def get_all_operators(company_id: str):
    """
    All operators associated with a given company
    :param company_id:
    :return: List of operators
    """
    query = f"SELECT distinct nm_socio FROM ReceitaFederal_QuadroSocietario where nr_cnpj = {company_id}"
    results = await database.fetch_all(query=query)
    operators = []
    for result in results:
        operators.append(result['nm_socio'])

    return operators


@app.get('/companies')
async def get_all_operators(operator: str):
    """
    All companies associated with a given operator
    :param operator:
    :return: List of company name
    """
    query = f"SELECT nm_fantasia FROM ReceitaFederal_QuadroSocietario where [nm_socio]= {operator}"
    results = await database.fetch_all(query=query)
    companies = []
    for result in results:
        companies.append(result['nm_fantasia'])

    return companies


@app.get('/shared_companies')
async def get_all_operators(company_id: str):
    """
    All companies connected to a given company via shared operators
    :param company_id:
    :return: List of company name
    """
    query = f"select distinct nm_fantasia from ReceitaFederal_QuadroSocietario where [nm_socio] in (SELECT distinct nm_socio FROM ReceitaFederal_QuadroSocietario where nr_cnpj={company_id})"
    results = await database.fetch_all(query=query)
    companies = []
    for result in results:
        companies.append(result['nm_fantasia'])

    return companies
