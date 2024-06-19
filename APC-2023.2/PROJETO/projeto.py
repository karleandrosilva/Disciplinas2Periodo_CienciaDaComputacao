import csv

arquivo = csv.reader('Disciplinas2Periodo_CienciaDaComputacao/dados/notas.csv')

def validar_registro(registro, linha):
    erros = []
    
    # Verifica se o nome está presente e não excede 40 caracteres
    if not registro['nome']:
        erros.append(('Nome ausente', linha))
    elif len(registro['nome']) > 40:
        erros.append(('Nome excede 40 caracteres', linha))

    # Verifica se a data de nascimento está presente e tem o formato dd/mm/aaaa
    if not registro['Data de Nascimento']:
        erros.append(('Data de Nascimento ausente', linha))
    elif len(registro['Data de Nascimento']) != 10 or not registro['Data de Nascimento'].count('/') == 2:
        erros.append(('Data de Nascimento inválida', linha))

    # Verifica se há pelo menos um dos dois: matrícula ou CPF
    if not registro['Matrícula'] and not registro['CPF']:
        erros.append(('Matrícula e CPF ausentes', linha))

    return erros

def ler_e_validar_csv(arquivo):
    problemas = []
    with open(arquivo, 'r', newline='') as f:
        reader = csv.DictReader(f)
        for linha, registro in enumerate(reader, start=1):
            erros = validar_registro(registro, linha)
            problemas.extend(erros)
    if problemas:
        print('Problema!')
        for erro, linha in problemas:
            print(f'Linha {linha}: {erro}')
    else:
        print('OK')

# Dados de exemplo
dados = arquivo

# Ler e validar o arquivo CSV
ler_e_validar_csv(arquivo)
