import mysql.connector as mysql
import pandas as pd

conn = mysql.connect(host='localhost',user='root',database='tpbd2')
cursor = conn.cursor()
cursor.execute("SELECT b.kodeklmpk,namaklmpk,namadept FROM barang b INNER JOIN kelompok k ON b.kodeklmpk=k.kodeklmpk INNER JOIN departemen d ON d.kodedept = k.kodedept GROUP BY b.kodeklmpk")
datas = cursor.fetchall()

df = pd.DataFrame(datas)
print("Ditemukan {} data".format(cursor.rowcount))
print(df)

cursor.close()
conn.close()