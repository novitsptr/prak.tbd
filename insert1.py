import mysql.connector as mysql

conn = mysql.connect(host='localhost',
                    user='root',
                    password='',
                    database='kampus')

cursor = conn.cursor()

strQuery = """
            INSERT INTO mahasiswa (nim, nama,seks,ipk)
            VALUES (%s, %s, %s, %s)
            """

val = ("215610061","NOVIT","W",3.8)

#jalankan strQuery dengan isian sesuai variabel val
cursor.execute(strQuery, val)
conn.commit()

print("Sebanyak {} data telah ditambahkan".format(cursor.rowcount))
cursor.close()
conn.close()