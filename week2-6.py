sayı1 = float(input("İlk sayıyı giriniz."))
sayı2 = float(input("İkinci sayıyı giriniz."))
işlem = input("İşlem giriniz.")

if işlem == "+":
    sonuç = sayı1 + sayı2
elif işlem == "-":
    sonuç = sayı1 - sayı2
elif işlem == "*":
    sonuç = sayı1 * sayı2
elif işlem == "/":
    if sayı2 == 0:
        sonuç = "Sıfıra bölme hatası."
    else:
        sonuç = sayı1 / sayı2
else:
    sonuç = "Hatalı işlem."
print("Sonuç=", sonuç)
