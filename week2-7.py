vize = float(input("Vize notunu giriniz: "))
final = float(input("Final notunu giriniz: "))

if (vize < 0 or vize > 100) or (final < 0 or final > 100):
    print("Hatalı not.")
else:
    ortalama = (vize * 0.4) + (final * 0.6)
    print("Ortalamanız:", ortalama)

    if final < 50:
        print("Dersten kaldınız.")
    elif ortalama >= 60:
        print("Dersten geçtiniz.")
    else:
        print("Dersten kaldınız (Ortalama 60'ın altında).")
