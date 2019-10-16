import MySQLdb

db = MySQLdb.connect(user='zuplae01', passwd='luquinhas19', host='mysql.zuplae.com', database='zuplae01')

c = db.cursor()
c.execute('select * from TIPO')

for t in c.fetchall():
    print(t)