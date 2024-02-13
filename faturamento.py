import json

def calcular_estatisticas_faturamento(json_data):
    # Extrair o faturamento diário
    faturamento_diario = [registro['valor'] for registro in json_data if registro['valor'] > 0]
    
    # Verificar se há faturamento no mês
    if not faturamento_diario:
        return None, None, 0  # Retorna None para menor e maior se não houver faturamento
    
    # Calculando o menor e o maior valor de faturamento diário
    menor_faturamento = min(faturamento_diario)
    maior_faturamento = max(faturamento_diario)
    
    # Calculando a média mensal de faturamento (ignorando dias sem faturamento)
    media_mensal = sum(faturamento_diario) / len(faturamento_diario)
    
    # Calculando o número de dias em que o valor de faturamento diário foi superior à média mensal
    dias_acima_da_media = sum(1 for valor in faturamento_diario if valor > media_mensal)
    
    return menor_faturamento, maior_faturamento, dias_acima_da_media

# Carregar dados do arquivo JSON
with open("dados.json", "r") as file:
    dados_faturamento = json.load(file)

# Calculando estatísticas
menor, maior, acima_media = calcular_estatisticas_faturamento(dados_faturamento)

# Exibir resultados
print("Menor valor de faturamento diário:", menor)
print("Maior valor de faturamento diário:", maior)
print("Número de dias no mês em que o valor de faturamento diário foi superior à média mensal:", acima_media)
