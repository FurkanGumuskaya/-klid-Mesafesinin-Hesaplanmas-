import math

# İki nokta arasındaki Öklid mesafesini hesaplayan fonksiyon
def oklid_mesafesi(x1, y1, x2, y2):
    q = x2 - x1
    r = y2 - y1
    p = math.sqrt(q**2 + r**2)
    return p

# Kullanıcıdan noktaların koordinatlarını alma
def kullanici_girdisi():
    while True:
        try:
            x1 = float(input("Birinci noktanın x koordinatını girin: "))
            y1 = float(input("Birinci noktanın y koordinatını girin: "))
            x2 = float(input("İkinci noktanın x koordinatını girin: "))
            y2 = float(input("İkinci noktanın y koordinatını girin: "))
            return x1, y1, x2, y2
        except ValueError:
            print("Geçersiz giriş! Lütfen sayı girin.")

# Ana program döngüsü
def ana_program():
    while True:
        x1, y1, x2, y2 = kullanici_girdisi()
        mesafe = oklid_mesafesi(x1, y1, x2, y2)
        print(f"({x1}, {y1}) ve ({x2}, {y2}) noktaları arasındaki Öklid mesafesi: {mesafe:.2f}")

        devam = input("Başka bir mesafe hesaplamak ister misiniz? (Evet/Hayır): ").strip().lower()
        if devam != 'evet':
            break

# Programı çalıştır
if __name__ == "__main__":
    ana_program()
