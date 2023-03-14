import csv
import json
import re

def processar_lista(valor):
    match = re.match(r'(.+){(\d+)(,\d+)?}', valor)
    if match:
        min_lista = int(match.group(2))
        max_lista = int(match.group(3)[1:]) if match.group(3) else min_lista
        valores = [campo.strip() for campo in valor.split(',') if campo.strip()]
        if len(valores) < min_lista or len(valores) > max_lista:
            raise ValueError(f'Número de elementos inválido para {valor}')
        return valores
    return valor

def processar_agregacao(valor):
    match = re.match(r'(.+)::(.+)', valor)
    if match:
        funcao = match.group(2)
        valores = processar_lista(match.group(1))
        if funcao == 'sum':
            resultado = sum([float(valor) for valor in valores])
        elif funcao == 'media':
            resultado = sum([float(valor) for valor in valores]) / len(valores)
        else:
            raise ValueError(f'Função de agregação inválida: {funcao}')
        return resultado
    return valor
  
  def convert_csv_to_json(csv_file_path, json_file_path):
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        header = next(csv_reader)
        json_data = []
        for row in csv_reader:
            json_row = {}
            for i, value in enumerate(row):
                field_name = header[i]
                if "{" in field_name:
                    field_name, array_length = field_name.split("{")
                    array_length = array_length[:-1]
                    if "," in array_length:
                        min_length, max_length = array_length.split(",")
                        min_length = int(min_length)
                        max_length = int(max_length)
                        values = [int(v) if v.isdigit() else v for v in row[i:i+max_length]]
                        values = [v for v in values if v != '']
                        if len(values) < min_length:
                            values += [''] * (min_length - len(values))
                        json_row[field_name] = values
                    else:
                        array_length = int(array_length)
                        json_row[field_name] = [int(v) if v.isdigit() else v for v in row[i:i+array_length]]
                elif "::" in field_name:
                    field_name, function_name = field_name.split("::")
                    function_name = function_name.lower()
                    values = [int(v) if v.isdigit() else v for v in row[i:i+len(header)]]
                    values = [v for v in values if v != '']
                    if function_name == "sum":
                        json_row[field_name] = sum(values)
                    elif function_name == "media":
                        json_row[field_name] = sum(values) / len(values)
                else:
                    json_row[field_name] = value
            json_data.append(json_row)
    with open(json_file_path, 'w') as json_file:
        json.dump(json_data, json_file, indent=2)
