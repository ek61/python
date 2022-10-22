import sqlite3

con = sqlite3.connect("kütüphane.db")

cursor = con.cursor()
def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT, Yazar TEXT, Yayınevi TEXT, Sayfa_Sayısı INT)")
    con.commit()

tablo_olustur()

def veri_ekle():
    cursor.execute("Insert into kitaplık Values('İstanbul Hatırası','Ahmet Ümit','Everest',561)")
    con.commit()

def veri_ekle2(isim,yazar,yayınevi,sayfa_sayisi):
    cursor.execute("Insert into kitaplık Values(?,?,?,?)",(isim,yazar,yayınevi,sayfa_sayisi))
    con.commit()

def verileri_al():
    cursor.execute("Select * From kitaplık")
    liste = cursor.fetchall()
    print("Kitaplık tablosunun bilgileri")
    for i in liste:
        print(i)

def verileri_al2():
    cursor.execute("Select İsim,Yazar from kitaplık")
    liste = cursor.fetchall()
    for i in liste:
        print(i)

def verileri_al3(yayınevi):
    cursor.execute("select * from kitaplık where Yayınevi = ?",(yayınevi,))
    liste = cursor.fetchall()
    for i in liste:
        print(i)

def verileri_guncelle(eskiYayinevi,yeniYayinevi):
    cursor.execute("update kitaplık set Yayınevi = ? where Yayınevi = ?",(yeniYayinevi,eskiYayinevi))
    con.commit()

def verileri_sil(yazar):
    cursor.execute("delete from kitaplık where Yazar = ?",(yazar,))
    con.commit()


verileri_al()

#verileri_al3("emir")

# isim = input("İsim: ")
# yazar = input("Yazar: ")
# yayınevi = input("Yayınevi: ")
# sayfa_sayisi = input("Sayfa Sayısı: ")
# veri_ekle2(isim,yazar,yayınevi,sayfa_sayisi)

con.close()