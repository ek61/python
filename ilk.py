 #Ekrana Hello World yazdırma
print("Hello World")

#Kullanıcının ismini alarak Merhaba (kullanıcı ismi) yazdırma
isim = input("İsminizi girin: ")
print("Merhaba "+ isim)

#Girilen iki sayıyı toplama
sayi1 = int(input("1.Sayıyı girin: "))
sayi2 = int(input("2.Sayıyı girin: "))
toplam = sayi2 + sayi1
print("Toplam: " , toplam)

#Girilen iki sayının ortalamasını bulma
sayi1 = int(input("1.Sayıyı girin: "))
sayi2 = int(input("2.Sayıyı girin: "))
toplam = sayi2 + sayi1
ort = toplam / 2
print(ort)

#Girilen vize ve final notu ortalaması hesaplayan python örneği
vize = int(input("Vize notunu girin: "))
final = int(input("Final notunu girin: "))
ort = vize*0.3 + final*0.7
print(ort)

#Yazılı ortalaması girilen öğrencinin sınıfı geçme durumunu gösterme
vize = int(input("Vize notunu girin: "))
final = int(input("Final notunu girin: "))
ort = vize*0.3 + final*0.7
print("Notların ortalaması: " , ort)
if(ort>=50):
    print("Dersi geçtiniz")
else:
    print("Dersden kaldınız")

#Girilen sayı tek mi yoksa çift mi
sayi = int(input("Sayı giriniz: "))
if(sayi%2 == 0):
    print("Girilen sayı çift")
else:
    print("Girilen sayı tek")    

#Girilen sayı pozitif, negatif veya 0 mı olduğunu bulma
sayi = int(input("Sayı giriniz: "))
if(sayi<0):
    print("Sayı negatif")
elif(sayi>0):
    print("Sayı pozitif")
else:
    print("Sayı 0")

#Girilen boy ve kütle değerlerine göre vücut kitle indeksini hesaplama ve buna göre aralık belirleme
boy = float(input("Boyunuzu giriniz: "))
kilo = float(input("Kilonuzu girin: "))
endeks = kilo / (boy * boy)
print("Vücut kitle endeksiniz: " , endeks)
if(endeks <= 18):
    print("Zayıf")
elif(endeks > 18 and endeks <= 25):
    print("Normal")
elif(endeks > 25 and endeks <= 30):
    print("Obez")
else:
    print("Aşırı obez")

#1-100 arasındaki sayıları yazdırma
for i in range(1,101):
    print(i)

#1-100 arasındaki çift sayıları yazdırma
for i in range(1,101):
    if(i % 2 == 0):
        print(i)

#Girilen metni harflerine ayırma
print("Kelime giriniz: ")
metin = input()
i = 0
for i in range(len(metin)):
    print(metin[i])
print("Kelime harflerine ayrıldı")

#Girilen sayılar arasındaki sayıların toplamını bulma
toplam = 0
sayi1 = int(input("1.Sayıyı giriniz: "))
sayi2 = int(input("2.Sayıyı giriniz: "))
for i in range(sayi1+1 , sayi2):
    toplam += i
print(toplam)

#Kullanıcıya sinema ya da tiyatro tercihi sorulsun. Sinema izlemek için 15 TL, tiyatro için 10 TL ödenmesi gerekmedir. Öğrencilere %50 indirim yapıldığı düşünülerek öğrenci ise indirim yapılan; öğrenci değilse indirimsiz tutarı hesaplayarak ekrana yazdıran kodu yazınız.
secim = input("Sinema izlemek için [1], Tiyatro izlemek için [2]'yi tuşlayın: ")
ogrenci = input("Öğrenci misiniz? [E/H]: ")
ucret = 0
if(secim == "1"):
    ucret = 15
elif(secim == "2"):
    ucret = 10
else:
    print("Hatalı tuşlama yapıldı.Tekrar deneyin.")
if(ogrenci == "E" or ogrenci == "e"):
    ucret = ucret / 2
print("Ödemeniz gereken ucret {}".format(ucret))

#Fonksiyon kullanılarak yarıçapı girilen bir çemberin çevresini hesaplama
def cemberCevre(yaricap):
    cevre = yaricap * 2 * 3
    return cevre
r = float(input("Yarıçapı girin: "))
print(cemberCevre(r))

#Fonksiyon kullanarak genişliği ve yüksekliği girilen dikdörtgenin alanını hesaplama
def rectAlan(genislik,yükseklik):
    alan = genislik * yükseklik
    return alan
kenar1 = float(input("1.Kenar uzunluğunu giriniz: "))
kenar2 = float(input("2.Kenar uzunluğunu giriniz: "))
print("Kenar uzunlukları girilen dikdörtgenin alanı: ",rectAlan(kenar1,kenar2))

#Sayı tahmin oyunu
from random import randint
rand =randint(1,100)
sayac = 0
while True:
    sayac += 1
    sayi = int(input("1 ile 100 arasında bir sayı girerek oyuna başlayın [Oyundan çıkmak için '0' giriniz]: "))
    if(sayi == 0):
        print("Oyundan çıktınız")
        break
    elif(sayi < rand):
        print("Daha büyük bir sayı giriniz: ")
        continue
    elif(sayi > rand):
        print("Daha küçük bir sayı giriniz: ")
        continue
    else:
        print("Rastgele seçilen sayı {}".format(rand))
        print("Yaptığınız tahmin sayısı {}".format(sayac))
