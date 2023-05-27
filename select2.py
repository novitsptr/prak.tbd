import mysql.connector as mysql

conn = mysql.connect(host='127.0.0.1',
                       user='root',
                       password='',
                       database='kampus')

cursor = conn.cursor()
cursor.execute("select * from mahasiswa")
datas = cursor.fetchall()
for data in datas:
    print("NIM : ",data[0],"Nama : ",data[1],
          " Sex : ",data[2]," ipk : ",data[3])
    
    cursor.close()
    conn.close()
