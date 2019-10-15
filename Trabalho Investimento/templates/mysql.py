import MySQLdb

conexao_mysql = MySQLdb.connect(host = 'localhost', database='invest', user='root', passwd='')
nome_investimento = 'invest pro'

cursor = conexao_mysql()
cursor.execute(f"INSERT INTO investimento (tipo) VALUES('{nome_investimento}')")
conexao_mysql.commit()

cursor.execute('SELECT * FROM investimento')
print('='*50)
print('\n'*3)

for b in cursor.fetchall():
    print(b)

