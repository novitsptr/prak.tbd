import mysql.connector as mysql

conn = mysql.connect(host='127.0.0.1',
                       user='root',
                       password='',
                       database='kampus')

if conn.is_connected():
    print("Berhasil Koneksi")
    conn.close()
