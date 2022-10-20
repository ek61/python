class Bilgisayar():
    def __init__(self,marka,islemci,ram,depolama):
        print("init fonksiyonu")
        self.marka = marka 
        self.islemci = islemci
        self.ram = ram
        self.depolama = depolama
    def bilgileriGöster(self):
        print("Bilgisayar bilgileri...")
        print("Markası: {}\nİşlemcisi: {}\nRam: {}\nDepolama: {}".format(self.marka,self.islemci,self.ram,self.depolama))
    def ramDegistir(self,yeniRam):
        self.ram =yeniRam


bilgisayar = Bilgisayar("Lenovo","i7 11",16,"1tb")
bilgisayar.bilgileriGöster()
bilgisayar.ramDegistir(32)
bilgisayar.bilgileriGöster()