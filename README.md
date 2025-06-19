---

```markdown
# ETL_RH - Pipeline de Extração, Transformação e Carregamento de Dados de Recursos Humanos

Este repositório contém um projeto Python que implementa um pipeline ETL (Extract, Transform, Load) para processar dados de recursos humanos a partir de uma planilha Excel e carregá-los em um banco de dados no Google BigQuery. O projeto organiza os dados em dimensões para análise eficiente, como funcionários, escritórios, cargos e desempenho.

## Descrição do Projeto

O ETL_RH foi desenvolvido para automatizar a transformação e o carregamento de dados de uma base de funcionários em um formato estruturado, adequado para análise de dados. O pipeline realiza as seguintes etapas:
- **Extração**: Lê dados de uma planilha Excel (`BaseFuncionarios.xlsx`).
- **Transformação**: Ajusta colunas, corrige dados, cria IDs únicos e separa informações como endereços em dimensões (bairro, cidade, estado, etc.).
- **Carregamento**: Insere os dados transformados em tabelas no Google BigQuery para armazenamento e análise.

## Estrutura do Projeto

```
ETL_RH/
├── .vscode/                         # Configurações do VS Code
├── src/                             # Diretório principal do código
│   ├── controller/                  # Lógica de controle do pipeline
│   │   └── projeto_rh.py            # Orquestra o pipeline ETL
│   ├── model/                       # Modelos de transformação e carregamento
│   │   ├── insert_data_bigquery.py  # Carrega dados no BigQuery
│   │   ├── split_data.py            # Divide dados em dimensões
│   │   ├── test_data.py             # Testes (opcional)
│   │   ├── transform_sheet.py       # Transforma dados do Excel
│   │   └── __init__.py              # Inicializa o pacote model
│   └── view/                        # Interface ou visualização (atualmente com init.py)
│       └── __init__.py              # Inicializa o pacote view
├── BaseFuncionarios.xlsx            # Arquivo de origem com dados de funcionários
├── BaseFuncionarios_final.xlsx      # Arquivo de saída (opcional, comentado)
├── executa_etl_rh.py                # Script principal para executar o pipeline
├── .gitignore                       # Arquivos ignorados pelo Git
└── README.md                        # Este arquivo
```

**Nota**: O arquivo de credenciais do Google BigQuery (`*.json`) não foi incluído neste repositório por razões de segurança. Configure-o localmente conforme descrito na seção "Pré-requisitos".

## Pré-requisitos

Antes de executar o projeto, instale as dependências necessárias:

```bash
pip install pandas google-cloud-bigquery pandas-gbq unidecode
```

### Configuração do Google BigQuery
1. Crie um projeto no Google Cloud e ative a API BigQuery.
2. Gere um arquivo de credenciais JSON no Google Cloud Console e salve-o localmente (ex.: `credentials.json`).
3. Insira o arquivo JSON gerado na pasta contendo o arquivo principal de execução do script.
4. Ajuste o código em `insert_data_bigquery.py` para usar o arquivo.

## Como Executar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/ETL_RH.git
   cd ETL_RH
   ```

2. Instale as dependências (conforme pré-requisitos acima).

3. Configure as credenciais do BigQuery (conforme instruções acima).

4. Execute o script principal:
   ```bash
   python executa_etl_rh.py
   ```

O script processará o arquivo `BaseFuncionarios.xlsx`, transformará os dados e os carregará nas tabelas do BigQuery no dataset configurado.

## Funcionalidades

- **Transformação de Dados**: 
  - Corrige IDs dos funcionários, separa endereços em componentes (bairro, cidade, estado, CEP).
  - Ajusta sexo e estado civil com base em regras específicas.
  - Insere o status de atividade do funcionário com base na existência de uma data de demissão.
  - Remove a coluna de imagens.
  - Remove acentos e padroniza nomes de colunas.
- **Divisão em Dimensões**: 
  - Cria dimensões como funcionários, escritórios, cidades, cargos, área, nível, desempenho, remuneração e emprego.
- **Carregamento no BigQuery**: 
  - Insere os dados em tabelas separadas no BigQuery, substituindo os dados existentes (opção `replace`).

## Estrutura dos Dados

- **Tabelas no BigQuery**:
  - `dim_funcionarios`
  - `dim_escritorios`
  - `dim_cidades`
  - `dim_cargos`
  - `dim_area`
  - `dim_nivel`
  - `dim_desempenho`
  - `dim_remuneracao`
  - `dim_emprego`

### Ajustes no Código
- Para usar variáveis de ambiente no lugar de caminhos fixos em `insert_data_bigquery.py`, modifique a função `insert_data` para:
  ```python
  import os
  from google.oauth2 import service_account
  from pandas_gbq import to_gbq

  def insert_data(dim_funcionarios, dim_escritorios, dim_cidades, dim_cargos, dim_area, dim_nivel, dim_desempenho, dim_remuneracao, dim_emprego):
      credencial_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
      if not credencial_path:
          raise ValueError("A variável de ambiente GOOGLE_APPLICATION_CREDENTIALS não está configurada.")
      credentials = service_account.Credentials.from_service_account_file(credencial_path)
      projeto = "seu-projeto-id"  # Substitua pelo seu ID de projeto
      dataset = "DM_RH"
      # ... (resto do código com to_gbq)
  ```
- Ajuste o `projeto` no código para corresponder ao seu ID de projeto no Google Cloud.

## Licença

Este projeto está sob a licença [MIT](LICENSE) (adicione um arquivo LICENSE se aplicável).

## Contato

- **Autor**: [Jeferson Andrade - j-90](https://github.com/j-90)
- **Email**: jandrademelo90@gmail.com
- **Data de Criação**: 19/06/2025 às 00:04 AM -03

## Histórico de Versões

- **v1.0.0** (19/06/2025): Versão inicial com pipeline ETL funcional.

## Notas Adicionais

- Certifique-se de que o arquivo `BaseFuncionarios.xlsx` contém as colunas esperadas (e.g., `Nome Completo`, `Endereço`, `Data de Demissao`, etc.).
- O código usa `if_exists='replace'` no BigQuery; ajuste para `append` se desejar adicionar dados sem sobrescrever.
- Testes adicionais podem ser implementados em `test_data.py`.
- Nunca comite arquivos de credenciais (e.g., `*.json`) ao repositório. Adicione-os ao `.gitignore`.

## Links Úteis

- [Documentação do Google BigQuery](https://cloud.google.com/bigquery/docs)
- [pandas](https://pandas.pydata.org/)
- [google-cloud-bigquery](https://cloud.google.com/python/docs/reference/bigquery/latest)
- [pandas-gbq](https://pandas-gbq.readthedocs.io/)
- [unidecode](https://pypi.org/project/Unidecode/)
```
