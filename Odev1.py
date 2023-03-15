# 1-Python'da Veri Tiplerini araştırınız, her bir veri tipi için kendi cümlelerinizle açıklamalar yazınız.

# int: Tamsayı ifadeler kullanılır.
sayi1 = 15
sayi2 = 0
sayi3 = -15

# float: Virgüllü sayılar ifade edilir.
ondalikli = 7.5

# bool: True veya False mantıksal ifadeler kullanılır
mantiksal = True

# string: Bir veya daha fazla karakterler içerir.
karakter = "a"
metin = "Musa"

# list: Birden fazla verileri liste halinde tutulur. Değiştirilebilir.
liste = ["Musa", "Görgeç", 15]

# tuple: Birden fazla verileri liste halinde tutulur. Değiştirilemez.
liste = ("Musa", "Görgeç", 25)

# dictionary: Anahtar-değer çiftleri şeklinde organize edilmiş veri koleksiyonlarıdır. Anahtarlar tekil ve değiştirilemezdir.
sozluk = {"İsim": "Musa",
          "No": 15}

# set: Benzersiz elemanlardan oluşan bir koleksiyondur. Elemanları sıralı değildir ve her eleman sadece bir kez görünür.
kume = set([1, 2, 3])
kume.add(3)
print(kume)


# ----------------------------------------------------------------------------------------------------------------------
# 2-Kodlama.io sitesinde değişken olarak kullanıldığını düşündüğünüz verileri, veri tipleriyle birlikte örneklendiriniz.

int_tamamlanan_kurs = 100
str_amac = 'Derste gördüğümüz "Değişkenler" ve "Şart Blokları" konularının pekiştirilmesi.'
bool_odev_tamamlandi = False
list_kurslar = ['Yazılım Geliştirici Yetiştirme Kampı',
                "Python & Selenium",
                "Java"]
set_kurslar = set(list_kurslar)
set_kurslar.add("Java")
sozluk_gunler = {"Gun1":"Kamp tanıtımı ve tanışma",
                 "Gun2":"Tip Dönüşümleri"}

# 3-Kodlama.io sitesinde şart blokları kullanıldığını düşündüğünüz kısımları örneklendiriniz ve Python dilinde bu örnekleri koda dökünüz.
bool_odev_tamamlandi2 = True
if bool_odev_tamamlandi and bool_odev_tamamlandi2:
    print("Ödevi başarıyla tamamlandı.")
elif not bool_odev_tamamlandi or not bool_odev_tamamlandi2:
    print("2 Ödevi de tamamlayınız.")
else:
    print("Ödevleri tamamlayınız.")
