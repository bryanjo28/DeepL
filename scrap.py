import requests
from bs4 import BeautifulSoup

# URL situs web yang ingin diambil
url = "https://www.bca.co.id/id/bisnis/layanan/e-banking-bisnis/mybca-bisnis"

# Mengirim request ke situs web
response = requests.get(url)

# Mengecek apakah request berhasil
if response.status_code == 200:
    # Parsing konten HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Mengambil semua teks di halaman
    page_text = soup.get_text(separator="\n", strip=True)
    
    # Menampilkan semua teks di halaman
    print(page_text)
    
    # Menghitung jumlah karakter dalam teks yang diambil
    character_count = len(page_text)
    print("\nJumlah karakter:", character_count)
    
    # Menemukan dan menampilkan semua tautan di halaman
    links = soup.find_all('a')
    print("\nTautan di halaman:")
    for link in links:
        print(link.get('href'))
else:
    print("Gagal mengakses situs")
