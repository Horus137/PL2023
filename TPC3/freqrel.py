import re

# Frequência de tipos de relação
relationship_freq = {}

with open('processos.txt', 'r') as f:
    for line in f:
        # Extrai a relação
        relation = re.findall(r'(?:irmãos?|filhos?|netos?|bisnetos?|sobrinhos?|primos?|genros?|sogros?|cunhados?|tios?|avôs?|bisavôs?|sobrinhos-netos?|primo-netos?)', line, re.IGNORECASE)

        if relation:
            # Atualiza a frequência da relação
            for r in relation:
                if r in relationship_freq:
                    relationship_freq[r] += 1
                else:
                    relationship_freq[r] = 1

# Imprime a frequência de cada relação
for r, freq in sorted(relationship_freq.items(), key=lambda x: x[1], reverse=True):
    print(f'{r}: {freq}')
