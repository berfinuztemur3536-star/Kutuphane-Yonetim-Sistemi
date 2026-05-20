from abc import ABC, abstractmethod


class Kaynak(ABC):
    def __init__(self, baslik, kayitNo):
        self._baslik = baslik
        self._kayitNo = kayitNo

    @property
    def baslik(self):
      return self._baslik

    @baslik.setter
    def baslik(self, value):
      self._baslik = value

    @property
    def kayitNo(self):
      return self._kayitNo


    @abstractmethod
    def __str__(self):
        pass


class Kitap(Kaynak):
    def __init__(self, baslik, kayitNo, yazar, sayfa_sayisi):
        super().__init__(baslik, kayitNo)
        self._yazar = yazar
        self._sayfa_sayisi = sayfa_sayisi


    def __str__(self):
        return f"[Kitap] No: {self.kayitNo} | Başlık: {self.baslik} | Yazar: {self._yazar} | Sayfa: {self._sayfa_sayisi}"

class Dergi(Kaynak):
    def __init__(self, baslik, kayitNo, yayin_donemi, sayi_no):
        super().__init__(baslik, kayitNo)
        self._yayin_donemi = yayin_donemi
        self._sayi_no = sayi_no


    def __str__(self):
        return f"[Dergi] No: {self.kayitNo} | Başlık: {self.baslik} | Dönem: {self._yayin_donemi} | Sayı: {self._sayi_no}"

class Islem(ABC):
    @abstractmethod
    def ekle(self): pass
    @abstractmethod
    def sil(self): pass
    @abstractmethod
    def guncelle(self): pass
    @abstractmethod
    def listele(self): pass

class KitapIslem(Islem):
    kitap_listesi = []

    def ekle(self):
        print("\n--- Yeni Kitap Ekle ---")
        k_no = input("Kitabın kayıt numarasını girin: ")


        for k in self.kitap_listesi:
            if k.kayitNo == k_no:
                print(f"Hata: {k_no} numaralı kayıt zaten mevcut! İkinci kayıt eklenemez.")
                return

        baslik = input("Kitabın başlığını girin: ")
        yazar = input("Kitabın yazarını girin: ")
        sayfa = input("Kitabın sayfa sayısını girin: ")

        yeni_kitap = Kitap(baslik, k_no, yazar, sayfa)
        self.kitap_listesi.append(yeni_kitap)
        print("Kitap başarıyla eklendi.")

        self.toplam_sayi()

    def listele(self):

        if not self.kitap_listesi:
            print("\nKayıt bulunamadı.")
        else:
            print("\n--- Kitap Listesi ---")
            for kitap in self.kitap_listesi:
                print(kitap)


    def toplam_sayi(self):
        print(f"Sistemdeki Toplam Kitap Sayısı: {len(self.kitap_listesi)}")

    def sil(self):
        k_no = input("Silinecek kitabın kayıt nosunu girin: ")
        for k in self.kitap_listesi:
            if k.kayitNo == k_no:
                self.kitap_listesi.remove(k)
                print("Kayıt silindi.")
                return
        print("Kayıt bulunamadı.")

    def guncelle(self):
        k_no = input("Güncellenecek kitabın kayıt nosunu girin: ")
        for k in self.kitap_listesi:
            if k.kayitNo == k_no:
                k.baslik = input("Yeni başlık: ")
                print("Kayıt güncellendi.")
                return
        print("Kayıt bulunamadı.")

class DergiIslem(Islem):
    dergi_listesi = []

    def ekle(self):
        print("\n--- Yeni Dergi Ekle ---")
        k_no = input("Derginin kayıt numarasını girin: ")


        for d in self.dergi_listesi:
            if d.kayitNo == k_no:
                print(f"Hata: {k_no} numaralı kayıt zaten mevcut!")
                return

        baslik = input("Dergi başlığı: ")
        donem = input("Yayın dönemi (Aylık/Haftalık): ")
        sayi = input("Sayı no: ")

        yeni_dergi = Dergi(baslik, k_no, donem, sayi)
        self.dergi_listesi.append(yeni_dergi)
        print("Dergi başarıyla eklendi.")
        self.toplam_sayi()

    def listele(self):

        if not self.dergi_listesi:
            print("\nKayıt bulunamadı.")
        else:
            for dergi in self.dergi_listesi:
                print(dergi)


    def toplam_sayi(self):
        print(f"Sistemdeki Toplam Dergi Sayısı: {len(self.dergi_listesi)}")

    def sil(self):
        k_no = input("Silinecek derginin kayıt nosunu girin: ")
        for d in self.dergi_listesi:
            if d.kayitNo == k_no:
                self.dergi_listesi.remove(d)
                print("Kayıt silindi.")
                return
        print("Kayıt bulunamadı.")

    def guncelle(self):
        k_no = input("Güncellenecek derginin kayıt nosunu girin: ")
        for d in self.dergi_listesi:
            if d.kayitNo == k_no:
                d.baslik = input("Yeni başlık: ")
                print("Kayıt güncellendi.")
                return
        print("Kayıt bulunamadı.")


def ana_menu():
    k_islem = KitapIslem()
    d_islem = DergiIslem()

    while True:
        print("\n--- Kütüphane Yönetim Sistemi ---")
        print("1-4 Kitap İşlemleri | 5-8 Dergi İşlemleri | 9 Çıkış")
        print("1. Kitap Ekle\n2. Kitap Sil\n3. Kitap Güncelle\n4. Kitapları Listele")
        print("5. Dergi Ekle\n6. Dergi Sil\n7. Dergi Güncelle\n8. Dergileri Listele")
        print("9. Çıkış")

        secim = input("Yapmak istediğiniz işlemi seçin (1-9): ")

        if secim == '1': k_islem.ekle()
        elif secim == '2': k_islem.sil()
        elif secim == '3': k_islem.guncelle()
        elif secim == '4': k_islem.listele()
        elif secim == '5': d_islem.ekle()
        elif secim == '6': d_islem.sil()
        elif secim == '7': d_islem.guncelle()
        elif secim == '8': d_islem.listele()
        elif secim == '9':
            print("Sistemden çıkılıyor...")
            break
        else:
            print("Lütfen 1-9 arasında bir sayı girin!")

if __name__ == "__main__":
    ana_menu()
