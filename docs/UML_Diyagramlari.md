# UML Diyagramları

## Use Case Diagram

Aktör:
- Kullanıcı

Use Case'ler:
- Sefer Ekle
- Seferleri Görüntüle
- Saat Bilgisi Gir
- Şehir Bilgisi Gir

---

## Class Diagram

### Class: Sefer
Özellikler:
- _sehir
- _saat

Metotlar:
- getSehir()
- getSaat()

---

### Class: OtobusSeferi
Kalıtım:
- Sefer sınıfından türetilmiştir.

Ek Özellik:
- _otobusTipi

Metot:
- getOtobusTipi()

---

### Class: TopluTasimaSistemi
Özellik:
- seferler[]

Metotlar:
- seferEkle()
- listeyiGoster()