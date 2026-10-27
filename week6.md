# Hafta 6

## Görevler
1) urun_fiyatlari = { ​"laptop": 12000,​"telefon": 8000,​"tablet": 5000,​"kulaklik": 1500​ }​
   - Fiyatı 6000 TL'den yüksek ürünleri liste halinde yazdırın​
   - Tüm ürünlere %10 zam yaparak zamlı_fiyat sözlüğünü oluşturun.​
   - En pahalı ve en ucuz ürünü fiyatıyla birlikte ekrana yazdırın.
​

2) Aşağıdaki öğrenci bilgilerini notlarına göre gruplayın.​
   
   - ogrenciler = [​{"ad": "Ali", "not": 85},​ {"ad": "Ayşe", "not": 45},​ {"ad": "Mehmet", "not": 85},​ {"ad": "Zeynep", "not": 60}​]​
   - Beklenen: {85: ['Ali', 'Mehmet'], 45: ['Ayşe'], 60: ['Zeynep']}​ ​
​
3) ogrenciler = [​{"ad": "Ali", "notlar": [85, 90, 78]},​ {"ad": "Veli", "notlar": [70, 65, 80]},​ {"ad": "Ayşe", "notlar": [95, 88, 92]}​]​
   
   - Her öğrencinin not ortalamasını hesaplayıp sözlüğe ekleyin (ortalama anahtarını kullan)​
   - En yüksek ortalamaya sahip öğrenciyi ekrana ortalama bilgisi ile yazdırın.
   - Sınıfın genel ortalamasını ekrana yazdırın.
​
4) Aşağıdaki küme işlemlerini yapınız.​​
 
   urunler_A = {"elma", "armut", "muz", "kiraz", "soğan"}​
   
   urunler_B = {"muz", "kiraz", "çilek", "karpuz", "sarımsak"}​
   - İki kümenin birleşimini bulun​​
   - Sadece meyvelerde olanları bulun​​
   - Ortak elemanları bulun​

5) Kitaplık Uygulaması​

   Her kitabı “ID” ile temsil eden bir sözlük oluştur.​
   Her ID bir alt sözlük tutsun:​

   kitaplar = {1: {"ad": "Suc ve Ceza", "yazar":"Dostoyevski"}, 2: {"ad": "Kürk Mantolu Madonna", "yazar":"Sabahattin Ali"}}
   - Yeni kitap ekleyen​
   - Bir kitabın yazarını güncelleyen
   - Tüm kitapları listeleyen küçük bir program yaz.

7) Alışveriş fişi oluşturma uygulaması (Detay ekran çıktıları ders dokümanında yer alıyor):​
   
   Ürün Listesi: Önceden tanımlanmış ürünler ve fiyatları​
   
   Sepet: Kullanıcının seçtiği ürünler ve miktarları saklanır​
   
   **Kullanıcı Etkileşimi:​**
   - Ürün adı sorulur ("tamam" girilene kadar)​
   - Geçersiz ürün girilirse uyarı verilir​
   - Ürün miktarı sayısal ve pozitif olmalıdır​

   **Sepet Güncelleme:​**
   - Aynı ürün tekrar eklenirse miktar artar​
   - Yeni ürün eklenirse sepete yeni kayıt oluşturulur​

   **Fatura:​**
   - Tüm alınan ürünler listelenir​
   - Her ürünün toplam fiyatı hesaplanır​
   - Genel toplam gösterilir​
