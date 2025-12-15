## Python Hash Cracker 

Bu proje, siber güvenlik operasyonlarında (SOC) sıkça karşılaşılan **Hashing** algoritmalarının mantığını kavramak ve **Brute-Force** saldırılarının mekaniğini anlamak amacıyla geliştirilmiş, Python tabanlı bir güvenlik aracıdır.

> **⚠YASAL UYARI:** Bu yazılım sadece eğitim ve test amaçlı (Educational Purposes Only) geliştirilmiştir. İzinsiz sistemlerde kullanılması yasaktır.

##  Projenin Amacı
Saldırganların kullandığı yöntemleri anlamak, savunma yapmanın ilk adımıdır. Bu proje ile şunlar hedeflenmiştir:
* **Kriptografi Temelleri:** MD5, SHA1, SHA256 gibi algoritmaların işleyişini kod seviyesinde anlamak.
* **Otomasyon Yeteneği:** Manuel yapılabilecek işlemleri Python scriptleri ile hızlandırmak.
* **Python CLI Geliştirme:** argparse kütüphanesi ile kullanıcı dostu komut satırı araçları yazmak.

## Özellikler
* **Otomatik Algılama:** Girilen hash değerinin türünü (MD5, SHA1, SHA256 vb.) uzunluğuna bakarak otomatik tespit eder.Elle girme seçeneği de mevcut.
* **Çoklu Algoritma Desteği:** MD5, SHA1, SHA256 ve SHA512 algoritmalarını destekler.
* **Hata Yönetimi:** Bozuk wordlist dosyaları veya hatalı girdilerde programın çökmesini engelleyen hata yakalama blokları.

## Kurulum ve Kullanım
* **help:** Help komutu içerisinde bilgiler mevcut