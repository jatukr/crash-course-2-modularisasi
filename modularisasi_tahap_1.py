"""
Program menghitung luas segitiga
luas_segitiga = alas x tinggi / 2
"""
print('Luas Segitiga 1')
alas = 10
tinggi = 6
luas_segitiga = alas * tinggi / 2
print(f'Segitiga dengan alas={alas} dan tinggi={tinggi} memiliki luas {luas_segitiga}')

print('\nLuas Segitiga 2 dengan copy paste')
alas = 30
tinggi = 10
luas_segitiga = alas * tinggi / 2
print(f'Segitiga dengan alas={alas} dan tinggi={tinggi} memiliki luas {luas_segitiga}')

def hitung_luas_segitiga(alas, tinggi):
    luas_segitiga = alas * tinggi / 2
    return  luas_segitiga
print(f'Menghitung luas segitiga dengan fungsi, {hitung_luas_segitiga(10,8)}')
