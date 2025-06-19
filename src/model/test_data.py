import gender_guesser.detector as gender
import pandas as pd
from transform_sheet import transform_data


def test_data(df_rh):
    # # Detector de gênero
    # detector = gender.Detector()

    # # Verificando o sexo dos funcionários por aproximação de gênero do nome
    # df_rh['Genero Inferido'] = df_rh['Nome Completo'].apply(
    #     lambda nome: (
    #         'M' if detector.get_gender(str(nome).split()[0]) in ['male', 'mostly_male']
    #         else 'F' if detector.get_gender(str(nome).split()[0]) in ['female', 'mostly_female']
    #         else 'N/A'
    #     )
    # )

    # # Verifica se a coluna ID RH está em ordem crescente de 1 até o número de linhas
    # eh_ordenado = df_rh['ID RH'].equals(pd.Series(range(1, len(df_rh) + 1)))

    # if eh_ordenado:
    #     print("A coluna 'ID RH' está ordenada corretamente.")
    # else:
    #     print("A coluna 'ID RH' NÃO está ordenada corretamente.")

    # # Método para mostrar todas as linhas do dataframe ao printar na tela
    # pd.set_option('display.max_rows', None)

    # quantidade_enderecos_distintos = df_rh['Endereço'].nunique()

    # print(f"Existem {quantidade_enderecos_distintos} endereços distintos.")

    print(df_rh['Endereço'].head(10))
    
if __name__ == "__main__":
    df = transform_data()
    test_data(df)
    
