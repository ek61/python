class Ogrenci():
    def __init__(self,adi="Bilgi yok",soyadi= "Bilgi yok",numarasi= "Bilgi yok",sinifi= "Bilgi yok",notOrt= "Bilgi yok"):
        self.adi = adi
        self.soyadi = soyadi
        self.numarasi = numarasi
        self.sinifi = sinifi
        self.notOrt = notOrt
    def ogrenciEkle(self,adi,soyadi,numarasi,sinifi,notOrt):
        print("Öğrenci Ekleme Fonksiyonu Çalıştırıldı.")
        self.adi = adi
        self.soyadi = soyadi
        self.numarasi = numarasi
        self.sinifi = sinifi
        self.notOrt = notOrt
    def ogrenciSilme(self):
        print("Öğrenci Silme Fonksiyonu Çalıştırıldı.")
        self.adi = "Bilgi yok"
        self.soyadi = "Bilgi yok"
        self.numarasi = "Bilgi yok"
        self.sinifi = "Bilgi yok"
        self.notOrt = "Bilgi yok"
    def notDegistirme(self,yeniOrt):
        print("Öğrenci Notu Değiştirme Fonksiyonu Çalıştırıldı.")
        self.notOrt = yeniOrt
    def sinifDegistirme(self,yeniSinif):
        print("Öğrenci Notu Değiştirme Fonksiyonu Çalıştırıldı.")
        self.notOrt = yeniSinif    
    def bilgileriGöster(self):
        print("Öğrenci Bilgileri Gösterme Fonksiyonu Çalıştırıldı.")
        print("Ad: {}\nSoyadı: {}\nNumarası: {}\nSınıfı: {}\nNot Ortalaması: {}".format(self.adi,self.soyadi,self.numarasi,self.sinifi,self.notOrt))

print("### Öğrenci Otomasyon Sistemine Hoş Geldiniz ###\n")
print("Sistemde Bulunan Özellikler\n[1]Öğrenci Ekleme\n[2]Öğrenci Silme\n[3]Öğrenci Bilgilerini Gösterme\n[4]Not Değiştirme\n[5]Sınıf Değiştirme")
x = int(input("Yapmak istediğiniz işlemin kodunu giriniz: "))
if(x == 1):
    ogrenci = Ogrenci()
    adi = input("Adı: ")
    soyadi = input("Soyadı: ")
    numarasi = input("Numarası: ")
    sinifi = input("Sınıfı: ")
    notOrt = input("Not Ortalaması: ")
    ogrenci.ogrenciEkle(adi,soyadi,numarasi,sinifi,notOrt)
elif(x == 2):
    ogrenci = Ogrenci()
    ogrenci.ogrenciSilme()
elif(x == 3):
    ogrenci = Ogrenci()
    ogrenci.bilgileriGöster()
elif(x == 4):
    ogrenci = Ogrenci()
    y = int(input("Öğrencinin yeni notunu girin: "))
    ogrenci.notDegistirme(y)
elif(x == 5):
    ogrenci = Ogrenci()
    z = int(input("Öğrencinin yeni sınıfını girin: "))
    ogrenci.sinifDegistirme(z)
else:
    print("Yanlış özellik kodu girdiniz.")
print("\n### Sistemden Çıkılıyor... ###")
print("çalışıyor")