# Hafta 7

## Görevler
1) İki sayının ortalamasını hesaplayan fonksiyonu yazınız.​
2) Değişken sayıda parametre alan ve sayısal değerlerin toplamını dönen fonksiyonu yazınız.
3) Aşağıdaki belirtilen şekilde çalışan hesap_makinesi fonksiyonunu yazınız. İslem olarak toplama, çıkarma, çarpma ve bölme yapılabilsin.
   
   ```python
   def hesap_makinesi(sayi1, sayi2, islem):
       # kodunuz

   print(hesap_makinesi(15, 5, "+")) # 20
   print(hesap_makinesi(15, 5, "-")) # 10 
   ```
​
4) Sayısal değeri içeren listede aşağıda belirtilen işlemleri yapabilen bir fonksyion yazınız.
   ```python
   def liste_islemleri(liste, islem):
       """ Verilen işlem ve türüne göre:
        - 'tek' -> Sadece tek sayıları döner
        - 'cift' -> Sadece çift sayıları döner
        - 'ters' -> listeyi ters cevirir
        - 'kare' -> elemanların karesini alır
       """

   print(liste_islemleri([1, 2, 3, 4, 5], 'tek')) # [1, 3, 5]
   print(liste_islemleri([1, 2, 3, 4, 5], 'kare')) # [1, 4, 9, 16, 25]
   ```

5) Aşağıda belirtilen nitelikte şifre oluşturma fonksiyonu yazınız.

   ```python
   def sifre_dogrulama(sifre):
       """ Sifrenin:
        - En az 8 karakter
        - En az 1 büyük karakter
        - En az 1 küçük karakter
        - En az 1 rakam içermesini kontrol eder
       """

   print(sifre_dogrulama("Python123")) # True
   print(sifre_dogrulama("python")) # False
  ```
