import mysql.connector as mysql
import pandas as pd

conn = mysql.connect (host ='localhost',
                      user ='root',
                      password = '',
                      database = 'tpbd2')

cursor = conn.cursor()
cursor.execute("SELECT departemen.namadept, COUNT(barang.kodebrg), SUM(barang.stok) FROM barang JOIN kelompok ON barang.kodeklmpk = kelompok.kodeklmpk JOIN departemen ON kelompok.kodedept = departemen.kodedept GROUP BY departemen.namadept")
datas = cursor.fetchall()

df = pd.DataFrame (datas)
df.colums = ('namadept','kodebrg','stok')
print (df)

cursor.close()
conn.close()