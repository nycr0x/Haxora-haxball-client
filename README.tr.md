<div align="center">

<img src="https://nycr0x.github.io/Haxora-haxball-client/site/Haxora_Icon.png" width="104" alt="Haxora" />

# Haxora — Next-Gen HaxBall Client

**Windows için ücretsiz, bağımsız HaxBall client / masaüstü istemcisi**

Tarayıcıda takılan oyun burada takılmıyor.

[English](README.md) · **Türkçe**

<br />

[![Sürüm](https://img.shields.io/github/v/release/nycr0x/Haxora-haxball-client?label=s%C3%BCr%C3%BCm&color=4f8fbd&style=flat-square)](https://github.com/nycr0x/Haxora-haxball-client/releases/latest)
[![İndirme](https://img.shields.io/github/downloads/nycr0x/Haxora-haxball-client/total?label=indirme&color=4f8fbd&style=flat-square)](https://github.com/nycr0x/Haxora-haxball-client/releases)
[![Platform](https://img.shields.io/badge/platform-Windows%2010%20%2F%2011-4f8fbd?style=flat-square)](https://github.com/nycr0x/Haxora-haxball-client/releases/latest)

**[⬇ İndir](https://github.com/nycr0x/Haxora-haxball-client/releases/latest)** &nbsp;·&nbsp; **[🌐 Haxora HaxBall Client web sitesi](https://nycr0x.github.io/Haxora-haxball-client/)** &nbsp;·&nbsp; **[🐞 Sorun bildir](https://github.com/nycr0x/Haxora-haxball-client/issues)**

</div>

---

Haxora, HaxBall'ı kendi penceresinde açar: daha yüksek FPS, daha az gecikme ve tarayıcıda olmayan bir sürü şey. Kurulum yok, ücretsiz, arayüz Türkçe.

## Öne çıkanlar

| | |
| :-- | :-- |
| ⚡ **Yüksek FPS** | Kare hızı sınırını kaldır. Arka plana alınca oyun yavaşlamaz. |
| 👥 **Arkadaş listesi ve DM** | Kim online görürsün, maçtan çıkmadan yazışırsın. |
| 💬 **Mesaj bildirimi** | Maçın ortasında gelen mesaj sahanın üstünü kapatmayan bir bildirimde çıkar. Konumu ve belirginliği sana kalmış. |
| 🔇 **Susturma** | Sinir olduğun adamı sadece kendi ekranında susturursun. Bot üzerinden yazan odalarda da çalışır. |
| ⚽ **Gol efektleri** | Attığın golle yediğin golün sahadaki görsel efekti ayrı. İkisine ayrı efekt seç, istemezsen kapat. |
| 🎨 **Tema ve görünüm** | Renk, top görünümü, skor tabelası, tuş atamaları. |
| 📤 **Ayar paylaşımı** | Görünüm ve tuş ayarlarını koda çevir, arkadaşına yolla. Sana gelen kodu yapıştır, onun düzeni sende açılsın. |
| 🎵 **Spotify kontrolü** | Şarkıyı maçtan çıkmadan başlat, duraklat, geç. Alt-tab yok, kaçan top yok. |
| 🎮 **Discord Rich Presence** | Sen oynarken Discord profilinde Haxora'da olduğun görünür. |
| 😀 **Avatar tepkileri** | Bir tuşa emoji atarsın, bastığın sürece avatarın o olur. |
| 🎯 **Antrenman modu** | Tek başına şut ve pas çalış. |
| 🎬 **Maç kaydı** | Maçı kaydet, sonra izle. |
| ⭐ **Favori odalar** | Sık girdiğin odalar ve oda geçmişi elinin altında. |
| 🌍 **Türkçe / İngilizce** | Dili ilk açılışta seç, sonra istediğin an değiştir. |

## Kurulum

**1.** [`Haxora.exe`](https://github.com/nycr0x/Haxora-haxball-client/releases/latest) dosyasını indir
**2.** Çift tıkla — kurulum sihirbazı yok, yönetici izni yok

**Gereken:** Windows 10 veya 11, 64-bit

> [!NOTE]
> Windows **"bilgisayarınızı korudu"** derse → **Ek bilgi** → **Yine de çalıştır**.
> Bu uyarı, dosyanın kod imzalama sertifikası olmadığı için çıkar; imzasız her yeni programda çıkar, virüs bulunduğu anlamına gelmez. Sertifika ücretli olduğu için Haxora şimdilik imzasız dağıtılıyor.

## Güvenli mi, ne saklıyor?

Kısa cevap ve kontrol edebileceğin yerler:

- **Sadece buradan indir.** Tek resmî dağıtım kanalı bu reponun [Releases](https://github.com/nycr0x/Haxora-haxball-client/releases) sayfası. Başka sitedeki "Haxora" dosyalarının benimle ilgisi yok.
- **Hesap zorunlu değil.** Odalara girip oynamak için giriş yapmana gerek yok. Hesap yalnızca arkadaş listesi, özel mesaj ve ayar senkronizasyonu için.
- **Ayarların sende.** Tema, tuş atamaları ve favori odalar bilgisayarında yerel olarak tutulur.
- **Spotify.** Bağlantı Spotify'ın kendi giriş ekranından yapılır, Haxora şifreni görmez; yalnızca oynatmayı yönetir (çal / duraklat / geç).
- **Oyunun kendisine dokunmaz.** Haxora [node-haxball](https://github.com/wxyz-abcd/node-haxball) üzerine kurulu bağımsız bir istemcidir; susturma gibi özellikler sadece senin ekranında çalışır, diğer oyuncuları etkilemez.

## Dili değiştirme

Arayüz Türkçe ve İngilizce. Üç yerden değiştirebilirsin:

- **İlk açılış** — karşılama ekranındaki ilk seçim dil
- **Ana menü** — üst bardaki `TR` / `EN` düğmesi
- **Ayarlar** — *Ayarlar → Genel → Arayüz dili*, hem ana menüde hem maçın içinde

Değişiklik anında uygulanır, yeniden başlatmaya gerek yok.

## Sık sorulanlar

<details>
<summary><b>Susturma karşı tarafı etkiler mi?</b></summary>

Hayır. Susturma sadece senin ekranında geçerli, diğer oyuncular o kişiyi görmeye devam eder.
</details>

<details>
<summary><b>Ücretli mi, reklam var mı?</b></summary>

Hayır. Haxora ücretsiz, içinde reklam yok.
</details>

<details>
<summary><b>Mac veya Linux sürümü var mı?</b></summary>

Şu an sadece Windows 64-bit destekleniyor.
</details>

<details>
<summary><b>Güncelleme nasıl geliyor?</b></summary>

Yeni sürümler [Releases](https://github.com/nycr0x/Haxora-haxball-client/releases) sayfasından yayınlanır, değişiklikler sürüm notlarında yazar.
</details>

## Sorun bildirme

Bir şey çalışmıyorsa ya da fikrin varsa → **[issue aç](https://github.com/nycr0x/Haxora-haxball-client/issues)**

Şunları yazarsan çok daha hızlı çözülür:

- Haxora sürümü
- Ne yaptığında oluyor, adım adım
- Varsa ekran görüntüsü

---

<div align="center">
<sub>

Haxora bağımsız bir projedir; HaxBall ile resmî bir bağı, ortaklığı veya onayı yoktur.
[node-haxball](https://github.com/wxyz-abcd/node-haxball) üzerine kurulu · MIT · [nycr0x](https://github.com/nycr0x)

</sub>
</div>
