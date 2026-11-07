# Haxora GitHub Pages

Site: https://nycr0x.github.io/Haxora-haxball-client/

## Yayına alma

Mevcut GitHub Pages kaynağını değiştirmeden güncellenmiş `docs/` dosyalarını
repo köküne uygula. `docs/docs/` oluşturma. `scripts/` klasörü ve bu belge site
kaynağının dışında kalır; uygulamanın `version` dosyasını değiştirmez.

GitHub erişimi olmadığı için bu değişiklikler hazırlandıkları oturumda uzak
repoya gönderilmedi. Yerel dosyaların değişmesi canlı siteyi güncellemez.

## Neler değişti?

- Türkçe ana sayfa her ziyarette Türkçe ve kendi canonical adresinde kalır.
  İngilizce düğmesi gerçek `/en/` sayfasına gider. Eski `?lang=en` bağlantıları
  JavaScript açıkken `/en/` adresine yönlenir; JavaScript kapalıyken ana sayfa
  ve İngilizce bağlantısı kullanılabilir. Kayıtlı dil tercihi canonical değiştirmez.
- Ana sayfa içeriği ve sürüm bilgisi JavaScript/API çağrısı olmadan görünür.
  Kaydırma animasyonunun içeriği görünmez bırakması kaldırıldı.
- Ana sayfaya kullanım senaryoları ve geliştirici bağlantısı eklendi.
  Tasarımın renkleri, saha animasyonu ve mevcut özellik bölümleri korundu.
- Sürüm bilgisi GitHub'ın en son kararlı sürümünden HTML'e yazıldı. Kurulum
  ve ZIP seçenekleri gerçek sürüm dosyalarıyla eşleştirildi.
- Logonun `screenshot` olarak tanımlanması kaldırıldı. Gerçek ekran görüntüsü
  depoda olmadığı için temsili bir görsel gerçek ürün görüntüsü gibi eklenmedi.
- Ana sitemap `docs/sitemap.xml`. `docs/site/sitemap.xml` geçmiş gönderimleri
  bozmamak için aynı içeriğin uyumluluk kopyası olarak tutulur. Yeni gönderimde
  yalnızca ana sitemap kullanılmalı. `priority` ve `changefreq` kaldırıldı.
- `.nojekyll` ile statik dosyaların doğrudan yayımlanması belirtilir.

Bunlar tespit edilen tutarsızlıkları giderir; indekslenmeme nedeninin kanıtı
veya Google'da sıralama garantisi değildir.

## Yeni sürüm yayımlandığında

Python 3.9+ ile repo kökünde çalıştır:

```bash
python scripts/update_site_release.py
git diff
```

Komut en son yayımlanmış kararlı GitHub sürümünü okur. Ana sayfadaki sürüm,
kurulum dosyası boyutu, yayın tarihi ve sürüm notlarını; İngilizce sayfadaki
sürüm özetini ve iki sayfanın SoftwareApplication verisini günceller.
HTML değiştiğinde ilgili sitemap `lastmod` değerlerini de günceller.
Güncellenen dosyaları commit edip GitHub'a gönder. Komut kendiliğinden push yapmaz.
İndirme düğmeleri `/releases/latest` üzerinden güncel dosyalara erişir.

`version` uygulama güncelleme mekanizmasına ait olabileceği için bu komut
tarafından değiştirilmez. Scriptin kabul ettiği kurulum dosyası adı
`Haxora-Setup.exe`; ileride ad değişirse scripti de güncelle.

## Search Console — yayın tamamlandıktan sonra

1. URL öneki mülkü: `https://nycr0x.github.io/Haxora-haxball-client/`.
2. Site Haritaları'nda şu tam URL'yi gönder:
   `https://nycr0x.github.io/Haxora-haxball-client/sitemap.xml`.
3. Ana sayfa URL Denetimi'nde canlı testi çalıştır. Görüntülenen HTML'de
   canonical ana sayfayı, dil `tr` değerini, sürüm alanı dolu içeriği göstermeli.
4. Bir kez dizine ekleme iste. Google Dizini sekmesinde son tarama tarihinin
   yeni yayından sonraya geçip geçmediğini takip et. Günlük tekrar isteme.
5. Sitemap yine okunamazsa tam hata ayrıntısını incele; robots veya domain
   değiştirmenin sorunu otomatik çözeceğini varsayma.

Bu bir proje sitesi. Etkili robots.txt adresi `https://nycr0x.github.io/robots.txt`
olur; bu repoya `docs/robots.txt` eklemek host kökündeki robots.txt'yi yönetmez.
Bu nedenle etkisiz bir robots.txt eklenmedi.
