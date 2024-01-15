import pymysql

# Conectar ao banco de dados
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    database="granlog"
)

# Executar consultas
with connection.cursor() as cursor:
    sql = "SELECT nome, cnpj, cidade FROM granlog.pessoa LIMIT 1"
    cursor.execute(sql)
    result = cursor.fetchall()

# Obter nomes das colunas
columns = [column[0] for column in cursor.description]

# Criar lista de dicionários
result_dict_list = []
for row in result:
    row_dict = dict(zip(columns, row))
    result_dict_list.append(row_dict)

# Fechar a conexão
connection.close()

# Imprimir o resultado como objetos chave-valor
for item in result_dict_list:
    print(item[''])
