from src.model.transform_sheet import transform_data
from src.model.split_data import split
from src.model.insert_data_bigquery import insert_data


def pipeline():
    df_rh = transform_data()
    dim_funcionarios, dim_escritorios, dim_cidades, dim_cargos, dim_area, dim_nivel, dim_desempenho, dim_remuneracao, dim_emprego = split(df_rh)
    insert_data(dim_funcionarios, dim_escritorios, dim_cidades, dim_cargos, dim_area, dim_nivel, dim_desempenho, dim_remuneracao, dim_emprego)
    
    # return df_rh

