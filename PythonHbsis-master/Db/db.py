import MySQLdb

conexao_mysql  = MySQLdb.connect(host='localhost', database='MercadoTech', user='root', passwd='')
nome_da_bebida = 'Suco de bixcoito'

cursor = conexao_mysql.cursor()
cursor.execute(f"INSERT INTO bebidas (tipo) VALUES('{nome_da_bebida}')")
conexao_mysql.commit()

cursor.execute('SELECT * FROM bebidas')
print('='*50)
print('\n'*3)

for b in cursor.fetchall():
    print(b)

print('\n'*3)
print('='*50)