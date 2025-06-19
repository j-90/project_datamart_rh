import pandas as pd
import re
from unidecode import unidecode



def transform_data():
    base_rh = r'D:\Projeto\ETL_Python\ETL_RH\BaseFuncionarios.xlsx'
    
    # Transformando a base de dados em dataframe
    df_rh = pd.read_excel(base_rh)

    # Corrigindo a contagem dos IDs na coluna ID RH
    df_rh['ID RH'] = range(1, len(df_rh) + 1)
    df_rh = df_rh.rename(columns={'ID RH':'id_funcionario'})
    
    # Separando a coluna de Endereço nas colunas "Bairro", "Cidade", "Estado" e "CEP"
    df_rh[['Complemento', 'Bairro', 'Cidade', 'Estado', 'CEP']] = df_rh['Endereço'].str.extract(
    r'^(?:.*?,\s*[\d.]+)\s*-\s*(.*?)\s*-\s*([^,]+),\s*([^,]+)\s*-\s*([A-Z]{2}),\s*(\d{5}-\d{3})$'
    )
    
    # Extrair bairro, cidade, estado e CEP, ignorando trecho adicional como 'quadra 2.1'
    df_rh[['Complemento', 'Bairro', 'Cidade', 'Estado', 'CEP']] = df_rh['Endereço'].str.extract(
        r'^(?:.*?,\s*(?:\d+\.\d+|\d+-\d+|\d+))\s*-\s*(?:(.+?)\s*-\s*)?([^,]+),\s*([^,]+)\s*-\s*([A-Z]{2}),\s*(\d{5}-\d{3})$'
    )

    # Preencher valores nulos (endereços que não seguem o formato) com vazio
    df_rh[['Complemento', 'Bairro', 'Cidade', 'Estado', 'CEP']] = df_rh[['Complemento', 'Bairro', 'Cidade', 'Estado', 'CEP']].fillna('')

    # Atualizar a coluna 'Endereço' para conter apenas rua e número
    df_rh['Endereço'] = df_rh['Endereço'].str.extract(r'^(.*?,\s*(?:\d+\.\d+|\d+-\d+|\d+))')[0]
    
    # Inserindo o status atual do empregado baseado na coluna Data de Demissao
    df_rh['Status'] = df_rh['Data de Demissao'].apply(lambda x: 'Funcionário demitido' if pd.isna(x) == False else 'Funcionário ativo')

    # Corrigindo o sexo cadastrado das funcionárias de nome Rachel Ferreira e Raquel Tavares
    if 'Nome Completo' in df_rh.columns:
        df_rh.loc[df_rh['Nome Completo'] == 'Rachel Ferreira', 'Sexo'] = 'F'
        df_rh.loc[df_rh['Nome Completo'] == 'Raquel Tavares', 'Sexo'] = 'F'
    
    # Deletando a coluna de imagens
    df_rh = df_rh.drop(['Imagem'], axis=1)
    
    # Tratando os valores nulos nas colunas de data
    df_rh['Data de Demissao'] = df_rh['Data de Demissao'].where(pd.notna(df_rh['Data de Demissao']), None)
    
    new_columns = {}
    
    for col in df_rh.columns:
        # Remove acentos e converte para minúsculas
        new_col = unidecode(col).lower()
        
        # Substitui espaços por underscores
        new_col = new_col.replace(' ', '_')
        new_columns[col] = new_col
    
    # Renomeia as colunas no DataFrame
    df_rh = df_rh.rename(columns=new_columns)
    print(df_rh.columns)
    
    # Transformando a letra C e a letra S na coluna de estado civil para Casado e Solteiro, respectivamente
    df_rh['estado_civil'] = df_rh['estado_civil'].replace({'C': 'Casado', 'S': 'Solteiro'})

    for col in df_rh.columns:
        if col in df_rh.columns and df_rh[col].dtype in ['float64', 'int64']:
            df_rh[col] = df_rh[col].round(2)
    
    return df_rh

