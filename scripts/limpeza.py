import pandas as pd

arquivo = pd.read_csv('dados/vendas.csv', sep=';')

print('\nBASE ORIGINAL\n')

print(arquivo)

print('\n========================')
print('INICIANDO LIMPEZA')
print('========================\n')

duplicados = arquivo.duplicated().sum()

arquivo = arquivo.drop_duplicates()

print(f'Duplicados removidos: {duplicados}')

valores_vazios = arquivo.isnull().sum().sum()

print(f'Valores vazios encontrados: {valores_vazios}')

arquivo['cidade'] = arquivo['cidade'].fillna('Nao informado')

arquivo['cidade'] = arquivo['cidade'].str.title()

valores_negativos = (arquivo['valor'] < 0).sum()

print(f'Valores negativos encontrados: {valores_negativos}')

arquivo.loc[arquivo['valor'] < 0, 'valor'] = 0

arquivo['data'] = pd.to_datetime(arquivo['data'])

arquivo = arquivo.sort_values(by='data')

arquivo.to_csv('dados/vendas_tratadas.csv', index=False)

print('\n========================')
print('BASE TRATADA')
print('========================\n')

print(arquivo)

print('\nArquivo salvo com sucesso')