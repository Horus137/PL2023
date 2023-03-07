import re

# Cria um dicionário para armazenar as frequências de processos por ano
frequencia_por_ano = {}

# Abre o arquivo 'processos.txt' para leitura
with open('processos.txt', 'r') as arquivo:
    # Itera pelas linhas do arquivo
    for linha in arquivo:
        # Usa regex para obter o ano da linha
        ano = re.search(r'^\d+::(\d{4})', linha)
        if ano:
            # Incrementa a frequência do ano no dicionário
            frequencia_por_ano[ano.group(1)] = frequencia_por_ano.get(ano.group(1), 0) + 1

# Exibe as frequências de processos por ano
for ano, frequencia in frequencia_por_ano.items():
    print(f'Ano {ano}: {frequencia} processos')
