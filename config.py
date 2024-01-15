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
    sql = "SELECT * FROM sua_tabela"
    cursor.execute(sql)
    result = cursor.fetchall()

# Fechar a conexão
connection.close()
