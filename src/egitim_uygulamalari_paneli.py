#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Pardus Eğitim Uygulamaları Kısayol Paneli
ÇalıPardusLab2 / Pardus Hata Yakalama ve Öneri Yarışması 2026

Bu ilk prototip, eğitim ortamlarında sık kullanılan uygulamalara
tek menü üzerinden erişim fikrini göstermektedir.
Gerçek uygulama başlatma işlemi yapmaz; simülasyon çıktıları üretir.
"""

UYGULAMALAR = {
    "1": {
        "ad": "LibreOffice Writer",
        "aciklama": "Metin belgesi hazırlamak için kullanılır."
    },
    "2": {
        "ad": "LibreOffice Impress",
        "aciklama": "Sunum hazırlamak için kullanılır."
    },
    "3": {
        "ad": "Web Tarayıcı",
        "aciklama": "İnternet araştırmaları ve eğitim portalları için kullanılır."
    },
    "4": {
        "ad": "Dosya Yöneticisi",
        "aciklama": "Belgeler, indirilenler ve ders materyallerine erişim sağlar."
    },
    "5": {
        "ad": "Terminal",
        "aciklama": "Komut satırı işlemleri ve teknik çalışmalar için kullanılır."
    },
    "6": {
        "ad": "Hesap Makinesi",
        "aciklama": "Matematiksel işlemler için kullanılır."
    }
}


def baslik_yaz() -> None:
    print("=" * 65)
    print("PARDUS EĞİTİM UYGULAMALARI KISAYOL PANELİ")
    print("=" * 65)
    print("Eğitim uygulamalarına hızlı erişim prototipi\n")


def menu_goster() -> None:
    print("Lütfen açmak istediğiniz uygulamayı seçin:")
    for kod, bilgi in UYGULAMALAR.items():
        print(f"{kod} - {bilgi['ad']}")
    print("7 - Uygulama açıklamalarını göster")
    print("8 - Çıkış")
    print()


def uygulama_ac(secim: str) -> None:
    uygulama = UYGULAMALAR.get(secim)

    if uygulama:
        print(f"\n[{uygulama['ad']}]")
        print(f"{uygulama['ad']} açılıyor... (simülasyon)")
        print("İşlem tamamlandı.\n")
    else:
        print("\nGeçersiz uygulama seçimi.\n")


def aciklamalari_goster() -> None:
    print("\n[Uygulama Açıklamaları]")
    for kod, bilgi in UYGULAMALAR.items():
        print(f"{kod} - {bilgi['ad']}: {bilgi['aciklama']}")
    print()


def ana_program() -> None:
    baslik_yaz()

    while True:
        menu_goster()
        secim = input("Seçiminiz: ").strip()

        if secim in UYGULAMALAR:
            uygulama_ac(secim)
        elif secim == "7":
            aciklamalari_goster()
        elif secim == "8":
            print("\nKısayol paneli kapatıldı.")
            break
        else:
            print("\nGeçersiz seçim yaptınız. Lütfen tekrar deneyin.\n")


if __name__ == "__main__":
    ana_program()
