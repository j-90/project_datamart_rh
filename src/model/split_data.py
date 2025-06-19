import pandas as pd



def print_columns(df_rh):
    print(df_rh.columns)

def split(df_rh):
    # Criando a dimensão de funcionários
    dim_funcionarios = df_rh[['id_funcionario', 'nome_completo', 'estado_civil', 'sexo', 'data_de_nascimento']].copy()
    
    #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------    
    
    # Criando a dimensão de escritórios
    dim_escritorios = df_rh[['endereco', 'complemento', 'bairro']].copy()
    dim_escritorios['id_escritorio'] = pd.factorize(df_rh['endereco'])[0] + 1
    
    # Criando a dimensão de cidades e a coluna ID Cidade
    dim_cidades = df_rh[['cidade', 'estado', 'cep']].drop_duplicates().reset_index(drop=True)
    dim_cidades['id_cidade'] = dim_cidades.index + 1
    
    # Criando o dataframe auxiliar para fazer um merge entre a dimensão de escritórios e a dimensão de cidades
    df_aux_e = df_rh[['endereco', 'cidade', 'estado', 'cep']].drop_duplicates()
    dim_escritorios = dim_escritorios.merge(df_aux_e, on='endereco', how='left')

    # Inserindo a coluna ID Cidade à dimensão de escritórios
    dim_escritorios = dim_escritorios.merge(dim_cidades, on=['cidade', 'estado', 'cep'], how='left')
    
    # Criando a estrutura final das dimensões de cidades e escritórios
    dim_escritorios = dim_escritorios[['id_escritorio', 'endereco', 'bairro', 'complemento', 'cep', 'id_cidade']].drop_duplicates()
    dim_cidades = dim_cidades[['id_cidade', 'cidade', 'estado']].drop_duplicates()
    
    #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------    
    
    # Criando a dimensão de cargos e a coluna ID Cargo
    dim_cargos = df_rh[['cargo']].copy()
    dim_cargos['id_cargo'] = pd.factorize(df_rh['cargo'])[0] + 1
    
    # Criando a dimensão de área e a coluna ID Área
    dim_area = df_rh[['area']].drop_duplicates().reset_index(drop=True)
    dim_area['id_area'] = dim_area.index + 1
    
    # Criando a dimensão de Nível e a coluna ID Nível
    dim_nivel = df_rh[['nivel']].drop_duplicates().reset_index(drop=True)
    nivel_id = {
        'Estagiário':1,
        'Analista':2,
        'Coordenador':3,
        'Gerente':4,
        'Diretor':5
    }
    dim_nivel['id_nivel'] = dim_nivel['nivel'].map(nivel_id)
    
    # Criando o dataframe auxiliar para fazer um merge com as dimensões de nível e área
    df_aux_c = df_rh[['cargo', 'area', 'nivel']].drop_duplicates()
    df_aux_c = df_aux_c.merge(dim_area, on='area', how='left')
    df_aux_c = df_aux_c.merge(dim_nivel, on='nivel', how='left')
    
    # Inserindo a coluna ID Área e ID Nível à dimensão de cargos usando o dataframe auxiliar
    dim_cargos = dim_cargos.merge(df_aux_c[['cargo', 'id_area', 'id_nivel']], on='cargo', how='left')
    
    # Criando a estrutura final da dimensão de cargos
    dim_cargos = dim_cargos[['id_cargo', 'cargo', 'id_area', 'id_nivel']].drop_duplicates()
    
    #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    # Criando a dimensão de Desempenho
    dim_desempenho = df_rh[['id_funcionario','avaliacao_do_funcionario', 'trabalho_em_equipe', 'lideranca', 'comunicacao', 'iniciativa', 'organizacao']].copy()
    
    # Criando a dimensão de Remuneração
    dim_remuneracao = df_rh[['id_funcionario', 'salario_base', 'impostos', 'beneficios', 'vt', 'vr']].copy()
    
    #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    # Criando a dimensão de Emprego
    dim_emprego = df_rh[['id_funcionario', 'data_de_contratacao', 'data_de_demissao', 'status', 'ferias_acumuladas', 'horas_extras']].copy()
    
    # Criando um dataframe auxiliar para fazer um merge com as dimensões de cargos e escritórios
    df_aux_emp = df_rh[['id_funcionario', 'cargo', 'endereco']].drop_duplicates()
    df_aux_emp = df_aux_emp.merge(dim_cargos, on='cargo', how='left')
    df_aux_emp = df_aux_emp.merge(dim_escritorios, on='endereco', how='left')
    
    # Inserindo a coluna ID Escritório e ID Cargo à dimensão de empregos usando o dataframe auxiliar
    dim_emprego = dim_emprego.merge(df_aux_emp[['id_funcionario', 'id_cargo', 'id_escritorio']], on='id_funcionario', how='left')
    dim_emprego = dim_emprego[['id_funcionario', 'data_de_contratacao', 'data_de_demissao', 'status', 'ferias_acumuladas', 'horas_extras', 'id_cargo', 'id_escritorio']].drop_duplicates()
    
    return dim_funcionarios, dim_escritorios, dim_cidades, dim_cargos, dim_area, dim_nivel, dim_desempenho, dim_remuneracao, dim_emprego

