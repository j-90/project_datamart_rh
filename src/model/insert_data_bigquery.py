import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account
from pandas_gbq import to_gbq



def insert_data(dim_funcionarios, dim_escritorios, dim_cidades, dim_cargos, dim_area, dim_nivel, dim_desempenho, dim_remuneracao, dim_emprego):
    # Especificando o caminho onde as credenciais, no arquivo json, estão armazenadas
    credencial_path = r'D:\Projeto\ETL_Python\ETL_RH\dm-rh-457714-9a2edc8453de.json'
    
    # Carregando as credenciais
    credentials = service_account.Credentials.from_service_account_file(credencial_path)
    
    # Definindo o ID do projeto e dataset
    projeto = "dm-rh-457714"
    dataset = "DM_RH"
    
    # Inserindo dados em cada tabela do BigQuery
    # dim_funcionarios.to_gbq(f'{dataset}.dim_funcionarios', project_id=projeto, if_exists='append', credentials=credentials)
    dim_funcionarios.to_gbq(f'{dataset}.dim_funcionarios', project_id=projeto, if_exists='replace', credentials=credentials)
    
    # dim_escritorios.to_gbq(f'{dataset}.dim_escritorios', project_id=projeto, if_exists='append', credentials=credentials)
    dim_escritorios.to_gbq(f'{dataset}.dim_escritorios', project_id=projeto, if_exists='replace', credentials=credentials)
    
    # dim_cidades.to_gbq(f'{dataset}.dim_cidades', project_id=projeto, if_exists='append', credentials=credentials)
    dim_cidades.to_gbq(f'{dataset}.dim_cidades', project_id=projeto, if_exists='replace', credentials=credentials)
    
    # dim_cargos.to_gbq(f'{dataset}.dim_cargos', project_id=projeto, if_exists='append', credentials=credentials)
    dim_cargos.to_gbq(f'{dataset}.dim_cargos', project_id=projeto, if_exists='replace', credentials=credentials)
    
    # dim_area.to_gbq(f'{dataset}.dim_area', project_id=projeto, if_exists='append', credentials=credentials)
    dim_area.to_gbq(f'{dataset}.dim_area', project_id=projeto, if_exists='replace', credentials=credentials)
    
    # dim_nivel.to_gbq(f'{dataset}.dim_nivel', project_id=projeto, if_exists='append', credentials=credentials)
    dim_nivel.to_gbq(f'{dataset}.dim_nivel', project_id=projeto, if_exists='replace', credentials=credentials)
    
    # dim_desempenho.to_gbq(f'{dataset}.dim_desempenho', project_id=projeto, if_exists='append', credentials=credentials)
    dim_desempenho.to_gbq(f'{dataset}.dim_desempenho', project_id=projeto, if_exists='replace', credentials=credentials)
    
    # dim_remuneracao.to_gbq(f'{dataset}.dim_remuneracao', project_id=projeto, if_exists='append', credentials=credentials)
    dim_remuneracao.to_gbq(f'{dataset}.dim_remuneracao', project_id=projeto, if_exists='replace', credentials=credentials)
    
    # dim_emprego.to_gbq(f'{dataset}.dim_emprego', project_id=projeto, if_exists='append', credentials=credentials)
    dim_emprego.to_gbq(f'{dataset}.dim_emprego', project_id=projeto, if_exists='replace', credentials=credentials)


# if __name__ == "__main__":
#     df = transform_data()
#     dim_funcionarios, dim_escritorios, dim_cidades, dim_cargos, dim_area, dim_nivel, dim_desempenho, dim_remuneracao, dim_emprego = split(df)
#     insert_data(dim_funcionarios, dim_escritorios, dim_cidades, dim_cargos, dim_area, dim_nivel, dim_desempenho, dim_remuneracao, dim_emprego)
    
