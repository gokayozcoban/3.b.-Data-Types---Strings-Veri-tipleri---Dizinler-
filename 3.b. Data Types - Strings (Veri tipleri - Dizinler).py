# DATA TYPES (DATA TİPLERİ)

# STRİNGS (KARAKTER DİZİNLERİ)

# Bir karakter dizinini tanımlamak için tırnaklar kullanılır. birkaç satır ka-
# rakter dizini yazıyorsak 3 tırnak kullanılır:
print("""Üç tırnaklı
karakter
dizinine
örnek""")
üç tırnaklı
karakter
dizinine
örnek

print('Tek tırnak: Tek satırlık stringlerde uygulanır.')
Tek tırnak: Tek satırlık stringlerde uygulanır.
print("Çift Tırnak: Yine tek satırlık cümlelerde kullanılır.")
Çift Tırnak: Yine tek satırlık cümlelerde kullanılır.

# Farklı tırnakların olmasının nedeni, tek tırnakla ayrılan özel isimlerin ayrım
# işaretinin çıktıyı string olarak kabul etmesini önlemek:
print("Türkiye'nin başkenti Ankara'dır.")
Türkiye'nin başkenti Ankara'dır.
# Yukarıdaki gibi bir çıktı almak için çift tırnak ("") kullandım. Çünkü tek
# tırnak kullansam şöyle hatalı bir print kodu oluşurdu:
print('Türkiye'nin başkenti Ankara'dır.') # Python, dğerlerin hatalı olduğunu
# ifade eden renklendirme yapardı.
# Çift tırnakla başlayıp ayraçları tek tırnak yaparsak Python, çift tırnakla
# başladığından dolayı aradaki tek tırnakları görmez ve onu da string içeriği
# olarak kabul eder. Aynı şekilde üç tırnakla başlasaydım bu sefer de çift tır-
# nakları görmeyip onları da string içeriği olarak kabul ederdi.
