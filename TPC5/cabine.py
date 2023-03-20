import re
import sys

MOEDAS_VALIDAS = ["5c", "10c", "20c", "50c", "1e", "2e"]
SALDO_MINIMO_CHAMADA_NACIONAL = 25
CUSTO_CHAMADA_INTERNACIONAL = 150
CUSTO_CHAMADA_VERDE = 0
CUSTO_CHAMADA_AZUL = 10

estado = "INICIAL"
saldo = 0
troco = []
numero = ""

while True:
    entrada = sys.stdin.readline().strip()

    if not entrada:
        break

    if estado == "INICIAL":
        if entrada == "LEVANTAR":
            estado = "AGUARDANDO_MOEDAS"
            print("maq: \"Introduza moedas.\"")
        else:
            print("maq: \"Levante o auscultador para iniciar a chamada.\"")
    
    elif estado == "AGUARDANDO_MOEDAS":
        if entrada.startswith("MOEDA "):
            moedas = entrada[6:].split(", ")

            for m in moedas:
                if m in MOEDAS_VALIDAS:
                    saldo += int(re.findall(r'\d+', m)[0])
                else:
                    print(f"maq: \"{m} - moeda inválida; saldo = {saldo/100:.2f}e\"")

            print(f"maq: \"saldo = {saldo/100:.2f}e\"")
            estado = "AGUARDANDO_TELEFONE"
        else:
            print("maq: \"Introduza moedas para continuar.\"")
    
    elif estado == "AGUARDANDO_TELEFONE":
        if entrada.startswith("T="):
            numero = entrada[2:]

            if numero.startswith("601") or numero.startswith("641"):
                print("maq: \"Esse número não é permitido neste telefone. Queira discar novo número!\"")
            elif numero.startswith("00"):
                if saldo >= CUSTO_CHAMADA_INTERNACIONAL:
                    saldo -= CUSTO_CHAMADA_INTERNACIONAL
                    print(f"maq: \"Chamada internacional para {numero} - custo = 1.50e; saldo = {saldo/100:.2f}e\"")
                    estado = "CHAMADA_CONCLUIDA"
                else:
                    print(f"maq: \"Saldo insuficiente para chamada internacional - custo = 1.50e; saldo = {saldo/100:.2f}e\"")
                    estado = "AGUARDANDO_MOEDAS"
            elif numero.startswith("2"):
                if saldo >= SALDO_MINIMO_CHAMADA_NACIONAL:
                    saldo -= SALDO_MINIMO_CHAMADA_NACIONAL
                    print(f"maq: \"Chamada nacional para {numero} - custo = {SALDO_MINIMO_CHAMADA_NACIONAL/100:.2f}e; saldo = {saldo/100:.2f}e\"")
