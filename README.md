# Data Communication Project - Error Detection & Correction

Bu proje, veri iletimi sırasında oluşabilecek hataları simüle etmek ve çeşitli hata algılama algoritmalarını (Parity, CRC, Hamming, 2D Parity) uygulamalı olarak göstermek amacıyla geliştirilmiştir. Python Socket Programlama kullanılarak **Client-Server** mimarisi üzerine kurulmuştur.

## 📂 Proje Yapısı

Proje, birbiriyle haberleşen 3 ana bileşenden oluşur:

1. **Client 1 (Gönderici):**
   - Kullanıcıdan metin alır.
   - Seçilen yönteme göre (CRC, Parity vb.) kontrol verisi (checksum) üretir.
   - Veriyi paketleyip (`DATA|METHOD|CONTROL`) sunucuya gönderir.

2. **Server (Gürültü Simülasyonu):**
   - Veriyi aracı düğüm olarak alır.
   - Rastgele hata enjeksiyonu yapar (Bit Flip, Karakter Silme, Ekleme veya Değiştirme).
   - Bozulmuş veriyi alıcıya iletir.

3. **Client 2 (Alıcı ve Kontrol):**
   - Gelen paketi analiz eder.
   - Kendi tarafında kontrol verisini yeniden hesaplar.
   - Orijinal kontrol verisiyle karşılaştırıp **"DATA CORRECT"** veya **"DATA CORRUPTED"** raporu verir.

## 🚀 Kullanılan Algoritmalar

Proje aşağıdaki hata algılama yöntemlerini destekler:
* **Parity Bit:** Tek/Çift eşlik kontrolü.
* **CRC-16 (Cyclic Redundancy Check):** Polinom tabanlı güçlü hata tespiti.
* **2D Parity:** Matris tabanlı satır ve sütun kontrolü.
* **Hamming Code:** Hata tespiti ve tek bitlik düzeltme simülasyonu.

## 💻 Nasıl Çalıştırılır?

Bağlantı hatalarını önlemek için dosyaları **mutlaka aşağıdaki sırayla** ve 3 ayrı terminalde çalıştırınız:

### Adım 1: Alıcıyı Başlat
```bash
python client2.py
```

### Adım 2: Sunucuyu (Bozucu) Başlat
```bash
python server.py
```

### Adım 3: Göndericiyi Başlat ve Veri Gir
```bash
python client1.py
```

## ⚠️ Hata Senaryoları (Error Injection)

Sunucu (Server.py), veri iletimi sırasında aşağıdaki hataları rastgele uygular:
* **Substitution:** Bir karakteri rastgele değiştirir.
* **Deletion:** Veriden bir karakter siler.
* **Insertion:** Veriye rastgele karakter ekler.
* **Swapping:** İki karakterin yerini değiştirir.
