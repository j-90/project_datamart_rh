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

**Nota**: O arquivo de credenciais do Google BigQuery (`*.json`) não deve ser incluído neste repositório por razões de segurança. Configure-o localmente conforme descrito na seção "Pré-requisitos".

## Pré-requisitos

Antes de executar o projeto, instale as dependências necessárias:

```bash
pip install pandas google-cloud-bigquery pandas-gbq unidecode
```

### Configuração do Google BigQuery
1. Crie um projeto no Google Cloud e ative a API BigQuery.
2. Gere um arquivo de credenciais JSON no Google Cloud Console e salve-o localmente (ex.: `credentials.json`).
3. Configure a variável de ambiente `GOOGLE_APPLICATION_CREDENTIALS` para o caminho do arquivo JSON antes de executar o script:
   ```bash
   set GOOGLE_APPLICATION_CREDENTIALS=caminho/para/seu/credentials.json  # Windows
   export GOOGLE_APPLICATION_CREDENTIALS=caminho/para/seu/credentials.json  # Linux/Mac
   ```
4. Ajuste o código em `insert_data_bigquery.py` para usar a variável de ambiente, se necessário (veja a seção "Contribuindo" para detalhes).

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
  - Corrige IDs, separa endereços em componentes (bairro, cidade, estado, CEP).
  - Ajusta sexo e estado civil com base em regras específicas.
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

## Contribuindo

Sinta-se à vontade para contribuir! Siga estas etapas:
1. Faça um fork do repositório.
2. Crie uma branch para sua feature: `git checkout -b feature/nova-funcionalidade`.
3. Commit suas alterações: `git commit -m "Descrição da mudança"`.
4. Envie para o repositório: `git push origin feature/nova-funcionalidade`.
5. Abra um Pull Request.

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

- **Autor**: [Seu Nome ou Usuário do GitHub](https://github.com/seu-usuario)
- **Email**: seu-email@example.com (opcional)
- **Data de Criação**: 07/06/2025 às 11:08 AM -03

## Histórico de Versões

- **v1.0.0** (07/06/2025): Versão inicial com pipeline ETL funcional.

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

---

### Instruções para Uso no GitHub
1. **Crie o Arquivo**:
   - Copie o conteúdo acima e salve como `README.md` na raiz do diretório `ETL_RH`.

2. **Adicione ao Repositório**:
   - Certifique-se de que `dm-rh-457714-92e2dc843d3e.json` está no `.gitignore` (ex.: adicione `*.json` se ainda não estiver lá).
   - Commit e envie ao GitHub:
     ```bash
     cd d:\Projeto\ETL_Python\ETL_RH
     git add README.md
     git commit -m "Adicionando README detalhado"
     git push origin main
     ```

3. **Ajustes no Código**:
   - Atualize `insert_data_bigquery.py` para usar a variável de ambiente, conforme sugerido na seção "Contribuindo".
   - Substitua `"dm-rh-457714"` pelo seu ID de projeto real no código, se necessário.

4. **Imagens (Opcional)**:
   - Se desejar adicionar as imagens sugeridas anteriormente (`project_structure.png`, `bigquery_result.png`, `sample_excel.png`), siga as instruções que forneci e insira-as no README com:
     ```markdown
     ![Estrutura do Projeto](project_structure.png)
     ![Resultado no BigQuery](bigquery_result.png)
     ![Exemplo de Dados do Excel](sample_excel.png)
     ```
   - Certifique-se de que as imagens não exponham dados sensíveis.

---

### Observações de Segurança
- O README não menciona caminhos ou nomes específicos de credenciais, mantendo a segurança.
- Instruções genéricas guiam os usuários a configurar suas próprias credenciais localmente.
- Adicione um arquivo `LICENSE` com a licença MIT, se desejar, para formalizar a distribuição.

Se precisar de ajuda para ajustar o código, adicionar imagens ou subir o repositório, é só me chamar!