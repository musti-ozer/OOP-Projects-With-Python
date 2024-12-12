#3. Kütüphane Yönetim Sistemi

class Kitap:
    def __init__(self, ad, yazar):
        self.ad = ad  # Kitap adı
        self.yazar = yazar  # Yazar adı
        self.odunc_alindi = False  # Kitap ödünç alındı mı?

class Kutuphane:
    def __init__(self):
        self.kitaplar = []  # Kütüphanedeki kitaplar
        self.odunc_kitaplar = []  # Ödünç alınan kitaplar

    def kitap_ekle(self, kitap):
        self.kitaplar.append(kitap)

    def kitap_listele(self):
        for kitap in self.kitaplar:
            durum = "Ödünç Alındı" if kitap.odunc_alindi else "Mevcut"
            print(f"{kitap.ad} - {kitap.yazar} ({durum})")

    def odunc_ver(self, kitap_ad):
        for kitap in self.kitaplar:
            if kitap.ad == kitap_ad and not kitap.odunc_alindi:
                kitap.odunc_alindi = True
                self.odunc_kitaplar.append(kitap)
                print(f"{kitap_ad} ödünç verildi.")
                return
        print(f"{kitap_ad} mevcut değil veya zaten ödünç alındı.")

    def odunc_al(self, kitap_ad):
        for kitap in self.odunc_kitaplar:
            if kitap.ad == kitap_ad:
                kitap.odunc_alindi = False
                self.odunc_kitaplar.remove(kitap)
                print(f"{kitap_ad} geri alındı.")
                return
        print(f"{kitap_ad} ödünç alınmamış.")

# Ana program
kutuphane = Kutuphane()

# Kitaplar ekleyelim
kitap1 = Kitap("1984", "George Orwell")
kitap2 = Kitap("Savaş ve Barış", "Lev Tolstoy")
kitap3 = Kitap("Bir Ada Hikayesi", "Yaşar Kemal")

kutuphane.kitap_ekle(kitap1)
kutuphane.kitap_ekle(kitap2)
kutuphane.kitap_ekle(kitap3)

# Kitapları listeleyelim
print("Kütüphanedeki Kitaplar:")
kutuphane.kitap_listele()

# Kitap ödünç verelim
kutuphane.odunc_ver("1984")
kutuphane.odunc_ver("Savaş ve Barış")

# Ödünç alınan kitapları listeleyelim
print("\nÖdünç Alınan Kitaplar:")
kutuphane.kitap_listele()

# Kitap geri alalım
kutuphane.odunc_al("1984")

# Güncel durumu görelim
print("\nGüncel Kitap Durumları:")
kutuphane.kitap_listele()





#7. Film Yönetim Sistemi

class Film:
    def __init__(self, ad, yonetmen, yil, tur):
        self.ad = ad  # Film adı
        self.yonetmen = yonetmen  # Yönetmen
        self.yil = yil  # Yıl
        self.tur = tur  # Tür

class FilmYoneticisi:
    def __init__(self):
        self.filmler = []  # Film listesini tutacak

    def film_ekle(self, ad, yonetmen, yil, tur):
        yeni_film = Film(ad, yonetmen, yil, tur)
        self.filmler.append(yeni_film)

    def film_sil(self, ad):
        for film in self.filmler:
            if film.ad == ad:
                self.filmler.remove(film)
                print(f"{ad} adlı film silindi.")
                return
        print(f"{ad} adlı film bulunamadı.")

    def film_listele(self, yil=None, tur=None):
        for film in self.filmler:
            if (yil is None or film.yil == yil) and (tur is None or film.tur == tur):
                print(f"Film Adı: {film.ad}, Yönetmen: {film.yonetmen}, Yıl: {film.yil}, Tür: {film.tur}")
                
# Ana program
film_yoneticisi = FilmYoneticisi()

# Filmleri ekleyelim
film_yoneticisi.film_ekle("Joker", "Todd Phillips", 2019, "Drama")
film_yoneticisi.film_ekle("The Dark Knight", "Christopher Nolan", 2008, "Aksiyon")
film_yoneticisi.film_ekle("Interstellar", "Christopher Nolan", 2014, "Bilim Kurgu")

# Filmleri listeleyelim
print("Tüm Filmler:")
film_yoneticisi.film_listele()

# Yıla göre listeleme
print("\n2019 Yılında Çıkan Filmler:")
film_yoneticisi.film_listele(yil=2019)

# Türle göre listeleme
print("\nBilim Kurgu Türündeki Filmler:")
film_yoneticisi.film_listele(tur="Bilim Kurgu")

# Film silme
film_yoneticisi.film_sil("Inception")
print("\nGüncel Film Listesi:")
film_yoneticisi.film_listele()

