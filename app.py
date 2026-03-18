# PROGRAMA: Cálculo de consumo de energia

# Entrada de dados (Informação de usuário)
print("----------------------------------------------------------------------------------")
nome_aparelho = input("Digite o nome do aparelho: ")                        # Entrada do nome do tipo de aparelho
potencia_w = float(input("Digite a potência do aparelho em watts (W): "))   # Valor da potência em watts
horas = float(input("Digite o tempo médio (só o número das horas): "))      # valores de horas

# Processamento (cálculos)
consumo_mensal = (potencia_w * horas) * 30                          # Cálculo do consumo mensal em Wh (watt-hora)
kwh = consumo_mensal / 1000                                         # Conversão para kWh
preco = 0.75                                                        # Valor médio do kWh (R$) atualizado em março de 2026
custo = preco * kwh                                                 # Cálculo do custo total

# Saída de dados (resultados)
print("----------------------------------------------------------------------------------")
print(f"Aparelho: {nome_aparelho}")                                 # Mostra o nome do aparelho
print(f"Consumo estimado: {kwh:.0f} kWh/mês")                       # Consumo sem casas decimais
print("Valor estimado baseado em tarifa média de R$ 0,75/kWh")      # Informação do valor usado
print(f"Custo estimado: R$ {custo:.2f}")                            # Custo com 2 casas decimais
print("----------------------------------------------------------------------------------")