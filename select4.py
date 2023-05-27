import mysql.connector as mysql
import pandas as pd

conn = mysql.connect(host='127.0.0.1',
                       user='root',
                       password='',
                       database='kampus')

cursor = conn.cursor()
strQuery = '''
        SELECT seks, count(*) as banyak
        FROM mahasiswa
        GROUP BY seks
        '''
cursor.execute(strQuery)
datas = cursor.fetchall()

df = pd.DataFrame(datas)
df.columns = ['SEKS','BANYAK']
print("Ditemukan Sebanyak : {} data ". format(cursor.rowcount))
print(df)
    
cursor.close()
conn.close()