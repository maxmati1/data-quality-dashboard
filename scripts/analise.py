import pandas as pd

arquivo = pd.read_csv('dados/vendas_tratadas.csv')

print('\n========================')
print('RELATORIO DE ANALISE')
print('========================\n')

total_vendas = arquivo['valor'].sum()

media_vendas = arquivo['valor'].mean()

maior_venda = arquivo['valor'].max()

menor_venda = arquivo['valor'].min()

cidade_top = arquivo['cidade'].value_counts().idxmax()

produto_top = arquivo['produto'].value_counts().idxmax()

print(f'Total vendido: R${total_vendas:.2f}')

print(f'Media das vendas: R${media_vendas:.2f}')

print(f'Maior venda: R${maior_venda:.2f}')

print(f'Menor venda: R${menor_venda:.2f}')

print(f'Cidade com mais vendas: {cidade_top}')

print(f'Produto mais vendido: {produto_top}')