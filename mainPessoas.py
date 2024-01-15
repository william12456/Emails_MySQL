import pymysql
from pathlib import Path
import json
from datetime import date

# Definindo path
path = Path.cwd() / 'arquivo.json'
# Conectar ao banco de dados
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    database="granlog"
)

# Executar consultas
with connection.cursor() as cursor:
    sql = "SELECT tipo_contato.Descricao, pessoa_contato.Valor, Nome, DataNascimento, CPF, Identidade, Emissor, DataEmissao, Cep, Endereco, Numero, Complemento, Bairro, Municipio, UF FROM testesql.pessoa inner join testesql.pessoa_contato ON pessoa.Id_Pessoa = pessoa_contato.Id_Pessoa inner join testesql.tipo_contato ON pessoa_contato.Id_Tipo_Contato = tipo_contato.Id_Tipo_Contato WHERE tipo_contato.Id_Tipo_Contato = 3"    
    cursor.execute(sql)
    result = cursor.fetchall()

# Obter nomes das colunas
columns = [column[0] for column in cursor.description]

# Criar lista de dicionários
result_dict_list = []
for row in result:
    row_dict = {}
    for i in range(len(columns)):
        # Verificar se o valor é do tipo date e convertê-lo para string
        if isinstance(row[i], date):
            row_dict[columns[i]] = row[i].isoformat()
        else:
            row_dict[columns[i]] = row[i]

    result_dict_list.append(row_dict)

# Fechar a conexão
connection.close()

with open(path, 'w', encoding='utf-8') as arquivo:
    # Imprimir o resultado como objetos chave-valor
    json.dump(result_dict_list, arquivo, indent=2, ensure_ascii=False)
