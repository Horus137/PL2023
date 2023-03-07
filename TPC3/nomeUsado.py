import re

# Frequência de nomes próprios e sobrenomes por século
first_names_freq = {}
last_names_freq = {}

with open('processos.txt', 'r') as f:
    for line in f:
        # Extrai o século
        year = re.findall(r'\d{4}', line)
        if year:
            century = (int(year[0][:2]) + 1) if year[0][2:] != '00' else int(year[0][:2])
        else:
            continue

        # Extrai o primeiro e último nome
        first_name = re.findall(r'[A-Z][a-z]*', line)
        last_name = re.findall(r'[A-Z][a-z]*$', line)

        if first_name:
            # Atualiza a frequência do nome próprio
            if century in first_names_freq:
                if first_name[0] in first_names_freq[century]:
                    first_names_freq[century][first_name[0]] += 1
                else:
                    first_names_freq[century][first_name[0]] = 1
            else:
                first_names_freq[century] = {first_name[0]: 1}

        if last_name:
            # Atualiza a frequência do sobrenome
            if century in last_names_freq:
                if last_name[0] in last_names_freq[century]:
                    last_names_freq[century][last_name[0]] += 1
                else:
                    last_names_freq[century][last_name[0]] = 1
            else:
                last_names_freq[century] = {last_name[0]: 1}

# Imprime os 5 nomes próprios mais usados por século
for century in sorted(first_names_freq):
    print(f'Século {century} - Nomes próprios mais usados:')
    for name, freq in sorted(first_names_freq[century].items(), key=lambda x: x[1], reverse=True)[:5]:
        print(f'{name}: {freq}')
    print()

# Imprime os 5 sobrenomes mais usados por século
for century in sorted(last_names_freq):
    print(f'Século {century} - Sobrenomes mais usados:')
    for name, freq in sorted(last_names_freq[century].items(), key=lambda x: x[1], reverse=True)[:5]:
        print(f'{name}: {freq}')
    print()
