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
values = [
    ("19561007","TONO","W",2.3),
    ("19561008","MIRA","W",3.1),
    ("19561009","RINI","W",2.7)
]
#untuk setiap item di values dibaca sebagai val
for val in values:
    #jalankan strQuery dengan isian sesuai variabel val
    cursor.execute(strQuery, val)
    conn.commit()

print("Sebanyak {} data telah ditambahkan ".format(len(values)))
cursor.close()
conn.close()