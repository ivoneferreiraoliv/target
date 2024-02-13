# Faturamento mensal por estado
faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# Calculando o total mensal
total_mensal = sum(faturamento.values())

# Calculando o percentual de representação de cada estado
percentuais = {estado: (faturamento[estado] / total_mensal) * 100 for estado in faturamento}

# Imprimindo os percentuais
for estado, percentual in percentuais.items():
    print(f'{estado}: {percentual:.2f}%')
