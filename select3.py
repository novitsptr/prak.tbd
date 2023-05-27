import mysql.connector as mysql
import pandas as pd

conn = mysql.connect(host='127.0.0.1',
                       user='root',
                       password='',
                       database='kampus')

cursor = conn.cursor()
cursor.execute("select * from mahasiswa")
datas = cursor.fetchall()

df = pd.DataFrame(datas)
df.columns = ['NIM','NAMA','SEKS','IPK']
print(df)
    
cursor.close()
conn.close()
